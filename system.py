from Tkinter import *
import tkMessageBox
import csv        


def validation(user, password):
	with open('staff.csv') as csvfile:
		rdr = [row for row in csv.reader(csvfile.read().splitlines())]
		for row in rdr:
			if row[0] == user:
				if row[8] == password:
					return True
				else:
					return False
                


class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createTitle()
        self.createInputs()
        self.createButton()
        

    def doLogin(self):
        if not (validation(self.txtUser.get(), self.txtPass.get())):
        	tkMessageBox.showerror("Login Error", "Incorrect username or password")
        else:
        	import mainmenu
        	root.destroy()
        	mainmenu.StartWindow()
                

    def createTitle(self):
    	lblTitle = Label(self, text='Cardiff admin login', font=('Segoe UI Light', 32), background="white")
    	lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E)

    def createInputs(self):      
    	lblUser = Label(self, text='Username:', font=('Segoe UI Light', 18), background="white")
        lblUser.grid(row=1, column=0, columnspan=3, sticky=W+E)

        lblPass = Label(self, text='Password:', font=('Segoe UI Light', 18), background="white")
        lblPass.grid(row=3, column=0, columnspan=3, sticky=W+E)

        self.txtUser = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
        self.txtUser.grid(row=2, column=0, columnspan=3, sticky=W+E, padx=20)

        self.txtPass = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white', show = "*")
        self.txtPass.grid(row=4, column=0, columnspan=3, sticky=W+E, padx=20)

    def createButton(self):
    	btnSubmit = Button(self, text='Login',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT, command=self.doLogin)
        btnSubmit.grid(row=6, column=1, pady=10, ipadx=2)

    
    


root = Tk()
root.title("login")
root.resizable(0,0)
app = Login(root)
app.configure(background="white")
root.mainloop()
 
