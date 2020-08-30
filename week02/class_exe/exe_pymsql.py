import pymysql

dbinfo = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "db": "test"
}

sqls = ["show databases"]

result = []

class DbManager():
    def __init__(self, dbinfo, sqls):
        self.host = dbinfo['host']
        self.port = dbinfo['port']
        self.user = dbinfo['user']
        self.password = dbinfo['password']
        self.db = dbinfo['db']
        self.sqls = sqls

    
    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db,
            charset = "utd8mb4"
        )

        cur = conn.cursor()

        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())

            cur.close()
            conn.commit()
        except:
            conn.rollback()
        
        conn.close()

if __name__ == "__main__":
    db = DbManager(dbinfo, sqls)
    db.run()
    print(result)