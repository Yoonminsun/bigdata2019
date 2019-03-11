import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')
# 시스템 구축 초기에 table이 없는 경우 table 생성
query = """CREATE TABLE sales
            (customer VARCHAR(20),
             product VARCHAR(40),
             amount FLOAT,
             date DATE);"""
con.execute(query)
con.commit()
# file system 이 아닌 memory에 생성하므로 속도는 빠르나 휘발성이다

# Insert a few rows of data into the table
data = [('Richard Lucas','Notepad',2.50,'2014-01-02'),
        ('Jenny Kim','Binder',4.15,'2014-01-15'),
        ('Svetlana Crow','Printer',155.75,'2014-02-03'),
        ('Stephen Randolph','Computer',679.40,'2014-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement,data)
con.commit()

# Query the sales table
# SELECT * FROM sales -> sales 테이블로부터(FROM) 모든값(*)을 가져옴(SELECT)
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall() # fetchall() 로 SELECT 한 값을 반환

# Count the number of rows in the output
row_counter=0
for row in rows:
    print(row)
    row_counter+=1
print('Number of rows: {}'.format(row_counter))