import pymysql
from common.handle_conf import conf


class HandleMysql():
    def __init__(self):
        self.con = pymysql.connect(host=conf.get('mysql', 'host'),
                                   user=conf.get('mysql', 'user'),
                                   port=int(conf.get('mysql', 'port')),
                                   password=conf.get('mysql', 'password'),
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor
                                   )

    def search_one(self, sql):
        with self.con.cursor() as cur:
            # 执行sql
            cur.execute(sql)
            self.con.commit()
            # 获取sql结果
            res = cur.fetchone()
            cur.close()
            return res

    def search_all(self, sql):
        with self.con.cursor() as cur:
            # 执行ｓｑｌ
            cur.execute(sql)
            self.con.commit()
            # 获取sql结果
            res = cur.fetchall()
            cur.close()
            return res

    def search_count(self, sql):
        with self.con.cursor() as cur:
            res = cur.execute(sql)
            self.con.commit()
            cur.close()
            return res

    def __del__(self):
        # 关闭连接，这个魔术方法会在python程序自动销毁对象时候调用这个方法
        print('对象销毁时自动执行')
        self.con.close()

if __name__ =='__main__':
    sql ='SELECT * FROM futureloan.loan WHERE member_id =72534 and title ="雨夜中波纹疾走"'
    db = HandleMysql()
    res =db.search_one(sql)
    print(res)