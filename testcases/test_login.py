import unittest
from unittestreport import ddt,list_data
from common.handle_excel import Handle_Excel

@ddt
class TestLogin(unittest.TestCase):
    excel = Handle_Excel()
    cases = excel.read_excel()



    @list_data(cases)
    def test_login(self,item):
