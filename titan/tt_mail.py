from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody
from titan import tt_config


class Mail:

    def __init__(self):
        self.email_name = tt_config.EMAIL_NAME
        self.email_password = tt_config.EMAIL_PASSWORD

    def email(self, to, subject, body):
        """
        发送邮件
        :param to: 接收人
        :param subject: 邮件主题
        :param body: 邮件内容
        :return:
        """
        creds = Credentials(
            username=self.email_name,
            password=self.email_password
        )
        account = Account(
            primary_smtp_address=self.email_name + '@taoche.com',
            credentials=creds,
            autodiscover=True,
            access_type=DELEGATE
        )
        m = Message(
            account=account,
            subject=subject,
            body=HTMLBody(body),
            to_recipients=[Mailbox(email_address=i) for i in to]

        )
        m.send()


    def send_email(self, project_name, receivers, report_full_name):
        """
        封装email,将指定测试报告放入邮件正文
        :param receivers: 接收人 集合；['test1@taoceh.com','test2@taoche.com']
        :param report_full_name: 报告全路径名称
        :return:
        """
        with open(report_full_name, 'r', encoding='UTF-8') as f:
            report = f.read()

        self.email(receivers, project_name + "自动化测试报告", report)


mail = Mail()
# to = ['zhaoliuming@taoche.com']
# subject = '淘车测试管理平台报警'
# msg = '邮件报警测试'
# mail.email(to, subject, msg)


