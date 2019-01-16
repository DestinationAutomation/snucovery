import unittest
import pytest
from snucovery.excel import ExcelWorkbooks
from snucovery.errors import InvalidWorksheetName, WorksheetNotExists


class TestExcel(unittest.TestCase):
    def test_init_aws_service(self):
        excel = ExcelWorkbooks('test_workbook.xlsx')
        self.assertIsInstance(excel, object)

    def test_create_workbook(self):
        excel = ExcelWorkbooks('test_workbook.xlsx')
        self.assertTrue(excel.workbook)

    def test_get_workbook_name_no_ext(self):
        excel = ExcelWorkbooks('test_workbook')
        self.assertEqual(excel.workbook_name[-5:], '.xlsx')

    def test_create_worksheet(self):
        excel = ExcelWorkbooks('test_workbook')
        worksheet = excel.create_worksheet('foo')
        self.assertIsInstance(worksheet, object)

    def test_create_worksheet_fail(self):
        excel = ExcelWorkbooks('test_workbook')
        with self.assertRaises(InvalidWorksheetName):
            excel.create_worksheet('')

    def test_add_new_worksheet(self):
        excel = ExcelWorkbooks('test_workbook')
        excel.create_worksheet('foo_test')
        self.assertTrue(excel.worksheets['foo_test'])

    def test_get_worksheets(self):
        excel = ExcelWorkbooks('test_workbook')
        excel.create_worksheet('foo_test')
        self.assertGreater(len(excel.get_worksheets()), 0)

    def test_get_worksheet(self):
        excel = ExcelWorkbooks('test_workbook')
        excel.create_worksheet('foo_test')
        self.assertTrue(excel.get_worksheet('foo_test'))

    def test_get_worksheet_raise_exception(self):
        excel = ExcelWorkbooks('test_workbook')
        with self.assertRaises(WorksheetNotExists):
            excel.get_worksheet('foo_test')

    def test_set_workbook_name(self):
        excel = ExcelWorkbooks('test_workbook')
        self.assertEqual(excel.workbook_name, 'test_workbook.xlsx')

    def test_set_workbook_name_with_ext(self):
        excel = ExcelWorkbooks('test_workbook.xlsx')
        self.assertEqual(excel.workbook_name, 'test_workbook.xlsx')

    def test_get_workbook(self):
        excel = ExcelWorkbooks('test_workbook')
        self.assertTrue(excel.get_workbook())

    def test_get_workbook_with_unset(self):
        excel = ExcelWorkbooks('test_workbook')
        del excel.workbook
        self.assertTrue(excel.get_workbook())
