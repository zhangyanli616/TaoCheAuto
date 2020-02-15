import time
import os
# 基础目录
#BASE_PATH = 'D:\\WorkSpace'
BASE_PATH = '/Users/taoche/Desktop/mc-log'

# 报告生成目录
current_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
REPORT_PATH = os.path.join(BASE_PATH, 'tt_test_result', current_date)

# 通知邮件
EMAIL_NAME = 'auto_test'
EMAIL_PASSWORD = 'abcd.1234'

# 企业微信
CORPID = "wwa5bfb8f102dad85f"  # 企业id
SECRET = "P35R_QY6_cS-ey7Fk89iWFtCjxKogEs5heYs-21I_2U"  # Secret
AGENTID = 1000040  # Agentid