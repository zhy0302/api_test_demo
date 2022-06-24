#导包
import unittest
import json
from api.login import LoginAPI
from parameterized import parameterized
#构建测试数据
def build_data():
    test_data = []
    #指定文件路径
    json_file = "../data/login.json"
    #打开json文件
    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            login_data = case_data.get("login_data")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            #error_code = case_data.get("error_code")
            message = case_data.get("message")
            test_data.append((login_data, status_code, code, message))
            print("test_data = {}".format(login_data, status_code, code, message))
    return test_data

#创建测试类
class TestLogin(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_api = LoginAPI()
    #后置处理
    #def tearDown(self):
    #    pass
    @parameterized.expand(build_data)
    #定义测试用例
    def test01_login(self, login_data, status_code, code, message):
        #调用登录接口进行登录
        response = self.login_api.login(login_data)
        print(response.json())
    #断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        #self.assertIn(error_code, response.json().get("error_code"))
        self.assertIn(message, response.json().get("message"))