import re
from common.handle_conf import conf


def replace_data(data, cls):
    """
    while循环，如果需要替换才执行该循环，不需要替换不执行
    :param data:
    :param cls:
    :return:
    """
    while re.search('#(.+?)#', data):
        # 获取re对象
        res = re.search('#(.+?)#', data)
        # 　获取需要被替换的数据
        item = res.group()
        # 获取对应的属性名
        attr = res.group(1)
        try:
            value = getattr(cls,attr)
        except:
            value = conf.get('test_data',attr)
        # 替换
        data = data.replace(item,str(value))
    return data
