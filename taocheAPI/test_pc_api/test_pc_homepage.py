import requests
from taocheAPI.base import Base
from taocheAPI.config import config
from titan.tt_log import LOG
from titan import tt_check

default_url = config.home_url


class HomePageAPI(Base):
    @staticmethod
    def test_getbaozhencar():
        """测试保真车获取接口@author:zhaoliuming"""
        response = requests.get(default_url + "ajax/jsonp/getbaozhencar.ashx?cid=201&tid=1&callback=jQuery112402816550473892061_1564803591809")
        LOG.info("【访问】" + default_url + "ajax/jsonp/getbaozhencar.ashx?cid=201&tid=1&callback=jQuery112402816550473892061_1564803591809")
        status = response.status_code
        tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)
        tt_check.assertRegex(response.text, "成功", "返回是否包含成功")

