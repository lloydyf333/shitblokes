from tkinter import *

class MainMenu(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def openAssign(self):
        import assign
        assign.StartWindow()
    
    def openSearch(self):
        import test1
        test1.StartWindow()
    
    def createTitle(self):
        lblTitle = Label(self, text='----------=Cardiff University=---------- \n ----------=Tutor Assignment=----------', font=('Segoe UI Light', 32), background="white")
        lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E, pady=10, padx=20)

    def createButtons(self):
        btnAssign = Button(self, text='Assign', font=('Segoe UI', 16), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF', command=self.openAssign)
        btnAssign.grid(row=1, column=1, columnspan=2, sticky=W+E, ipadx=40)
        btnReassign = Button(self, text='Search', font=('Segoe UI', 12), command=self.openSearch)
        btnReassign.grid(row=2, column=1, columnspan=2, sticky=W+E)

def StartWindow():
    root = Tk()
    root.title("Tutor & Tutee")
    root.resizable(0,0)
    app = MainMenu(root)
    app.configure(background="white")
    root.mainloop()

if __name__ == "__main__":
    import system