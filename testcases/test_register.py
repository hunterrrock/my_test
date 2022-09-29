import unittest
import os
import requests
import random
from unittestreport import ddt, list_data
from common.handle_excel import Handle_Excel
from common.handle_path import DATAS_DIR
from common.handle_conf import conf
from common.tools import replace_data
from common.handle_log import mylog
from common.handle_db import HandleMysql


@ddt
class TestRegister(unittest.TestCase):
    excel = Handle_Excel(os.path.join(DATAS_DIR, 'datas.xlsx'), 'register')
    cases = excel.read_excel()
    db = HandleMysql()

    @list_data(cases)
    def test_register(self, item):
        # 准备用例数据
        url = conf.get('env', 'base_url') + item['url']
        method = item['method'].lower()
        if '#mobile#' in item['data']:
            setattr(TestRegister, 'mobile', self.random_mobile())
        elif '#pass_mobile#' in item['data']:
            sql = 'SELECT * FROM futureloan.member WHERE LENGTH(mobile_phone) =11 LIMIT 1'
            passmobile = self.db.search_one(sql)['mobile_phone']
            setattr(TestRegister, 'pass_mobile', passmobile)
        item['data'] = replace_data(item['data'], TestRegister)
        print(item['data'])
        # print(item['data'])
        params = eval(item['data'])
        expected = eval(item['expected'])
        headers = eval(conf.get('env', 'headers_v1'))
        # 發送請求
        response = requests.request(method=method, json=params, url=url, headers=headers)
        res = response.json()
        # 请求后检查数据库，该手机号是否存在库中
        sql = 'SELECT * FROM futureloan.member WHERE mobile_phone ={}'.format(self.mobile)
        result = self.db.search_count(sql)
        # 做断言
        try:
            self.assertEqual(res['code'], expected['code'])
            self.assertEqual(res['msg'], expected['msg'])
            if res['msg'] == 'OK':
                self.assertEqual(result, 1)
        except AttributeError as e:
            mylog.error('----用例【{}】----执行失败----'.format(item['title']))
            mylog.exception(e)
            raise e
        else:
            mylog.info('----用例【{}】----执行成功----'.format(item['title']))

    def random_mobile(self):
        mobile = '133'
        for i in range(8):
            n = str(random.randint(0, 9))
            mobile += n
        return mobile
