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


    def getadress(self):  # Выбераем всех тех кому будем отправлять сообщение vgroups.blocked, vgroups.archive
        self.cur = self.con.cursor()
        # self.cur.execute("""SELECT address_street.name, accounts_addr.building, accounts_addr.flat, accounts_addr.address from accounts_addr
        #                     LEFT JOIN address_street ON accounts_addr.street = address_street.record_id
        #                     WHERE 1""")
        self.cur.execute("""SELECT address_building.record_id, address_street.name, address_building.name from address_building
                                    LEFT JOIN address_street ON address_building.street = address_street.record_id
                                    WHERE 1""")

        result = self.cur.fetchall()

        return result


    def getUtmAddress(self):
        self.cur = self.con.cursor()
        self.cur.execute("""SELECT id, street, houses.number from houses WHERE 1""")
        result = self.cur.fetchall()

        return result

    def updatebase(self, key, value, string):
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE houses SET post_code = %i, country='%s' WHERE id=%i" % (int(value), string, int(key)) )
        self.con.commit()



    def close(self): #Закрываем соединение
        self.con.close()


res = Resurse(host="localhost",user= "root",passw= "pUMoLitEDA",db= "telerevizorro")

res.connect()
result = res.getUtmAddress()

res1 = Resurse(host="91.226.152.6",user= "unt",passw= "pUMoLitEDA",db= "billing")

res1.connect()
result1 = res1.getadress()
res1.close()

utm = []
for res3 in result:
    if res3[2]:
        addres = res3[1]+" "+res3[2]
        utm.append({"utmId":res3[0], "utmName":addres})



i=0
for res2 in result1:
        i=i+1
        if res2[1]:
            print i, res2[0], res2[1], res2[2]
            addres = res2[1]+" "+res2[2]
            # print addres
            if res2[1] in u"К.Либкнехта":addres = addres.replace(u"К.Либкнехта", u"К. Либкнехта")
            if res2[1] in u"М.Гречко": addres = addres.replace(u"М.Гречко", u"М. Гречко")
            if res2[1] in u"Д.Бедного": addres = addres.replace(u"Д.Бедного", u"Д. Бедного")
            if res2[1] in u"М.Жукова": addres = addres.replace(u"М.Жукова", u"М. Жукова")
            if res2[1] in u"М.Жукова": addres = addres.replace(u"М.Жукова", u"М. Жукова")
            if res2[1] in u"1-й пер.Дивизионный": addres = addres.replace(u"1-й пер.Дивизионный", u"М. Жукова")

            for utm2 in utm:
                if addres.lower() in utm2['utmName'].lower():
                    utm2.update({"lanID":res2[0], "lanName":addres})


print "***************************************************************************"
for displ in utm:
    # print displ['utmId'], displ['utmName'],displ['utmId'],displ['utmId']
    try:
        print displ['utmId'], displ['utmName'], displ['lanID'], displ['lanName']
        res.updatebase(displ['utmId'], displ['lanID'], displ['lanName'])
    except:
        print None, None
        pass