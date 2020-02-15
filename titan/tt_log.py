"""日志相关"""

import logbook
import os
# from functools import wraps
from logbook.more import ColorizedStderrHandler
from titan import tt_config

report_path = tt_config.REPORT_PATH
log_dir = os.path.join(report_path, 'testLog')
os.makedirs(log_dir, exist_ok=True)


def get_logger(name='log', level='INFO'):
    logbook.set_datetime_format('local')
    # 输出到控制台
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    # 写入log文件
    # logbook.TimedRotatingFileHandler(
    #     os.path.join(log_dir, '%s.log' % name),
    #     date_format='%Y-%m-%driver-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


LOG = get_logger()


# def logger(param):
#     def wrap(function):
#         @wraps(function)
#         def _wrap(*args, **kwargs):
#             LOG.info("当前模块 {}".format(param))
#             LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
#             return function(*args, **kwargs)
#
#         return _wrap
#
#     return wrap
