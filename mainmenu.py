from Tkinter import *



class MainMenu(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def openAssign(self):
    	root.destroy()
    	import assign   

    def createTitle(self):
        lblTitle = Label(self, text='Cardiff System ting', font=('Segoe UI Light', 32), background="white")
        lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E, pady=10, padx=20)

    def createButtons(self):
        btnAssign = Button(self, text='Assign', font=('Segoe UI', 16), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF', command=self.openAssign)
        btnAssign.grid(row=1, column=1, columnspan=2, sticky=W+E, ipadx=40)
          


root = Tk()
root.title("Tutor & Tutee")
root.resizable(0,0)
app = MainMenu(root)
app.configure(background="white")
root.mainloop()