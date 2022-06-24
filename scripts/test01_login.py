#导包
import unittest
from api.login import LoginAPI
import app
#创建测试类
class TestLogin(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_api = LoginAPI()    #实例化接口
    #后置处理
    #def tearDown(self):
    #    pass
    #定义测试用例
    #case001  登录成功
    def test01_001(self):
        #调用登录接口进行登录
        response = self.login_api.login({"identifier":"zhuhongyu","password":"veeron2020"})
        print(response.json())
        #断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get("code"))
        self.assertIn("OK", response.json().get("message"))
        self.assertIn("zhuhongyu", response.json().get("data").get("user").get("username"))

        # 提前token信息
        app.TOKEN = "Bearer " + response.json().get("data").get("access_token")
        print(app.TOKEN)
        app.headers_data["Authorization"] = app.TOKEN
        print(app.headers_data)
    #case002 不输入用户名或用户名错误
    def test02_002(self):
        #调用登录接口进行登录
        response = self.login_api.login({"identifier":"","password":"veeron2020"})
        print(response.json())
    #断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(400, response.json().get("code"))
        self.assertEqual("username_unsigned_up", response.json().get("error_code"))
        self.assertIn("用户名未注册", response.json().get("message"))
    # case003 不输入密码或密码错误
    def test03_003(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"identifier": "zhuhongyu", "password": ""})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(400, response.json().get("code"))
        self.assertEqual("password_incorrect", response.json().get("error_code"))
        self.assertIn("密码不正确", response.json().get("message"))

    # case004 多参
    def test04_004(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"identifier": "zhuhongyu", "password": "veeron2020","haha":"xixi"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get("code"))
        self.assertIn("OK", response.json().get("message"))
    #case005 少参-少用户名
    def test05_005(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"password": "veeron2020"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(400, response.json().get("code"))
        self.assertEqual("username_unsigned_up", response.json().get("error_code"))
        self.assertIn("用户名未注册", response.json().get("message"))

