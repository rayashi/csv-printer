
from prettytable import PrettyTable

class TablePrinter:
    def __init__(self, header, rows):
        self.header = header
        self.rows = rows

    def print(self):
      table = PrettyTable()
      table.field_names = self.header
      table.add_rows(self.rows)
      print(table)


