import xlrd
from os_path_scripts import PROJECT_ROOT_PATH, resources
import os


def test_xls():

    xls_path = os.path.join(PROJECT_ROOT_PATH, resources, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_path)
    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    assert book.nsheets == 1

    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    print(f'Количество строк {sheet.nrows}')
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}')
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=8, colx=2) == 'Melgar'