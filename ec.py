import csv
import os			#Only to check if the file already exits.
import getpass		#To hide the password.

email = ""
password = ""
firstName = ""
lastName = ""
l_email = []
l_password = []
r_email = ""
download_dir = "data.csv"

def init():
	global l_email, l_password
	if os.path.exists("data.csv"):
	    pass
	else:
	    out = open(download_dir, "a")
	    columnTitleRow = "email, password, first_name, last_name\n"
	    out.write(columnTitleRow)
	    out.close()

	if os.path.exists("inbox.csv"):
	    pass
	else:
	    out = open("inbox.csv", "a")
	    columnTitleRow = "receiverEmail, senderEmail, inbox\n"
	    out.write(columnTitleRow)
	    out.close()

	if os.path.exists("outbox.csv"):
	    pass
	else:
	    out = open("outbox.csv", "a")
	    columnTitleRow = "senderEmail, receiverEmail, outbox\n"
	    out.write(columnTitleRow)
	    out.close()

	with open("data.csv",'rb') as f:
		reader = csv.reader(f)
		for line in reader:
		    l_email.append(line[0])
		    l_password.append(line[1])
	f.close()

def update():
	global l_email, l_password
	l_email = []
	l_password = []
	with open("data.csv",'rb') as f:
		reader = csv.reader(f)
		for line in reader:
			l_email.append(line[0])
			l_password.append(line[1])
	f.close()

def register():
	global email, password, firstName, lastName, download_dir
	print ("\nRegister :-")
	email = raw_input("Enter Username (email): ") 
	password = getpass.getpass("Enter Password: ")
	firstName = raw_input("Enter First Name: ")
	lastName = raw_input("Enter Last Name: ")
 
	out = open(download_dir, "a") 
	
	row = email + "," + password + "," + firstName + "," + lastName + "\n"
	out.write(row)
	out.close()

	logout()


def login():
	global email, password
	print ("\nLogin :-")
	email = raw_input("Enter Email: ")
	password = getpass.getpass("Enter Password: ")
	authenticate()

def authenticate():
	global email, password, l_email, l_password
	status = False
	for i, em in enumerate(l_email):
		if email == l_email[i] and password == l_password[i]:
			status = True
			break
		else:
			status = False
	if status == True:
		print "\nWelcome"
		dashboard()
	else:
		print "\nAuthentication Failed"
		home()

def home():
	print ("\nHome\n[0] Register\n[1] Login")
	inpt = int(input())
	if inpt == 0:
		register()
	elif inpt == 1:
		login()
	else:
		print ("Invalid input\n")
		home()

def dashboard():
	global email
	print ("\nDashboard:" + email + "\n\n[0] View My Inbox\n[1] View My Outbox\n[2] Send New Message\n[3] Logout")
	inpt = input()
	if inpt == 0:
		inbox()
	elif inpt == 1:
		outbox()
	elif inpt == 2:
		sendMessage()
	elif inpt == 3:
		logout()
	else:
		print ("Invalid Input\n")
		dashboard()

def logout():
	update()
	home()

def sendMessage():
	global email
	print "Send Message :-"
	r_email = raw_input("To: ")
	message = raw_input("Enter Message: ")

	out = open("inbox.csv", "a")
	row = r_email + "," + email + "," + message + "\n"
	out.write(row)
	out.close()

	out = open("outbox.csv", "a")
	row = email + "," + r_email + "," + message + "\n"
	out.write(row)
	out.close()

	dashboard()

def inbox():
	global email
	message = ""
	print "\nInbox :-" + email + "\n"

	with open("inbox.csv",'rb') as f:
		reader = csv.reader(f)
		for line in reader:
		    if email == line[0]:
		    	print "\nFrom: " + line[1]
		    	print "Message: " + line[2]
	f.close()

	dashboard()


def outbox():
	global email
	message = ""
	print "\nOutbox :-" + email + "\n"

	with open("outbox.csv",'rb') as f:
		reader = csv.reader(f)
		for line in reader:
		    if email == line[0]:
		    	print "\nTo: " + line[1]
		    	print "Message: " + line[2]
	f.close()

	dashboard()

init()
home()