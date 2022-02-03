import socket
from tkinter import *


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# creating root object
root = Tk()

# defining size of window
root.geometry("2000x2000")

# setting up the title of window
root.title("Message Encryption")

Tops = Frame(root, width = 100, relief = RIDGE)
Tops.pack(side = TOP)

f1 = Frame(root, width = 100, height = 100,
							relief = RIDGE)
f1.pack(side = TOP)



lblInfo = Label(Tops, font = ('helvetica', 30, 'bold'),
		text = "MESSAGE ENCRYPTION",
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
ip = StringVar()

# set ip function
def setIP():
    host = ip.get()
    HOST_ADDR = socket.gethostbyname(host)
    hostIp = HOST_ADDR
    portNumber = 1234
    
    print(HOST_ADDR)
    clientSocket.connect((hostIp, portNumber))
    return host
    

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
		text = "Enter IP Address:", bd = 16, anchor = "w")
		
lblMsg.grid(row = 1, column = 3)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = ip, bd = 5, insertwidth = 4,
				bg = "#d6a3ff", justify = 'right')
				
txtMsg.grid(row = 1, column = 4)

lblMsg = Label(f1, font = ('arial', 16, 'bold'),
		text = "Enter Message:", bd = 16, anchor = "w")
		
lblMsg.grid(row = 3, column = 3)

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
		textvariable = Msg, bd = 5, insertwidth = 4,
				bg = "#d6a3ff", justify = 'right')
				
txtMsg.grid(row = 3, column = 4)

lblMsg = Label(f1, font = ('arial', 18, 'bold'),
		text = "By using AES", bd = 10, anchor = "w")
		
lblMsg.grid(row = 4, column = 4)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the first Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 5, column = 2)

txtkey = Entry(f1, font = ('arial', 16, 'bold'), show="*",
		textvariable = key, bd = 5, insertwidth = 4,
				bg = "#d6a3ff", justify = 'right')
				
txtkey.grid(row = 5, column = 3)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Encrypted Message1:", bd = 16, anchor = "w")
			
lblService.grid(row = 5, column = 5)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result, bd = 5, insertwidth = 4,
					bg = "#d6a3ff", justify = 'right')
						
txtService.grid(row = 5, column = 6)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the second Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 6, column = 2)

txtkey = Entry(f1, font = ('arial', 16, 'bold'), show="*",
		textvariable = key2, bd = 5, insertwidth = 4,
				bg = "#d6a3ff", justify = 'right')
				
txtkey.grid(row = 6, column = 3)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Encrypted Message2:", bd = 16, anchor = "w")
			
lblService.grid(row = 6, column = 5)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result2, bd = 5, insertwidth = 4,
					bg = "#d6a3ff", justify = 'right')
						
txtService.grid(row = 6, column = 6)

lblMsg = Label(f1, font = ('arial', 18, 'bold'),
		text = "By using MD5", bd = 10, anchor = "w")
		
lblMsg.grid(row = 7, column = 4)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the third Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 8, column = 2)

txtkey = Entry(f1, font = ('arial', 16, 'bold'), show="*",
		textvariable = key3, bd = 5, insertwidth = 4,
				bg = "#d6a3ff", justify = 'right')
				
txtkey.grid(row = 8, column = 3)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Encrypted Message3:", bd = 16, anchor = "w")
			
lblService.grid(row = 8, column = 5)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result3, bd = 5, insertwidth = 4,
					bg = "#d6a3ff", justify = 'right')
						
txtService.grid(row = 8, column = 6)

lblkey = Label(f1, font = ('arial', 16, 'bold'),
			text = "Enter the fourth Key:", bd = 16, anchor = "w")
			
lblkey.grid(row = 9, column = 2)

txtkey = Entry(f1, font = ('arial', 16, 'bold'), show="*",
		textvariable = key4, bd = 5, insertwidth = 4,
				bg = "#d6a3ff", justify = 'right')
				
txtkey.grid(row = 9, column = 3)


lblService = Label(f1, font = ('arial', 16, 'bold'),
			text = "Encrypted Message4:", bd = 16, anchor = "w")
			
lblService.grid(row = 9, column = 5)

txtService = Entry(f1, font = ('arial', 16, 'bold'),
			textvariable = Result4, bd = 5, insertwidth = 4,
					bg = "#d6a3ff", justify = 'right')
						
txtService.grid(row = 9, column = 6)

import base64

# Function to encode
def encode(key, clear):
	enc = []
	
	for i in range(len(clear)):
		key_c = key[i % len(key)]
		enc_c = chr((ord(clear[i]) +
					ord(key_c)) % 256)
					
		enc.append(enc_c)
		
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def Ref():
	print("Message= ", (Msg.get()))
	clear = Msg.get()
	k = key.get()
	return Result.set(encode(k, clear))

def Ref2():
	print("Message= ", (Result.get()))
	clear = Result.get()
	k = key2.get()
	return Result2.set(encode(k, clear))

def Ref3():
    print("Message= ", (Result2.get()))
    clear = Result2.get()
    k = key3.get()
    return Result3.set(encode(k, clear))

def Ref4():
    print("Message= ", (Result3.get()))
    clear = Result3.get()
    k = key4.get()
    return Result4.set(encode(k, clear))
 
def sendMessage():
    clientMessage = Result4.get()
    if clientMessage:clientSocket.send(clientMessage.encode())
    


# connect button
btnTotal = Button(f1, padx = 5, pady = 5, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Connect", bg = "#74ff5c",
						command = setIP).grid(row = 2, column = 4)


# Encrypt button
btnTotal = Button(f1, padx = 5, pady = 5, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Encrypt", bg = "#74ff5c",
						command = Ref).grid(row = 5, column = 4)

btnTotal = Button(f1, padx = 5, pady = 5, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Encrypt", bg = "#74ff5c",
						command = Ref2).grid(row = 6, column = 4)

btnTotal = Button(f1, padx = 5, pady = 5, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Encrypt", bg = "#74ff5c",
						command = Ref3).grid(row = 8, column = 4)

btnTotal = Button(f1, padx = 5, pady = 5, bd = 5, fg = "black",
						font = ('arial', 16, 'bold'), width = 10,
					text = "Encrypt", bg = "#74ff5c",
						command = Ref4).grid(row = 9, column = 4)

# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 5,
				fg = "black", font = ('arial', 20, 'bold'),
					width = 10, text = "Reset", bg = "yellow",
				command = Reset).grid(row = 10, column = 2)

# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 5,
				fg = "black", font = ('arial', 20, 'bold'),
					width = 10, text = "Exit", bg = "red",
				command = qExit).grid(row = 10, column = 6)

# Send button
btnSend = Button(f1, padx = 16, pady = 8, bd = 5,
				fg = "white", font = ('arial', 20, 'bold'),
					width = 10, text = "Send", bg = "#2b00ff",
				command = sendMessage).grid(row = 10, column = 4)

# keeps window alive
root.mainloop()
