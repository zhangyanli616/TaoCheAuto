# -*- coding: utf-8 -*-
import json
import requests
from titan import tt_config
from titan import LOG


class CorpWeChat(object):
    def __init__(self):
        self.url = "https://qyapi.weixin.qq.com"
        self.corpid = tt_config.CORPID
        self.secret = tt_config.SECRET
        self.agentid = tt_config.AGENTID

    # 获取企业微信的 access_token
    def access_token(self):
        url_arg = '/cgi-bin/gettoken?corpid={id}&corpsecret={crt}'.format(
            id=self.corpid, crt=self.secret)
        url = self.url + url_arg
        response = requests.get(url=url)
        text = response.text
        self.token = json.loads(text)['access_token']

    # 构建消息格式
    def messages(self, to_user, msg):
        values = {
            "touser": to_user,
            "msgtype": 'text',
            "agentid": self.agentid,
            "text": {'content': msg},
            "safe": 0
        }
        self.msg = (bytes(json.dumps(values), 'utf-8'))

    # 发送信息
    def send_message(self, to_user, msg):
        self.access_token()
        send_url = '{url}/cgi-bin/message/send?access_token={token}'.format(
            url=self.url, token=self.token)
        for user in to_user:
            self.messages(user, msg)
            response = requests.post(url=send_url, data=self.msg)
            errcode = json.loads(response.text)['errcode']

            if errcode != 0:
                LOG.error('企业微信发送失败。')


WeChat = CorpWeChat()


