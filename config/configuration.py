import os

ROOT = os.getcwd()
DIR_DATA = os.path.join(ROOT, "data")
DEBUG = True


def main():
    try:
        os.makedirs(DIR_DATA)
    except OSError:
        if not os.path.isdir(DIR_DATA):
            print("Error to create data")
