import sqlite3

filename = 'ProjectEcho.db'

# class Members:
#     def __init__(self):
#         self._memlist = []
#         try:
#             self.conn = sqlite3.connect(filename)
#         except Error as e:
#             print(e)
#         cursor = self.conn.cursor()
#         try:
#             cursor.execute("SELECT MemNum, LastName, FirstName, Email FROM 'Members'")
#         except:
#             cursor.execute("CREATE TABLE 'Members' ( `MemNum` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, `LastName` "
#                            "TEXT, `FirstName` TEXT, `Email` TEXT )")
#         for row in cursor:
#             self._memlist.append({'memnum': row[0], 'last': row[1], 'first': row[2], 'email': row[3]})
#         cursor.close()
#
#     def __del__(self):
#         self.conn.close()
#
#     def __len__(self):
#         return len(self._memlist)
#
#     def getList(self):
#         return sorted(self._memlist, key=lambda i: i['last'])
#
#     def getMember(self,num):
#         member = {}
#         for member in self._memlist:
#             if member['memnum'] == int(num):
#                 return member
#         return None
#
#     def addMember(self, last, first, email):
#         if last not in [mem['last'] for mem in self._memlist]:
#             self.conn.execute(f"INSERT INTO 'Members' (LastName, FirstName, Email) VALUES ('{last}','{first}','{email}')")
#             self.conn.commit()
#         else:
#             print("Already there")
#         self.__init__()
#
#     def removeMember(self, num):
#         if num in [mem['memnum'] for mem in self._memlist]:
#             self.conn.execute(f"DELETE FROM 'Members' WHERE memnum={int(num)}")
#             self.conn.commit()
#             print('Deleted!')
#         else:
#             print('Not there')
#         self.__init__()
#
#     def editMember(self, num):
#         pass


# class Menus:
#     def __init__(self):
#         self._menulist = []
#         try:
#             self.conn = sqlite3.connect(filename)
#         except Error as e:
#             print(e)
#         cursor = self.conn.cursor()
#         try:
#             cursor.execute("SELECT MenuNum, Theme, MainDish, Starch, Vegetable, Additional, Salad FROM 'Menus'")
#         except:
#             cursor.execute("CREATE TABLE 'Menus' ( `MenuNum` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, `Theme` "
#                            "TEXT, `MainDish` TEXT, `Starch` TEXT, 'Vegetable' TEXT, 'Additional' TEXT, 'Salad' TEXT)")
#         for row in cursor:
#             self._menulist.append({'menunum': row[0], 'theme': row[1], 'main': row[2], 'starch': row[3], 'vegetable':
#                                   row[4], 'additional': row[5], 'salad': row[6]})
#         cursor.close()
#
#     def __del__(self):
#         self.conn.close()
#
#     def getList(self):
#         return sorted(self._menulist, key=lambda i: i['menunum'])
#
#     def getMenu(self, num):
#         menu = {}
#         for menu in self._menulist:
#             if menu['menunum'] == int(num):
#                 return menu
#         return None
#
#     def addMenu(self, theme, main, starch, vegetable, additional, salad):
#         if theme not in [menu['theme'] for menu in self._menulist]:
#             self.conn.execute(f"INSERT INTO 'Menus' (Theme, MainDish, Starch, Vegetable, Additional, Salad) "
#                               f"VALUES ('{theme}','{main}','{starch}','{vegetable}','{additional}','{salad}')")
#             self.conn.commit()
#         else:
#             print("Already there")
#         self.__init__()
#
#     def removeMenu(self, num):
#         if num in [menu['menunum'] for menu in self._menulist]:
#             self.conn.execute(f"DELETE FROM 'Menus' WHERE menunum={int(num)}")
#             self.conn.commit()
#             print('Deleted!')
#         else:
#             print('Not there')
#         self.__init__()
#
#     def editMenu(self, num):
#         pass

class Table:
    def __init__(self):
        pass


class Database:
    def __init__(self, database_file=filename):
        self.database_file = database_file
        self.connection = sqlite3.connect(self.database_file)
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        print(f"List of Tables:\n")
        print(cursor.fetchall())
    
    def __del__(self):
        if self.connection:
            print("Database connection closed!")
            self.connection.close()
    
    def get_all_data(self):
        result = self.connection.execute("SELECT * FROM students")
        return result
    
    def insert(self, name, course, mobile):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, mobile))
        self.connection.commit()
        cursor.close()
    
    def update(self, student_id, name, course, mobile):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE students SET name= ?, course = ?, mobile = ? WHERE id = ?",
                       (name, course, mobile, student_id))
        self.connection.commit()
        cursor.close()
    
    def delete(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE from students WHERE id = ?", (student_id,))
        self.connection.commit()
        cursor.close()
    
    def search(self, name):
        cursor = self.connection.cursor()
        result = list(cursor.execute("SELECT * FROM students WHERE name = ?", (name,)))
        cursor.close()
        return result