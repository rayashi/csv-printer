

from prettytable import PrettyTable
from csv_file_reader import * 
from table_printer import * 

def print_table():
    reader = CSVFileReader(file_name='file.csv')
    header, values = reader.get_content()
    printer = TablePrinter(header=header, rows=values)
    printer.print()

def print_table_old():
    table = PrettyTable()
    with open('file.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        for row in reader:
            if reader.line_num == 1:
                table.field_names = row
            else:
                table.add_row(row)

        print(table)


if __name__ == '__main__':
    print_table_old()
    print_table()





