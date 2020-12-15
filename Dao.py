import json

import pymysql
import datetime


class Dao(object):
    def __init__(self):
        self.db = pymysql.connect(host='neuznyx.cn', port=3306, user='root', passwd='1023464930', db='drugbox2',
                                  charset='utf8')

    def get_drug_info(self, boxid):
        cursor = self.db.cursor()
        sql = "select * from drug,druginfo where drug.drugid=druginfo.drugid and boxid='%s'" % (boxid)
        cursor.execute(sql)
        result = cursor.fetchall()
        fields = cursor.description
        cursor.close()
        column_list = []
        for i in fields:
            column_list.append(i[0])
        data = "["
        for row in result:
            min_data = {}
            for i in range(len(column_list)):
                min_data[column_list[i]] = row[i]
            data = data + json.dumps(min_data, default=str, ensure_ascii=False) + ','
        data = data.strip(",") + "]"
        data = json.loads(data)
        file = open("druginfotest.txt", "w", encoding="utf-8")
        file.write(str(data))
        file.close()
        return data

    def consume_drug(self):  # 服用药品之后，药品剩余量的减少以及计算
        pass

    def add_drug(self, boxid, slotid, druginfo):  # 扫描条形码添加药品
        cursor = self.db.cursor()
        pass


if __name__ == '__main__':
    boxid = "dc-a6-32-a7-cc-a2"
    dao = Dao()
    data = dao.get_drug_info(boxid)
    print(data)
    druginfo = {
        'drugid':'',
        'sourcecode': '',
        'expirytime': '2020-09-17',
        'name':'',
        'producer':'',
        'form':''
    }
    dao.add_drug(boxid,3,druginfo)
