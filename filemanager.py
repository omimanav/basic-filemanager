#!/usr/bin/python3
import os, sys, readline, time

print("4ch-fm")
curDir = os.listdir(os.curdir)
curPath = os.curdir

while True:
	#TO DO
	#make dictionary with numbered keys for opening file
	
	def complete(curDir, state):
	    for item in curDir:
	        if item.startswith(text):
	            if not state:
	                return item
	            else:
	                state -= 1

	readline.parse_and_bind("tab: complete")
	readline.set_completer(complete)
	
	sys.stdout.write("\n[L] - list current directory:[L or list]\n[O] - open a file:[O or open] name of file in current directory\n[N] - make new file in current directory:[N or new] name of file incl. extension\n[C] - change directory:[C or change] path/to/go/to\n[X] - delete file:[X or delete] name of file in current directory\n[E] - exit:[E or exit]\n\n")
	
	arg = input("Type here: ")
	cmd = arg.split(' ')[0]
	
	if cmd in 'Ee' or cmd == 'exit':
		break
		
	elif cmd in 'Ll' or cmd == 'list':
		try:
			for file in curDir:
				print('file\t- ' if os.path.isfile(os.curdir + '/' + file) else 'folder\t- ', file)
		except:
			print("Empty directory.")
	elif cmd in 'Cc' or cmd == 'change':
		try:
			destPath = arg.split(' ')[1]
			curDir = os.listdir(os.chdir(destPath))
			curPath = os.curdir
			print('Current working directory is: ' + destPath)
		except:
			print('Something went wrong.\nEnter a valid path.\n\n')
	
	elif cmd in 'Xx' or cmd == "delete":
		try:
			path = arg.split(' ')[1]
			os.remove(path) if os.path.isfile(path) else os.rmdir(path)
		except:
			print('Something went wrong.\nEnter a valid path.\n')
	elif cmd in 'Oo' or cmd == 'open':
		try:
			sys.stdout.write('opening.')
			time.sleep(0.1)
			sys.stdout.write('.')
			time.sleep(0.3)
			sys.stdout.write('.\n')
			os.system('open ' + curPath + '/' + arg.split(' ')[1])
		except Exception as e:
			print('Invalid entry, please enter a filename that exists in current directory.\nEnter "L" to see list of file in current directory.')
	elif cmd in 'Nn' or cmd == 'new':
		try:
			print('trying to make new file...')
			newFile = open(arg.split(' ')[1], 'w')
			print('file made at ' + curPath +'/')
			newFile.close()
		except:
			print("File was not made.\nMake sure you have permission.")
		
	