import os

#Path to the files to be renamed. Eg. path = r"C:\xxx\yyy\prank"
path = " "
#The file prank.zip contains example files which are be to be renamed to reveal a hidden message.

def rename_files(path):
	#(1)get file names from a folder
	file_list = os.listdir(path)
	

	saved_path = os.getcwd()
	os.chdir(path)


	#(2)foreach file, rename file
	for file_name in file_list:
		print("Old Name: "+file_name)
		print("New Name: "+file_name.lstrip("1234567890"))
		os.rename(file_name,file_name.lstrip("1234567890"))
	os.chdir(saved_path)

rename_files(path)
