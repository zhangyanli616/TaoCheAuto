import pymysql
from service.config import DB_INFO
from pymysql import converters
converions = converters.conversions
converions[pymysql.FIELD_TYPE.BIT] = lambda x:'0' if '\x00' else '1'


class DBConnetion:
    def __init__(self):
        self.db_host = DB_INFO["DB_HOST"]
        self.db_port = DB_INFO["DB_PORT"]
        self.db_database = DB_INFO["DB_DATABASE"]
        self.db_user = DB_INFO["DB_USER"]
        self.db_password = DB_INFO["DB_PASSWORD"]

        self.db = pymysql.connect(host=self.db_host,
                                  port=self.db_port,
                                  database=self.db_database,
                                  user=self.db_user,
                                  password=self.db_password,
                                  charset='utf8',
                                  conv=converions)
        self.cursor = self.db.cursor()

    def create(self, sql):
        """
        创建数据库表
        :param sql: 执行sql
        :return:
        """
        self.cursor.execute(sql)

    def query(self, sql, size: int = 0):
        """
        查询数据库
        :param sql: 执行sql
        :param size: 需要返回的数据行数，0：所有，1:首行，其他数字：指定行数
        :return:返回查询结果
        """
        self.cursor.execute(sql)

        if size == 0:
            results = self.cursor.fetchall()
        elif size == 1:
            results = self.cursor.fetchone()
        else:
            results = self.cursor.fetchmany(size)

        return results

    def alter(self, sql):
        """
        数据库修改操作，如insert、update、delete；
        :param sql: 执行sql
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            raise sql


    def close(self):
        """
        关闭数据库链接
        :return:
        """
        self.db.close()

