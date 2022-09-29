import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATAS_DIR =os.path.join(BASE_DIR,'datas')

CONF_DIR =os.path.join(BASE_DIR,'conf')

LOG_DIR = os.path.join(BASE_DIR,'logs')

REPORT_DIR =os.path.join(BASE_DIR,'reports')

CASES_DIR = os.path.join(BASE_DIR,'testcases')