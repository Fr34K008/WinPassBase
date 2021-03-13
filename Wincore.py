# -*- coding: utf-8 -*-
# Version 1.1
# Author : [ Fr34K ]

# Necessary Modules
import sqlite3
import os
import hashlib 
import time

# Necessary Variables
#Color
red='\033[1;31m'
green='\033[1;32m'
blue='\033[1;34m'

#Path to dbs
path = "database.db"

#Icons
success = blue + "[" + green + "*" + blue + "]"
error = blue + "[" + red + "!" + blue + "]"
info = blue + "[" + green + "?" + blue + "]"

# Creating Connection object to connect with the database
connection = sqlite3.connect(path)

# Creating the Cursor object to execute SQL statements
cursor = connection.cursor()
	
# Creating passBass class for the Lincore Module
class passBase:
	def __init__(self):
		pass
		
	# Data Extraction 
	def extractEntries(self):
		sql = "SELECT * FROM Database"
		cursor.execute(sql)
		connection.commit()
		entries = cursor.fetchall()
		print(green + f'''{"id".upper().ljust(10)} {"website".upper().ljust(15)} {"username".upper().ljust(25)} {"email".upper().ljust(35)}  {"password".upper().ljust(50)}\n''' + blue)
		for i in range(len(entries)):
			itemList = list(entries[i])
			#print(str(itemList[0])+"  "+str(itemList[1])+"  "+str(itemList[2])+"  "+str(itemList[3])+"  "+str(itemList[4]))
			print(f'''{blue + str(itemList[0]).ljust(10) +green} {str(itemList[1]).ljust(15)} {str(itemList[2]).ljust(25)} {str(itemList[3]).ljust(35)}   {str(itemList[4]).ljust(50)}''' + blue)
			
	# Adding Entries
	def addEntry(self):
		while True:
			print("\n\n"+info + green + "URL can not include "+ blue + "http://" + green + " or " + blue + "https://")
			site = str(input(blue+"\nWebsite's URL : ")).upper().rstrip(".COM")
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
			print(success + green +" Successfully added all entries\n"+blue)
			
			# Prompting user to continue or going back to menu
			print("Commands:")
			print(info+blue+"ADD")
			print(info+blue+"MENU")
			res = str(input(">>> ")).upper()
			if res == 'MENU':
				break
			elif res == 'ADD':
				continue
			else:
				print("\n"+error +red+"Invalid Input")
				break 
		# 	Will add password encryption soon :)
	
	# Deleting Entries
	def deleteEntry(self):
		enID = int(input("Enter the ID of the entry to delete : "))
		cursor.execute("""DELETE FROM Database WHERE id=?""",(enID,))
		connection.commit()
		print(success + green +" Successfully deleted the entry\n")
			
		# According to sqlite python documentation , execute method takes a tuple of values as arguments
		
	# Deleting all entries
	def killDBS(self):
		cursor.execute("DELETE FROM Database")
		connection.commit()
		print(red+"\nAll Entries have been deleted")
