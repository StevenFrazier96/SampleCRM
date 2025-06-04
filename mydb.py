import mysql.connector

dB = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'PracticeProjects!2'
	)


cursorObject = dB.cursor()

cursorObject.execute("CREATE DATABASE TrashGoblin")

print('fin')