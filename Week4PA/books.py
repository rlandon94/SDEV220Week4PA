import sqlalchemy as sa
import sqlite3

database = sqlite3.connect('books.db')
cursor = database.cursor()

table = '''DROP TABLE IF EXISTS books'''
cursor.execute(table)

table = '''CREATE TABLE books(title VARCHAR(255), author VARCHAR(255), year INT)'''
cursor.execute(table)

cursor.execute('''INSERT INTO books VALUES('The Weirdstone of Brisingamen','Alan Garner',1960)''')
cursor.execute('''INSERT INTO books VALUES('Perdido Street Station','China Miéville',2000)''')
cursor.execute('''INSERT INTO books VALUES('Thud!','Terry Pratchett',2005)''')
cursor.execute('''INSERT INTO books VALUES('The Spellman Files','Lisa Lutz',2007)''')
cursor.execute('''INSERT INTO books VALUES('Small Gods','Terry Pratchett',1992)''')

database.commit()
database.close()

engine = sa.create_engine('sqlite:///books.db')
connection = engine.connect()
metadata = sa.MetaData()
table_to_query = sa.Table('books', metadata, autoload_with=engine)

query = sa.select(table_to_query.c.author).order_by(table_to_query.c.author)
resultA = connection.execute(query)
resultB = resultA.fetchall()

print(resultB)