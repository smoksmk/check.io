#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb


#Выдергииваем нужную инфу
class Resurse():

    def __init__(self,host="localhost",user= "root",passw= "pUMoLitEDA",db= "telerevizorro"):

        self.host = host
        self.user = user
        self.passw = passw
        self.db = db

        self.con = ""
        self.cur = ""

    def connect(self): #Подключение к базе
        self.con = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passw, db=self.db, charset='utf8')


    def getBalanse(self): #Выбераем всех тех кому будем отправлять сообщение vgroups.blocked, vgroups.archive
        self.cur = self.con.cursor()
        self.cur.execute("""SELECT accounts.name,
                        agreements.balance, agreements.number, accounts.descr, tarifs.descr
                        from vgroups

						LEFT JOIN accounts ON accounts.uid=vgroups.uid
						LEFT JOIN agreements ON accounts.uid=agreements.uid
						LEFT JOIN  accounts_addr ON accounts.uid= accounts_addr.uid
						LEFT JOIN  tarifs ON vgroups.tar_id= tarifs.tar_id
						LEFT JOIN  address_flat ON accounts_addr.flat= address_flat.record_id
						WHERE vgroups.archive = 0 AND accounts_addr.type=0 AND vgroups.blocked=0
						ORDER BY accounts.uid""")
        result = self.cur.fetchall()
        self.cur.close()
        return result

    def getadress(self, id):
        self.cur = self.con.cursor()
        self.cur.execute("SELECT id from houses WHERE post_code = %i LIMIT 1"%id)
        result = self.cur.fetchall()
        try:
            return result[0][0]
        except:
            return None

    def close(self): #Закрываем соединение
        self.con.close()


res = Resurse(host="91.226.152.6",user= "unt",passw= "pUMoLitEDA",db= "billing")

res.connect()
result = res.getBalanse()
res.close()

for resurs in result:
   name, balanse, number, deskr, tarif = resurs

   print number+";"+name+";"+str(int(balanse))+";"