from selenium import webdriver


class TestBaidu():
    def setup_class(self):
        self.driver=webdriver.Chrome()
    def test_index1(self):
        self.driver.get("https://www.baidu.com")
    def teardown_class(self):
        self.driver.quit()

