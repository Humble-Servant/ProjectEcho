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
            if member['memnum']==int(num):
                return member
        return None

    # def add(self, name, email):
    #     member = {}
    #     first, last = name.split(' ')
    #     member['first'] = first
    #     member['last'] = last
    #     member['email'] = email
    #     for m in self.memlist:
    #         if

