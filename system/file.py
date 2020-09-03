import os
from config.configuration import DIR_DATA, DEBUG


class File:
    def __init__(self, name):
        self.filename = os.path.join(DIR_DATA, name)

    def f_write(self, data):
        with open(self.filename, "w") as file:
            file.write(data)

    def f_append(self, data):
        with open(self.filename, "a") as file:
            file.write(data)

    def f_read(self):
        with open(self.filename, "r") as file:
            return file.read()

    def f_lines(self):
        with open(self.filename, "r") as file:
            return file.readlines()

    def __del__(self):
        if not DEBUG:
            os.remove(self.filename)
