import hashlib #library used 

flag = 0

pass_hash = input("Enter md5 hash: ") #this input will be compared 

wordlist = input("File name: ")

try:
	pass_file = open (passwords, "r")
except:
	print("No file found")
	quit()

for word in pass_file:
	enc_word = word.encode('utf-8')
	digest = hashlib.md5(enc_word.strip()).hexdigest()

	print(word)
	print(digest)
	print(pass_hash)

	if digest == pass_hash:
		print("Password has been found")
		print("The password is " + word)
		flag = 1
		break

if flag == 0:
	print("password is not in the list")