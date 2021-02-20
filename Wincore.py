# tasks
# 1. fetch data
# 2. Incert data
# 3. Delete data
# 4. Show the path of the dbs
# 5. About section
# 6. MD5 hash decryption

# Version 1.0
# Project-type 		   ===> Open Source
# Development-initiated ==> 3/2/21
# Developer 			=>	Fr34K

# Necessary Variables

#String literels
Id = "id"
web = "website"
mail = "email"
uname = "username"
passwd = "password"

#Color
red='\033[1;31m'
green='\033[1;32m'
blue='\033[1;34m'

# Necessary Modules
import sqlite3
import os
import hashlib 
import time

# Creating Connection object to connect with the database
connection = sqlite3.connect('database.db')

# Creating the Cursor object to execute SQL statements
cursor = connection.cursor()
	
# Creating passBass class for the Lincore Module
class passBase:
	def __init__(self):
		pass
		
	# Data Extraction 
	def extractEntries(self):
		os.system("cls")
		sql = "SELECT * FROM Database"
		cursor.execute(sql)
		connection.commit()
		entries = cursor.fetchall()
		print(green + f'''{Id.upper().ljust(10)} {web.upper().ljust(15)} {uname.upper().ljust(25)} {mail.upper().ljust(35)}  {passwd.upper().ljust(50)}\n''' + blue)
		for i in range(len(entries)):
			itemList = list(entries[i])
			#print(str(itemList[0])+"  "+str(itemList[1])+"  "+str(itemList[2])+"  "+str(itemList[3])+"  "+str(itemList[4]))
			print(f'''{str(itemList[0]).ljust(10)} {str(itemList[1]).ljust(15)} {str(itemList[2]).ljust(25)} {str(itemList[3]).ljust(35)}   {str(itemList[4]).ljust(50)}''' + blue)
			
	# Adding Entries
	def addEntry(self):
		os.system("cls")
		while True:
			site = str(input(blue+"\nWebsite : ")).upper().rstrip('.COM')
			username = str(input(blue+"Username : "))
			email = str(input(blue+"Email : "))
			password = str(input(blue+"Password : "))
			hashed = hashlib.sha512(password.encode()).hexdigest()
			cipherHash = hashed[::-1]

			# Creating a tuple to store the values above
			credtuple = (site,username,email,cipherHash)
			
			# execute method takes two arguments
			cursor.execute("""
			INSERT INTO Database(website,username,email,password) VALUES(?, ?, ?, ?)""",credtuple)
			connection.commit()
			print(green+"\n	[*]"+ blue +" Successfully added all entries\n"+blue)
			
			# Prompting user to continue or going back to menu
			print("Press [a] to add entries or [Enter] to go to menu\n")
			res = str(input(">>> "))
			if res == '':
				break
			elif res == 'a':
				continue
			else:
				print(red+"\nInvalid Input")
				print("Going back to menu"+blue)
				time.sleep(3)
				break 
		# 	Will add password encryption soon :)
	
	# Deleting Entries
	def deleteEntry(self):
		enID = int(input("Enter the ID of the entry to delete : "))
		cursor.execute("""DELETE FROM Database WHERE id=?""",(enID,))
		connection.commit()
		print(green +"[*]"+ blue +" Successfully deleted the entry")
		time.sleep(3)
		# According to sqlite python documentation , execute method takes a tuple of values as arguments
		
	# Deleting all entries
	def killDBS(self):
		cursor.execute("DELETE FROM Database")
		connection.commit()
		print(red+"\nAll Entries have been deleted")
