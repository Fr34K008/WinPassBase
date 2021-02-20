import Wincore
import os
import sys
import time

# Creating passbase object
dbs = Wincore.passBase()

# Var
banner = """

 __      __.__      __________                      __________                                       .__  .__ 
/  \    /  \__| ____\______   \_____    ______ _____\______   \_____    ______ ____             ____ |  | |__|
\   \/\/   /  |/    \|     ___/\__  \  /  ___//  ___/|    |  _/\__  \  /  ___// __ \   ______ _/ ___\|  | |  |
 \        /|  |   |  \    |     / __ \_\___ \ \___ \ |    |   \ / __ \_\___ \\\  ___/  /_____/ \  \___|  |_|  |
  \__/\  / |__|___|  /____|    (____  /____  >____  >|______  /(____  /____  >\___  >          \___  >____/__|
       \/          \/               \/     \/     \/        \/      \/     \/     \/               \/         
 """

#Color
red='\033[1;31m'
green='\033[1;32m'
blue='\033[1;34m'


# Menu
while True:
	try:
		os.system("cls")
		print(green + banner + blue)
		print("\n" + """
		[1] List all entries
		[2] Add new entries
		[3] Delete entries
		[4] Reset 
		[0] Exit
		""")

		opt = int(input("wpb> "))

		if opt == 1:
			dbs.extractEntries()
			res = str(input("\nPress [Enter] to continue"))
			if res == '':
				continue
			else:
				continue

		elif opt == 2:
			dbs.addEntry()

		elif opt == 3:
			confirmation = str(input(red +"Are you sure about deleting entries [y/n] ?\n>>> "+blue)).upper()
			if confirmation == 'Y':
				dbs.extractEntries()
				print("\n")
				dbs.deleteEntry()
			else:
				res = str(input("\nPress [Enter] to continue"))
				if res == '':
					continue
				else:
					continue

		elif opt == 4:
			print("[" + red + "*" + blue +"]" + blue + "Warning : [ THIS OPERATION WILL DELETE ALL ENTRIES IN THE DATABASE !!]")
			res = str(input("Do You Want to Proceed [y/n] ? \n>>> ")).upper()
			if res == 'Y':
				dbs.killDBS()
				time.sleep(5)
			elif res == 'N': 
				continue

		elif opt == 0:
			os.system("cls")
			print(green + "Thank you for using WinPassBase :)\n")
			sys.exit()

	except Exception:
		print(red + "\nInvalid Input")
		res = str(input("Press [Enter] to continue"))
		if res == '':
			continue
		else:
			continue
