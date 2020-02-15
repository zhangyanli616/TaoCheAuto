import os
from titan import tt_config
from BeautifulReport import BeautifulReport

report_path = tt_config.REPORT_PATH
os.makedirs(report_path, exist_ok=True)


class Report(BeautifulReport):
    """
    测试报告生成类
    """
    def __init__(self, suite, name, report_time):
        """
        测试报告生成初始化
        :param suite: 准备执行生成报告的测试套件
        :param name: 测试报告的名称
        """
        self.suite = suite
        self.name = name
        self.time = report_time

    def build(self):
        """
        生成测试报告
        :return: 
        """
        self.filename = self.name + '_' + self.time
        self.runner = BeautifulReport(self.suite)
        self.runner.report(filename=self.filename, report_dir=report_path, description=self.name)

    def report_result(self):
        self.build()
        return self.runner





