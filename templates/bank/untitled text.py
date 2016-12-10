	cnx = MySQLdb.connect(user='root', passwd='mysql',
                              host='127.0.0.1', port=3306,
                              db='bankSystem')
	cursor = cnx.cursor()


	addUser = ("INSERT INTO user "
               "(userId, firstName, lastName, balance) "
               "VALUES (%s, %s, %s, %s)")

	dataUser = (22, 'fafnland', 'fdsfsd', 5000)

# Insert new employee
	cursor.execute(addUser, dataUser)
	cnx.commit()

	cursor.close()
	cnx.close()

#	account1 = User.objects.get(pk=1);