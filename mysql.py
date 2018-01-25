#python code goes here
#python version :3 
import mysql.connector
cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='check')
cursor=cnx.cursor()
query="select * from userdata"
cursor.execute(query)
print(cursor.fetchall())
query1="INSERT INTO `userdata` (`id`, `name`, `email`, `password`) VALUES ('4', 'ddd', 'ddd123@gmail.com', 'ddd123');"
cursor.execute(query1)
print(cursor.fetchall())

#output
#[(1, u'aaa', u'aaa123@gmail.com', u'aaa123'), (2, u'bbb', u'bbb123@gmail.com', u'bbb123'), (3, u'ccc', u'ccc123@gmail.com', u'ccc123')]
#[(1, u'aaa', u'aaa123@gmail.com', u'aaa123'), (2, u'bbb', u'bbb123@gmail.com', u'bbb123'), (3, u'ccc', u'ccc123@gmail.com', u'ccc123'), (4, u'ddd', u'ddd123@gmail.com', u'ddd123')]
