import sqlite3

filename = 'ProjectEcho.db'

class Members:
    def __init__(self):
        self.memlist = []
        try:
            self.conn = sqlite3.connect(filename)
        except Error as e:
            print(e)
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT MemNum, LastName, FirstName, Email FROM 'Members'")
        except:
            cursor.execute("CREATE TABLE 'Members' ( `MemNum` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, `LastName` "
                           "TEXT, `FirstName` TEXT, `Email` TEXT )")
        for row in cursor:
            self.memlist.append({'memnum': row[0], 'last': row[1], 'first': row[2], 'email': row[3]})
        cursor.close()

    def __del__(self):
        self.conn.close()

    def getList(self):
        return sorted(self.memlist, key=lambda i: i['last'])

    def getMember(self,num):
        member = {}
        for member in self.memlist:
            if member['memnum'] == int(num):
                return member
        return None

    def addMember(self, last, first, email):
        if last not in [mem['last'] for mem in self.memlist]:
            self.conn.execute(f"INSERT INTO 'Members' (LastName, FirstName, Email) VALUES ('{last}','{first}','{email}')")
            self.conn.commit()
        else:
            print("Already there")
        self.__init__()

    def removeMember(self, num):
        if num in [mem['memnum'] for mem in self.memlist]:
            self.conn.execute(f"DELETE FROM 'Members' WHERE memnum={int(num)}")
            self.conn.commit()
            print('Deleted!')
        else:
            print('Not there')
        self.__init__()

    def editMember(self, num):
        pass


class Menus:
    def __init__(self):
        self.menulist = []
        try:
            self.conn = sqlite3.connect(filename)
        except Error as e:
            print(e)
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT MenuNum, Theme, MainDish, Starch, Vegetable, Additional, Salad FROM 'Menus'")
        except:
            cursor.execute("CREATE TABLE 'Menus' ( `MenuNum` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, `Theme` "
                           "TEXT, `MainDish` TEXT, `Starch` TEXT, 'Vegetable' TEXT, 'Additional' TEXT, 'Salad' TEXT)")
        for row in cursor:
            self.menulist.append({'menunum': row[0], 'theme': row[1], 'main': row[2], 'starch': row[3], 'vegetable':
                                  row[4], 'additional': row[5], 'salad': row[6]})
        cursor.close()

    def __del__(self):
        self.conn.close()

    def getList(self):
        return sorted(self.menulist, key=lambda i: i['menunum'])

    def getMenu(self, num):
        menu = {}
        for menu in self.menulist:
            if menu['menunum'] == int(num):
                return menu
        return None

    def addMenu(self, theme, main, starch, vegetable, additional, salad):
        if theme not in [menu['theme'] for menu in self.menulist]:
            self.conn.execute(f"INSERT INTO 'Menus' (Theme, MainDish, Starch, Vegetable, Additional, Salad) "
                              f"VALUES ('{theme}','{main}','{starch}','{vegetable}','{additional}','{salad}')")
            self.conn.commit()
        else:
            print("Already there")
        self.__init__()

    def removeMenu(self, num):
        if num in [menu['menunum'] for menu in self.menulist]:
            self.conn.execute(f"DELETE FROM 'Menus' WHERE menunum={int(num)}")
            self.conn.commit()
            print('Deleted!')
        else:
            print('Not there')
        self.__init__()

    def editMenu(self, num):
        pass
