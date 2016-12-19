from PIL import Image

def dimension_counts(filepaths):
    """
    Given a list of filepaths, return a dictionary of the counts of each image size occurrence 
    """
    image_dimensions_counts = {}
    for image_filepath in filepaths:
        img = Image.open(image_filepath)
        size = img.size
        if size not in image_dimensions_counts:
            image_dimensions_counts[size] = 1
        else:
            image_dimensions_counts[size] += 1
    return image_dimensions_counts
