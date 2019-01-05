#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb, json
from random import sample
from lxml import etree
from random import randint

logins = []

def adress():
    pass

#Транслит фамилии
def transliterate(string):

    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Ё': u'E',
                       u'Ж': u'Zh',
                       u'З': u'Z',
                       u'И': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ц': u'Ts',
                       u'Ч': u'Ch',
                       u'Ш': u'Sh',
                       u'Щ': u'Sch',
                       u'Ъ': u'',
                       u'Ы': u'Y',
                       u'Ь': u'',
                       u'Э': u'E',
                       u'Ю': u'Yu',
                       u'Я': u'Ya',}

    lower_case_letters = {u'а': u'a',
                       u'б': u'b',
                       u'в': u'v',
                       u'г': u'g',
                       u'д': u'd',
                       u'е': u'e',
                       u'ё': u'e',
                       u'ж': u'zh',
                       u'з': u'z',
                       u'и': u'i',
                       u'й': u'y',
                       u'к': u'k',
                       u'л': u'l',
                       u'м': u'm',
                       u'н': u'n',
                       u'о': u'o',
                       u'п': u'p',
                       u'р': u'r',
                       u'с': u's',
                       u'т': u't',
                       u'у': u'u',
                       u'ф': u'f',
                       u'х': u'h',
                       u'ц': u'ts',
                       u'ч': u'ch',
                       u'ш': u'sh',
                       u'щ': u'sch',
                       u'ъ': u'',
                       u'ы': u'y',
                       u'ь': u'',
                       u'э': u'e',
                       u'ю': u'yu',
                       u'я': u'ya',}

    translit_string = ""

    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index+1:
                if string[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    return translit_string

#Генератор паролей
def generate(count=1, length=8):
    #'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
    chars = (
        'abcdefghijklmnopqrstuvwxyz' + \
        '01234567890'
        )
    """
     Generate password
    Kwargs:
        count (int)::
            How many passwords should be returned?
        length (int)::
            How many characters should the password contain
        allowed_chars (str)::
            Characters
    Returns:
        String with the password. If count > 1 then the return value will be auto_now=
        list of strings.
    """
    if count == 1:
        return ''.join(sample(chars, length))

    passwords = []
    while count > 0:
        passwords.append(''.join(sample(chars, length)))
        count -= 1

    return passwords

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


    def getUsers(self): #Выбераем всех тех кому будем отправлять сообщение vgroups.blocked, vgroups.archive
        self.cur = self.con.cursor()
        self.cur.execute("""SELECT accounts.name, accounts_addr.address, accounts.mobile,
                        agreements.balance, agreements.number, accounts.descr, tarifs.descr,
                        accounts.pass_sernum, accounts.pass_no, accounts.pass_issuedep, accounts.pass_issuedate,
                        vgroups.tar_id, accounts_addr.building, address_flat.name
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

def checklogin(login):
    if login in logins:
        return True

def getLogin(name, uid):
    fomil = name.split()
    login = u"tv-"+transliterate(fomil[0].lower())
    tire = u""
    while checklogin(login):
        print u"Дубляж "+name+" "+uid+" "+login
        i=randint(1,2)
        if randint(0,1):dash = u"-"
        try:
            login = login+dash+transliterate(fomil[i][0].lower())
        except:
            login = login + tire + u"1"
        dash = ""
    logins.append(login)
    return login

if __name__ == "__main__":
    conn = Resurse(host="91.226.152.6",user= "unt",passw= "pUMoLitEDA",db= "billing")
    conn.connect()
    res = conn.getUsers()
    conn.close()

    base = Resurse()
    base.connect()

    # Создание корневого элемента html
    page = etree.Element('import')
    # Добавление двух дочерних элементов - <head> и <body>
    usersElt = etree.SubElement(page, 'users')

    i = 0
    y = 0
    missadress = []
    print "login    - ФИО   - Адресс    - паспорт   - тел   - баланс    - uid"
    for res1 in res:
        i = 1+i
        name, adress, mobile, balanse, uid, descr,  tarif, pass_ser, pass_no, pass_dep, pass_date, tar_id, building, flat = res1

        fomil = name.split()

        adress = adress.replace(u'Россия,край Краснодарский,', "")
        adress = adress.replace(u',г Крымск,,', "")
        adress = adress.replace(u',,,', "")
        adress = adress.replace(u',', " ")
        adress = adress.replace(u' дом', u",")
        adress = adress.replace(u' кв', u",")
        mobile = mobile.replace(u'-', "")
        pashport = pass_ser+u" "+str(pass_no)+u" "+pass_dep+u" "+str(pass_date)
        if tar_id == 3: tar = "800"
        else: tar="900"

        if u'ФИО' not in fomil[0]:
            login = getLogin(name, uid)

            oldadress = base.getadress(building)


            if not oldadress:
                y=y+1
                missadress.append({'addres':adress, "builID":building, "old":oldadress})


            print str(i)+")", login ,"###", name,"####", adress,"####", pashport,"####", mobile,"####", int(balanse),"####", uid,"####", descr,"####" , tarif,"####" , oldadress,"####" , flat,"####" , building

            userElt = etree.SubElement(usersElt, 'user')
            # Пример: добавление элемента <title>Your page title here</title>
            etree.SubElement(userElt, 'login').text = login
            etree.SubElement(userElt, 'pass').text = generate()
            etree.SubElement(userElt, 'full_name').text = name
            etree.SubElement(userElt, 'act_address').text = adress
            etree.SubElement(userElt, 'passport').text = pashport
            etree.SubElement(userElt, 'mob_tel').text = str(mobile)
            etree.SubElement(userElt, 'comments').text = str(uid)+" "+descr+" "+tarif
            if oldadress:
                # print oldadress
                etree.SubElement(userElt, 'house_id').text = str(oldadress)
                etree.SubElement(userElt, 'flat_number').text = flat

            #Группы
            groups = etree.SubElement(userElt, 'groups')
            group = etree.SubElement(groups, 'group')
            etree.SubElement(group, 'group_id').text = tar
            #баланс и блокировка
            accounts = etree.SubElement(userElt, 'accounts')
            account = etree.SubElement(accounts, 'account')
            etree.SubElement(account, 'is_blocked').text = "0"
            etree.SubElement(account, 'balance').text = str(int(balanse))


    for z in missadress:
        print z['addres'], z['builID']

    print y

    # Создание и сохранение документа
    doc = etree.ElementTree(page)
    outFile = open('homemade.xml', 'w')
    doc.write(outFile)


