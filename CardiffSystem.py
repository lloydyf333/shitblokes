import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *
import csv


tutorAssignedStudents = []
tutor_list = []
Entr = ""
fontvar = ("Segoe UI Light", 18, "bold")


class System(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)
        window.grid_rowconfigure(6, weight=1)
        window.grid_columnconfigure(6, weight=1)
        window.grid(sticky=W + E + N + S)

        self.frames = {}
        for F in (MainMenu, Pg1, Pg2, Pg3):
            page_name = F.__name__
            frame = F(parent=window, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, controller, parent) :
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="----------=Cardiff University=---------- \n ----------=Tutor Managment System=----------", font=fontvar)
        label.grid(row=0, column=0, sticky=W)
        button1 = tk.Button(self, text="Search Tutor",
                            command=lambda: controller.show_frame("Pg1"))
        button2 = tk.Button(self, text="Assign Students",
                            command=lambda: controller.show_frame("Pg2"))
        button3 = tk.Button(self, text="Quota",
                            command=lambda: controller.show_frame("Pg3"))
        button1.grid(row=1, column=0, sticky=W)
        button2.grid(row=2, column=0, sticky=W)
        button3.grid(row=3, column=0, sticky=W)


class Pg1(tk.Frame):
    def __init__(self, parent, controller):
        global Entr
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tutor Search", font=fontvar)
        label.grid(row=0, column=0, sticky=W)

        button = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
        button.grid(row=7, column=0, sticky=W)

        label = tk.Label(self, text="Enter Tutor Name", font=fontvar)
        label.grid(row=3, column=0, sticky=W)

        Entr = Entry(self, textvariable=Entr)
        Entr.grid(row=4, column=0, sticky=W)

        button1 = tk.Button(self, text="Search", command=self.Submit)
        button1.grid(row=4, column=1, sticky=W)

    def Submit(self):
        count = 0
        count2 = 0
        count3 = 0
        query = Entr.get()
        listbox = tk.Listbox(self, width=70)
        listbox.grid(row=4, column=0, sticky=W)

        for i in tutor_list:

            
            if query == (i[1]+" "+i[0]):

                
                for a in tutorAssignedStudents:
                    count += 1
                    if a[4] == query:
                        self.student_list=[]
                        count3 += 1
                        self.student_list.append(a)
                        
                        for i in self.student_list:
                            listbox.insert(tk.END, i)

                   
                    elif count == len(tutorAssignedStudents) and count3 == 0:
                        label2 = tk.Label(self, text='Tutor has no students')
                        label2.grid(row=4, column=0, sticky=W)
                        break

                    elif count == len(tutorAssignedStudents):
                        break
            
            if query != (i[1]+" "+i[0]):
                count2 += 1

            if count2 == len(tutor_list) and count ==0:
                label2 = tk.Label(self, text='Tutor does not exist!')
                label2.grid(row=4, column=0, sticky=W)
                break


class Pg2(tk.Frame):  # class name


    def __init__(self, parent, controller):
        self.student_list = []

        tk.Frame.__init__(self, parent)
        self.controller = controller 
        label = tk.Label(self, text="Assign Students", font=fontvar)
        label.grid(row=0, column=0, sticky=W)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("MainMenu"))

        button.grid(row=6, column=1, sticky=W)

        button2 = tk.Button(self, text="Browse", command=self.readCSV,
                            width=10) 
        button2.grid(row=2, column=1, sticky=W) 


        label1 = tk.Label(self, text='Attach File')
        label1.grid(row=2, column=0, sticky=W)


        button3 = tk.Button(self, text="Assign", command=self.assign,
                            width=10)  
        button3.grid(row=5, column=1, sticky=W) 


        label2 = tk.Label(self, text='Automatically Assign Students')
        label2.grid(row=5, column=0, sticky=W)







    def readCSV(self):
        global tutor_list

        fname = askopenfilename(filetypes=(("CSV Files", "*.csv"),
                                          
                                           ("All files", "*.*")))

        file = open(fname, newline='')
        reader = csv.reader(file)

        header = next(reader)

        self.filePathVar = StringVar()
        self.filePathVar.set(fname)

        label3 = Label(self, textvariable=self.filePathVar)
        label3.grid(row=4, column=1, sticky=W)
        

        label4 = Label(self, text='File Attached:')
        label4.grid(row=4, column=2, sticky=W)
        

        for row in reader:
           

            self.student_list.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

        filEntr = open("test.csv", newline='')
        reader1 = csv.reader(filEntr)

        header1 = next(reader1)

        for row in reader1:
            

            tutor_list.append([row[0], row[1], row[2], row[3], row[4], row[5]])

    def assign(self):

        global tutorAssignedStudents
        lastAssignedStudent = 0
        recordsAssigned = []

        for tut in tutor_list:
            assignedStudentRecordCount = 0
            assignedStudentCount = 0

            for stu in self.student_list:
                assignedStudentRecordCount += 1  

                if (len(recordsAssigned) > 0) and not (assignedStudentRecordCount in recordsAssigned):

                    if tut[2] == stu[5] and stu[6] == tut[3]:  
                        assignedStudentCount += 1

                        recordsAssigned.append(assignedStudentRecordCount)

                        tutorAssignedStudents.append([stu[0], stu[1], stu[2], stu[3], tut[1] + " " + tut[0], stu[5], stu[6], stu[7]])
                        lastAssignedStudent = assignedStudentRecordCount  

                        if (assignedStudentCount >= 6 and tut[5] == 'PT') or (
                                        assignedStudentCount >= 11 and tut[5] == 'FT'):  
                            break
                elif len(recordsAssigned) == 0:
                    if tut[2] == stu[5] and stu[6] == tut[3]:  
                        assignedStudentCount += 1

                        recordsAssigned.append(assignedStudentRecordCount)

                        tutorAssignedStudents.append([stu[0], stu[1], stu[2], stu[3], tut[1] + " " + tut[0], stu[5], stu[6], stu[7]])
                        lastAssignedStudent = assignedStudentRecordCount  

                if assignedStudentCount == 120:
                    break

        label5 = Label(self, text='Students Assigned')
        label5.grid(row=6, column=0, sticky=W)
        


        return tutorAssignedStudents

class Pg3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Assign Students", font=fontvar)
        label.grid(row=0, column=0, sticky=W)
        button = tk.Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("MainMenu"))

        button.grid(row=0, column=1, sticky=W)

        label1 = Label(self, text="Quota of tutees each staff member has been assigned")

        button2 = Button(self, text="Press to calculate Quota", command=lambda: call(quota))

        label1.grid(row = 1, column = 1, sticky = W)
        button2.grid(row = 1, column = 2, sticky = W)

        def readCSVFile(filename):

            csvfile = open(filename, newline = '')
            rdr = csv.reader(csvfile)
            next(rdr)

            read_quota = {}
            for row in rdr:
                if row[4] in read_quota:
                    if row[6] in read_quota[row[4]]:
                        read_quota[row[4]][row[6]] += 1
                    else:
                        read_quota[row[4]][row[6]] = 1
                else:
                    read_quota[row[4]] = {row[6]: 1}

            return read_quota


        def call(quota):

            tutorLabels = []

            i = 0
            rowDisplay = 3
            columnDisplay = 1

            for tutor in quota:
                rowDisplay += 1

                display = tutor
                tutorLabels.append(Label(app, text = display, font = "Verdana 16 bold"))
                tutorLabels[i].grid(row = rowDisplay, column = columnDisplay, sticky = "W")
                
                for year in quota[tutor]:
                    i+=1
                    rowDisplay += 1
                    display = year + ": " + str(quota[tutor][year])
                    lb = tk.Listbox(self, width=10, height=10)
                    lb.grid(row=4, column=4, sticky=W)
                    lb.insert(tk.END, display)
                    


                i+=1

            global clean
            clean = [x for x in tutorLabels if x != None]

        quota = readCSVFile('student.csv')    

if __name__ == "__main__":
    app = System()
    app.mainloop()
