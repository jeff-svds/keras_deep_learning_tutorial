import bcolz

def save_array(fname, arr):
    bcolz.carray(arr, rootdir=fname, mode='w').flush()


def load_array(fname):
    return bcolz.open(fname)[:]
