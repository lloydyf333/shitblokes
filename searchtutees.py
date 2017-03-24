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
        for F in (MainMenu, Pg1, Pg2):
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
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("Pg1"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("Pg2"))
        button3 = tk.Button(self, text="Go to page three", 
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

        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("MainMenu"))
        button.grid(row=6, column=1, sticky=W)

        label = tk.Label(self, text="Enter Tutor Name", font=fontvar)
        label.grid(row=2, column=0, sticky=W)

        Entr = Entry(self, textvariable=Entr)
        Entr.grid(row=3, column=0, sticky=W)

        button1 = tk.Button(self, text="Search", command=self.Submit)
        button1.grid(row=3, column=1, sticky=W)

    def Submit(self):
        count = 0
        count2 = 0
        count3 = 0
        x = Entr.get()
        query = x
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
        label = tk.Label(self, text="This is page 2", font=fontvar)
        label.grid(row=0, column=0, sticky=W)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("MainMenu"))

        button.grid(row=1, column=0, sticky=W)

        button2 = tk.Button(self, text="Browse", command=self.load_file,
                            width=10) 
        button2.grid(row=2, column=1, sticky=W) 


        label1 = tk.Label(self, text='Attach File')
        label1.grid(row=2, column=0, sticky=W)


        button3 = tk.Button(self, text="Assign", command=self.assign_students,
                            width=10)  
        button3.grid(row=5, column=1, sticky=W) 


        label2 = tk.Label(self, text='Automatically Assign Students')
        label2.grid(row=5, column=0, sticky=W)







    def load_file(self):
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
        label4.grid(row=4, column=0, sticky=W)
        

        for row in reader:
            # row = [Student Code, Surname, ForenamEntr, Forename2, TUTOR, Course, Acad Year, Univ Email]

            self.student_list.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

        filEntr = open("test.csv", newline='')
        reader1 = csv.reader(filEntr)

        header1 = next(reader1)

        for row in reader1:
            # row = [Surname, Forename, Course, Acad Year, Univ Email, Working Hours]

            tutor_list.append([row[0], row[1], row[2], row[3], row[4], row[5]])

    def assign_students(self):

        global tutorAssignedStudents
        lastAssignedStudent = 0
        recordsAssigned = []

        for t in tutor_list:
            assignedStudentRecordCount = 0
            assignedStudentCount = 0

            for s in self.student_list:
                assignedStudentRecordCount += 1  # counts the row position in the student_list

                if (len(recordsAssigned) > 0) and not (assignedStudentRecordCount in recordsAssigned):

                    if t[2] == s[5] and s[6] == t[3]:  # course and acadYear must match
                        assignedStudentCount += 1

                        recordsAssigned.append(assignedStudentRecordCount)

                        tutorAssignedStudents.append([s[0], s[1], s[2], s[3], t[1] + " " + t[0], s[5], s[6], s[7]])
                        lastAssignedStudent = assignedStudentRecordCount  # keeps a record of where loop was in the array from last assignment

                        if (assignedStudentCount >= 6 and t[5] == 'PT') or (
                                        assignedStudentCount >= 11 and t[5] == 'FT'):  # max of 6 is PT max of 11 if FT
                            break
                elif len(recordsAssigned) == 0:
                    if t[2] == s[5] and s[6] == t[3]:  # course and acadYear must match
                        assignedStudentCount += 1

                        recordsAssigned.append(assignedStudentRecordCount)

                        tutorAssignedStudents.append([s[0], s[1], s[2], s[3], t[1] + " " + t[0], s[5], s[6], s[7]])
                        lastAssignedStudent = assignedStudentRecordCount  # keeps a record of where loop was in the array from last assignment

                if assignedStudentCount == 120:
                    break

        label5 = Label(self, text='Students Assigned')
        label5.grid(row=6, column=0, sticky=W)
        # label5.pack(side="top", fill="x", pady=10)


        return tutorAssignedStudents

                  







if __name__ == "__main__":
    app = System()
    app.mainloop()
