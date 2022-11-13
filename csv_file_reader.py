import csv

class CSVFileReader:
    def __init__(self, file_name, delimiter=','):
        self.file_name = file_name
        self.delimiter = delimiter

    def get_content(self):
        header = None
        values = []
        with open(self.file_name, newline='') as file:
            reader = csv.reader(file, delimiter=self.delimiter, quotechar='|')
            for row in reader:
                if reader.line_num == 1:
                    header = row
                else:
                    values.append(row)
        return header, values
