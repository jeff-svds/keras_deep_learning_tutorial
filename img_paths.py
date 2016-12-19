import os, random, re

def extract_label(filepath):
    """
    Parses out the class label from the filename
    """
    basename = os.path.basename(filepath)
    matcher = re.search("(.+)\.\d+\.jpg", basename)
    label = matcher.group(1)
    return label

def sample_paths(training_images_filepaths, fraction):
    """
    Given an array of filepaths, return a random sample of them
    """
    training_images_count = len(training_images_filepaths)
    sample_size = int(fraction * training_images_count)
    sample_indices = random.sample(range(training_images_count), sample_size)
    training_images_filepaths_sample = [training_images_filepaths[i] for i in sample_indices]
    return training_images_filepaths_sample

def sample_paths_labels(training_images_filepaths, fraction):
    """
    Returns array of filepaths and their labels (i.e., X, y in SciKit Learn parlance)
    """
    filepaths  = sample_paths(training_images_filepaths, fraction)
    labels = list(map(extract_label, filepaths))
    return filepaths, labels

def clear_training_validation_directories(parent_directory, labels):
    """
    Removes symlinks from training and validation subdirectories
    """
    for subdirectory in ['training', 'validation']:
        directory_path = parent_directory + '/' + subdirectory
        for label in labels:
            label_string = str(label)
            for file in os.listdir(directory_path + '/' + label_string):
                filepath = os.path.join(directory_path, label_string, file)
                if os.path.islink(filepath):
                    os.unlink(filepath)

def symlink_files(source_directory, parent_directory, subdirectory, filepaths, labels):
    """
    source_directory: original image directory to symlink from
    parent_directory: parent directory of training and validation subfolders
    filepaths: array of image filepaths
    labels: array of class labels for each file in filepaths
    """
    directory_path = parent_directory + '/' + subdirectory
    for i, filepath in enumerate(filepaths):
        basename = os.path.basename(filepath)
        os.symlink(source_directory + '/' + basename, directory_path + '/' + str(labels[i]) + '/' + basename)

import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img

def show(filepaths, rows=1, figsize=(12, 6)):
    f = plt.figure(figsize=figsize)
    filepaths_count = len(filepaths)
    for i in range(filepaths_count):
        sp = f.add_subplot(rows, filepaths_count//rows, i+1)
        img = load_img(filepaths[i])
        plt.imshow(img)
