from titan import Report
from titan import WeChat
from titan import tt_config
from .database_service import DBConnetion
import time
import re

report_dir = tt_config.REPORT_PATH


class AutoTest:
    def __init__(self, suite, name, to_user, case_type):
        self.suite = suite
        self.name = name
        self.to_user = to_user
        self.case_type = case_type

    def run(self):
        # 记录测试执行时间
        time_base = time.localtime(time.time())
        # 数据库时间
        testTime = time.strftime('%Y-%m-%d %H:%M:%S', time_base)
        # 测试报告html时间命名
        report_date = time.strftime('%Y-%m-%d', time_base)
        report_time = time.strftime('%Y-%m-%d_%H-%M-%S', time_base)
        # 测试集执行批次号
        setId = time.strftime('%Y%m%d%H%M%S', time_base)

        # 生成报告，并返回报告对象
        runner = Report(self.suite, self.name, report_time)
        result_obj = runner.report_result()

        # 获取报告对象中的测试集执行结果
        result_set = result_obj.fields

        # 连接数据库
        conn = DBConnetion()

        # 存储测试集执行结果
        result_set_sql = "INSERT INTO ui_autotest_set_record(testName, testAll, testPass, testFail, testError, testSkip, " \
                         "totalTime, testTime, setId, reportHtml) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', " \
                         "'%s', '%s', '%s')"

        testName = result_set['testName']
        testAll = result_set['testAll']
        testPass = result_set['testPass']
        testFail = result_set['testFail']
        testError = result_set['testError']
        testSkip = result_set['testSkip']
        totalTime = result_set['totalTime'].replace('s', '')
        reportHtml = report_date + '\\\\' + self.name + '_' + report_time + '.html'

        conn.alter(result_set_sql % (testName, testAll, testPass, testFail, testError,
                                     testSkip, totalTime, testTime, setId, reportHtml))

        # 获取case执行的详细结果
        result_cases = result_set['testResult']
        # 存储case执行结果
        result_case_sql = "INSERT INTO ui_autotest_case_record(setId, className, caseName,caseType, description, spendTime, caseStatus, " \
                          "caseLog, author, testTime,caseScreenShot) " \
                          "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        case_status = {"成功": 1, "失败": 2, "跳过": 3}
        for result_case in result_cases:
            className = result_case['className']
            caseName = result_case['methodName']
            # 存在描述时去掉头尾空格，不存在时默认没有描述
            description = '没有描述' if not result_case['description'] else result_case['description'].strip()
            author = re.search(r'@author:(.*)', description, flags=re.I)
            if author:
                description = description.replace(author.group(), '')
                author = author.group().replace('@author:', '')
                if not author:
                    author = None

            spendTime = float(result_case['spendTime'].split(' ')[0])
            caseStatus_key = result_case['status']
            caseStatus = case_status[caseStatus_key]
            caseLog = ';'.join(result_case['log']).replace("'", '"')
            # 匹配caseLog中的截图相对路径
            casePNG = re.search(report_date + r'\\testScreen\\(.*?).png', caseLog)
            caseScreenShot = casePNG if not casePNG else casePNG.group().replace("\\", "\\\\")

            conn.alter(
                result_case_sql % (
                setId, className, caseName, self.case_type, description, spendTime, caseStatus, caseLog, author,
                testTime, caseScreenShot))

        # 关闭数据库链接
        conn.close()

        wechat_msg_template = "{testTime} 自动化测试报告概要：\n" \
                              "【集合名称】{testName}\n" \
                              "【用例总数】{testAll}\n" \
                              "【用例通过】{testPass}\n" \
                              "【用例失败】{testFail}\n" \
                              "【用例跳过】{testSkip}\n" \
                              "【运行时间】{totalTime}s\n" \
                              "【报告路径】{reportHtml}"

        result_map = {"testTime": testTime,
                      "testName": testName,
                      "testAll": testAll,
                      "testPass": testPass,
                      "testFail": testFail,
                      "testSkip": testSkip,
                      "totalTime": totalTime,
                      "reportHtml": reportHtml.replace('\\\\', '\\')}
        wechat_msg = wechat_msg_template.format_map(result_map)

        #WeChat.send_message(self.to_user, wechat_msg)
