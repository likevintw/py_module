# .xls

import xlrd
import unittest


class TestFolderPathHandler(unittest.TestCase):
    @unittest.skip("Pass")
    def test_show_sheet_name(self):
        workbook = xlrd.open_workbook('test.xls')
        for sheet_name in workbook.sheet_names():
            print(sheet_name)

    @unittest.skip("Pass")
    def test_read_cell_color(self):
        workbook = xlrd.open_workbook("test.xls", formatting_info=True)
        sheet = workbook.sheet_by_index(0)  # read first sheet
        print(workbook.sheet_names())
        print("Total Row: ", sheet.nrows)
        print("Total Column: ", sheet.ncols)
        for col_index in range(sheet.ncols):  # Column Loop
            for row_index in range(sheet.nrows):  # Row Loop
                thecell = sheet.cell(row_index, col_index)
                # print("Cell Data: {}".format(thecell.value))  # show data
                cell_xf_index = sheet.cell_xf_index(row_index, col_index)
                cell_xf = workbook.xf_list[cell_xf_index]
                background = cell_xf.background.pattern_colour_index
                print("Cell Color:{}".format(background))  # show color
