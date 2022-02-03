import socket
from tkinter import *

3
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostIp = socket.gethostbyname('0.0.0.0')
portNumber = 1234
serverSocket.bind((hostIp, portNumber))
serverSocket.listen()
print("Waiting for connection...")

clientSocket, clientAddress = serverSocket.accept()
#client, address = serverSocket.accept()


# creating root object
root = Tk()


# defining size of window
root.geometry("2000x2000")

# setting up the title of window
root.title("Message Decryption")

Tops = Frame(root, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700,
							relief = SUNKEN)
f1.pack(side = TOP)
#scrollbar = ttk.Scrollbar(root, orient='vertical', command=f1.yview)
#scrollbar.grid(row=0, column=1, sticky='ns')

#  communicate back to the scrollbar
#f1['yscrollcommand'] = scrollbar.set


lblInfo = Label(Tops, font = ('helvetica', 30, 'bold'),
		text = "MESSAGE DECRYPTION",
					fg = "Black", bd = 10, anchor='w')
					
lblInfo.grid(row = 0, column = 0)

						
rand = StringVar()
Msg = StringVar()
key = StringVar()
key2=StringVar()
key3=StringVar()
key4=StringVar()
Result = StringVar()
Result2 = StringVar()
Result3 = StringVar()
Result4 = StringVar()

# exit function
def qExit():
	root.destroy()

# Function to reset the window
def Reset():
	rand.set("")
	Msg.set("")
	key.set("")
	Result.set("")



# labels
lblMsg = Label(f1, font = ('arial', 16, 'bold'),
		text = "Encrypted Message:", bd = 10, anchor = "w")
		
lblMsg.grid(row = 2, column = 2)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = Msg, bd = 5, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtMsg.grid(row = 2, column = 3)

lblMsg = Label(f1, font = ('arial', 18, 'bold'),
		text = "By using MD5", bd = 6, anchor = "w")
		
lblMsg.grid(row = 3, column = 3)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the fourth Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 4, column = 1)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),show="*",
		textvariable = key4, bd = 5, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtkey.grid(row = 4, column = 2)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Decrypted Message4:", bd = 16, anchor = "w")
			
lblService.grid(row = 4, column = 4)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result4, bd = 5, insertwidth = 4,
					bg = "powder blue", justify = 'right')
						
txtService.grid(row = 4, column = 5)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the third Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 5, column = 1)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),show="*",
		textvariable = key3, bd = 5, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtkey.grid(row = 5, column = 2)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Decrypted Message3:", bd = 16, anchor = "w")
			
lblService.grid(row = 5, column = 4)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result3, bd = 5, insertwidth = 4,
					bg = "powder blue", justify = 'right')
						
txtService.grid(row = 5, column = 5)

lblMsg = Label(f1, font = ('arial', 18, 'bold'),
		text = "By using AES", bd = 6, anchor = "w")
		
lblMsg.grid(row = 6, column = 3)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the second Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 7, column = 1)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),show="*",
		textvariable = key2, bd = 5, insertwidth = 4,
				bg = "powder blue", justify = 'right')
			
txtkey.grid(row = 7, column = 2)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Decrypted Message2:", bd = 16, anchor = "w")
			
lblService.grid(row = 7, column = 4)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result2, bd = 5, insertwidth = 4,
					bg = "powder blue", justify = 'right')
						
txtService.grid(row = 7, column = 5)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the first Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 8, column = 2)

txtkey = Entry(f1, font = ('arial', 16, 'bold'),show="*",
		textvariable = key, bd = 5, insertwidth = 4,
				bg = "powder blue", justify = 'right')
				
txtkey.grid(row = 8, column = 3)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Decrypted Message:", bd = 16, anchor = "w")
			
lblService.grid(row = 10, column = 2)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result, bd = 5, insertwidth = 4,
					bg = "powder blue", justify = 'right')
						
txtService.grid(row = 10, column = 3)


import base64

# Function to decode text4
def decode4(key4, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key4[i % len(key4)]
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec)


def Ref4():
	print("Message= ", (Msg.get()))
	clear = Msg.get()
	k4 = key4.get()
	Result4.set(decode4(k4, clear))
 
# Function to decode text3
def decode3(key3, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key3[i % len(key3)]
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec)


def Ref3():
	print("Message= ", (Msg.get()))
	clear = Result4.get()
	k3 = key3.get()
	Result3.set(decode3(k3, clear))


# Function to decode text2
def decode2(key2, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key2[i % len(key2)]
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec) 

def Ref2():
	print("Message= ", (Msg.get()))
	clear = Result3.get()
	k2 = key2.get()
	Result2.set(decode2(k2, clear))


# Function to decode text1
def decode(key, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec)


def Ref():
	print("Message= ", (Msg.get()))
	clear = Result2.get()
	k = key.get()
	Result.set(decode(k, clear))
 
#############################

def receiveMessage():
    message = clientSocket.recv(2048).decode()
    Msg.set(message)

# Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Decrypt", bg = "powder blue",
						command = Ref4).grid(row = 4, column = 3)

btnTotal = Button(f1, padx = 16, pady = 8, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Decrypt", bg = "powder blue",
						command = Ref3).grid(row = 5, column = 3)

btnTotal = Button(f1, padx = 16, pady = 8, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Decrypt", bg = "powder blue",
						command = Ref2).grid(row = 7, column = 3)
btnTotal = Button(f1, padx = 16, pady = 8, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Decrypt", bg = "powder blue",
						command = Ref).grid(row = 9, column = 3)



# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 5,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Reset", bg = "green",
				command = Reset).grid(row = 11, column = 1)

# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 5,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Exit", bg = "red",
				command = qExit).grid(row = 11, column = 5)

# Receive button
btnSend = Button(f1, padx = 5, pady = 5, bd = 5,
				fg = "black", font = ('arial', 16, 'bold'),
					width = 10, text = "Receive", bg = "blue",
				command = receiveMessage).grid(row = 1, column = 3)

# keeps window alive
root.mainloop()
