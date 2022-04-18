#psycopg......
print("Database task")
import psycopg2
con = psycopg2.connect(
        dbname='postgres', 
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
)
print("CONNECTION ESTABLISHED")
cur=con.cursor()
####Create############
query='''create table emp (emp_name varchar(20),empid varchar(10),emp_age varchar(20))'''
query1='''select * from emp '''
cur.execute(query)
cur.execute(query1)
query2=''' insert into emp values ('Deepak',101,23)'''
query3=''' insert into emp values ('Divya',102,24)'''
query4=''' insert into emp values ('aastha',103,25)'''
query5=''' insert into emp values ('jyoti',104,26)'''
cur.execute(query2)
cur.execute(query3)
cur.execute(query4)
cur.execute(query5)
query6='''select * from emp'''
cur.execute(query6)
list=[('hina',302,45),('esha',509,34)]
query23=''' insert into emp values (%s, %s ,%s)'''
cur.executemany(query23,list)
data=[('ishmat',508,98),('shubhm',56,78)]
cur.executemany(query23,data)
cur.execute('''select * from emp''')
row=cur.fetchall()
print(row)
##update
print("----------update-----------")
query24='''update emp set emp_age=100 where emp_name='shubham' '''
cur.execute(query24)
#row=cur.fetchall()
#print(row)
######read
print("-----------------read----------")
queryy='''select emp_name from emp'''
cur.execute(queryy)
print(cur.fetchall())
#####delete
print('------------delete---------')
querydel='''delete from emp where emp_name='hina' '''
cur.execute(querydel)
cur.execute(query6)
print(cur.fetchall())
####distinct
print("-----distinct------")
querydis='''select distinct emp_name from emp '''
cur.execute(querydis)
print(cur.fetchall())
###order by
print("-----order by-------")
queryordr='''select  emp_name from emp order by emp_name'''
cur.execute(queryordr)
print(cur.fetchall())
#####like
print("-----like-------")
querylike='''select * from emp where emp_name like 'a%' '''
cur.execute(querylike)
print(cur.fetchall())
con.commit()
con.close()
