
import unittest
import openpyxl


class TestExcelHandler(unittest.TestCase):
    # @unittest.skip("Pass")
    def test_show_sheet_title(self):
        workbook = openpyxl.load_workbook("test.xlsx")
        for sheet in workbook:
            print(sheet.title)  # get a string
