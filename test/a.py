import configparser
import os
base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(base_path)
from selenium import webdriver





ini_file_path = os.path.join(base_path, 'iselenium.ini')
print(ini_file_path)
config = configparser.ConfigParser()
config.read(ini_file_path)
print(config.get("driver","chrome_driver"))

driver=webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'))
driver.get("http://www.baidu.com")