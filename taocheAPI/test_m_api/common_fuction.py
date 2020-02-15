import random
import json
import requests
from taocheAPI.config import config
from taocheAPI.config import Test_M

header = {'Content-Type': "application/json"}

# 登录
def M_Login(userName,userPwd,):
    data = json.dumps({'mobile': userName,
                       'password': userPwd,
                       })
    result = requests.post(Test_M.login_url, data=data, headers=header).json()
    return result