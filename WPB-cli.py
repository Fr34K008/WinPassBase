# -*- coding: utf-8 -*-

# Necessary Modules
import os
import sys
import time
import Wincore

#Color
red='\033[1;31m'
green='\033[1;32m'
blue='\033[1;34m'

#Icons
success = blue + "[" + green + "*" + blue + "]"
error = blue + "[" + red + "!" + blue + "]"
info = blue + "[" + green + "?" + blue + "]"

#Banner
banner = blue +	"""  
""" +green+ """			 __      __.__      __________                      __________                                       .__  .__ 
"""+red+"""			/  \    /  \__| ____\______   \_____    ______ _____\______   \_____    ______ ____             ____ |  | |__|
"""+blue+"""			\   \/\/   /  |/    \|     ___/\__  \  /  ___//  ___/|    |  _/\__  \  /  ___// __ \   ______ _/ ___\|  | |  |
"""+red+"""			 \        /|  |   |  \    |     / __ \_\___ \ \___ \ |    |   \ / __ \_\___ \\\  ___/  /_____/ \  \___|  |_|  |
"""+green+"""			  \__/\  / |__|___|  /____|    (____  /____  >____  >|______  /(____  /____  >\___  >          \___  >____/__|
"""+blue+"""			       \/          \/               \/     \/     \/        \/      \/     \/     \/               \/         
"""

#Options
List = blue + "1. " + green + "List Credentials"
Add = blue + "2. " + green + "Add Credentials"
Erase = blue + "3. " + green + "Erase Credentials"
Flush = blue + "4. " + red + "Flush All" + green
Exit = blue + "5. " + green + "Exit"


# PassBase Object
db_do = Wincore.passBase()

def wpb():
	os.system("cls")
	print(banner)
	print(green +
	f"""
	-------------------------------------------------
	| {List}				\|
	| {Add}				\|
	| {Erase}				\|
	| {Flush}					\|
	| {Exit}					\|
	-------------------------------------------------
	""")
	
	try:
		action = int(input(blue + "option: "))
		if action == 1:
			os.system("cls")
			print(banner+"\n\n")
			db_do.extractEntries()
			input(blue + "Press Enter to continue")
			wpb()
		elif action == 2:
			os.system("cls")
			print(banner+"\n\n")
			db_do.addEntry()
			input(blue + "Press Enter to continue")
			wpb()
		elif action == 3:
			while True:
				os.system("cls")
				print(banner+"\n\n")
				db_do.extractEntries()
				db_do.deleteEntry()
				print(blue+"Commands:")
				print(info+blue+"DELETE")
				print(info+blue+"MENU")
				res = str(input(">>> ")).upper()
				if res == 'DELETE':
					continue
				elif res == 'MENU':
					break
				else:
					print("\n"+error +red+"Invalid Input")
					break
			input(blue+"Press Enter to continue")
			wpb()

		elif action == 4:
			print(info + blue + "Warning : THIS OPERATION WILL DELETE ALL ENTRIES IN THE DATABASE !!")
			res = str(input(info+"Do You Want to Proceed [y/n] ? \n>>> ")).upper()
			if res == 'Y':
				db_do.killDBS()
				input(blue+"Press Enter to continue")
				wpb()
			elif res == 'N': 
				wpb()
			else:
				print("\n"+error+red+"Invalid Input")
				input(blue+"Press Enter to continue")
				wpb()
		elif action == 5:
			os.system("cls")
			print(green+"Thank you for using WinPassBase :)\n")
			sys.exit()
	except ValueError:
		print("\n"+error + red + "Invalid Input")
		input(blue + "Press Enter to continue")
		wpb()
	except KeyboardInterrupt:
		print("\n\n"+error+green+"Keyboard Interrupt")
		print("Shuting Down")
		time.sleep(3)
		os.system("cls")
		print(green+"Thank you for using WinPassBase :)\n")
		sys.exit()
	
if __name__ == "__main__":
	wpb()
