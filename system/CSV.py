from system.File import File
import csv


class CSV(File):
    def __init__(self, name):
        File.__init__(self, name)
        self.fieldnames = ["Captor", "Time", "Level"]

    def f_read(self):
        with open(super().getfilename(), 'r', newline='') as file:
            dialect = csv.excel()
            reader = csv.DictReader(file,  fieldnames=self.fieldnames, dialect=dialect, delimiter=';')
            for row in reader:
                yield row

    def f_write(self, data):
        """

        :param data: dict
        :return: None
        """
        with open(super().getfilename(), 'w', newline='') as file:
            dialect = csv.excel()
            writer = csv.DictWriter(file, fieldnames=self.fieldnames, dialect=dialect, delimiter=';')
            writer.writeheader()
            writer.writerow(data)

    def f_append(self, data):
        """

        :param data: dict
        :return: None
        """
        with open(super().getfilename(), 'a', newline='') as file:
            dialect = csv.excel()
            writer = csv.DictWriter(file, fieldnames=self.fieldnames, dialect=dialect, delimiter=';')
            writer.writerow(data)