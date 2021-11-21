import pymysql


class Connection:

    conn = None

    def open(self):
        self.conn = pymysql.connect(host='3.130.126.210',
                                            port=3309,
                                            user='pruebas',
                                            password='VGbt3Day5R',
                                            db='habi_db')

    def close(self):
        if self.conn:
            self.conn.close()

    def commit(self):
        if self.conn:
            self.conn.commit()
        
    def query(self, sql, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            columns = cursor.description 
            result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
            return result
