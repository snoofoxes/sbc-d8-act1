#Login / Registration
l = []
p = []
def register():
	clears()
	lines = [line.strip() for line in open("username.txt")]
	for line in lines:
		l.append(line)
	user = input("Enter a username: ")
	if user not in l:
		usr = open("username.txt","a")
		print(user,file=usr)
		usr.close()
	else:
		print("Username is already exist!")
		register()
	pass_ = input("Enter a password: ")	
	pwd = open("password.txt", "a")
	print(pass_,file=pwd)
	pwd.close()
	main()

def clears():
	l.clear()
	p.clear()

def display():
	clears()
	lines = [line.strip() for line in open("username.txt")]
	for line in lines:
			l.append(line)

	pwd = [pd.strip() for pd in open("password.txt")]
	for pd in pwd:
			p.append(pd)
	print(l)
	print(p)

def retrieved():
	clears()
	lines = [line.strip() for line in open("username.txt")]
	for line in lines:
			l.append(line)
	pwd = [pd.strip() for pd in open("password.txt")]
	for pd in pwd:
			p.append(pd)
			
def login(get_index):
	clears()
	retrieved()
	he = l[get_index]
	print(f"Your Username: {he}")
	pass_ = input("Enter a password: ")
	if pass_ in p[get_index]:
		print(f"Login Succesfully! Welcome {he}!")
		main()	
	else:
		print("Wrong Password and Username!")
		login(get_index)




def change(get_index):
	clears()
	retrieved()
	pass_ = input("Enter a password: ")	
	if pass_ in p:
		pwd = input("New password: ")	
		p[get_index] = pwd
	else:
		print("Wrong Username or Password")
		change(get_index)
	print("Change Password Succesfully!")
	pe = open("password.txt", "w")
	print(p,file=pe)
	pe.close()
	with open("password.txt", mode="w") as ps:
		ps.write("\n".join(p) + "\n")
	main()


def user_id(get_index):
	clears()
	retrieved()
	users_id = input("Enter username: ")
	if users_id not in l:
		print("Incorrect Username")
		user_id(get_index)
	else:
		index = l.index(users_id)
		get_index(index)


		
# def pass_id(pw_index):
# 	user_id = input("Enter password: ")
# 	if user_id not in p:
# 		print("Incorrect Password")
# 	else:
# 		index = p.index(user_id)
# 		pw_index(index)

def main():
	while True:
		print("\nWELCOME TO AMBOT!\n[LOGIN | REGISTER | CHANGE PASSWORD]\n")
		print("Type 'Register' to register\nType 'Login' to login\nType 'Change' to change password\n")
		command = input("Enter your command: ").capitalize()
		if command == "Register":
			register()
			command = input("Enter your command: ").capitalize()
		elif command == "Login":
			user_id(login)
			command = input("Enter your command: ").capitalize()
		elif command == "Exit":
			print("Bye")
			break
		elif command == "Display":
			display()
			command = input("Enter your command: ").capitalize()
		elif command == "Change":
			user_id(change)
			command = input("Enter your command: ").capitalize()
		else:
			print("Error Command")
			command = input("Enter your command: ").capitalize()


main()