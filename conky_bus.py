from fetch_station import compile_menu
import sys

for line in compile_menu(sys.argv[1]):
	if "Striesen" in line:
		print(line.replace("Striesen Niederwaldpl.", "Home"))
		break