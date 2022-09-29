import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding='utf-8')


conf = Config(os.path.join(CONF_DIR, 'conf'))

if __name__ =='__main__':
    print(conf.get('env','base_url'))