import logging
import os
from common.handle_conf import conf
from common.handle_path import LOG_DIR


class HandleLog():

    def __init__(self, name='mylog', level='DEBUG', filename='log.log', sh_level='DEBUG', fh_level='DEBUG'):
        self.name = name
        self.level = level
        self.filename = filename
        self.sh_level = sh_level
        self.fh_level = fh_level

    def log(self):
        # 创建一个日志收集器
        log = logging.getLogger(self.name)
        # 设置日志收集器的等级
        log.setLevel(self.level)
        # 创建日志输出渠道
        sh = logging.StreamHandler()
        fh = logging.FileHandler(self.filename)
        # 设置日志输出渠道的等级
        sh.setLevel(self.sh_level)
        fh.setLevel(self.fh_level)
        # 绑定输出渠道到日志收集器
        log.addHandler(sh)
        log.addHandler(fh)
        # 设置输出格式
        log_format = logging.Formatter('%(asctime)s-[%(filename)s-->LINE:%(lineno)d]-%(levelno)s:%(message)s')
        # 绑定输出格式到输出渠道
        sh.setFormatter(log_format)
        fh.setFormatter(log_format)
        return log


log = HandleLog(
    name=conf.get('logging', 'name'),
    level=conf.get('logging', 'level'),
    filename=os.path.join(LOG_DIR, conf.get('logging', 'filename')),
    sh_level=conf.get('logging', 'sh_level'),
    fh_level=conf.get('logging', 'fh_level')
)
mylog = log.log()
