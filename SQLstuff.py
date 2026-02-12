import mysql.connector
import TestFunctions

ask = TestFunctions.RequestFromChEMBL()

print(ask.nameToSMILES("Aspirin"))



connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="practiceDB"
)

cursor = connection.cursor()

