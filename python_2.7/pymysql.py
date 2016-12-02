import pymysql.cursors
connection=pymysql.connect(host='localhost',
	user='root',
	passwd='123456',
	db='wikiurl',
	charset='utf8mb4')
connection.cursors()
cursors.exectute(sql,(m1,m2))