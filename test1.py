from Tkinter import *
from tkFileDialog import askopenfilename
import csv

tutorAssignedStudents = []

class MyFrame(Frame): #class name




    def __init__(self):
        self.studentList = []
        self.tutorList = []
        #self.tutorAssignedStudents = []

        Frame.__init__(self)            #starts Tkinter frame
        self.master.title("Example")    #Frame title
        self.master.rowconfigure(5, weight=1)   #row size
        self.master.columnconfigure(5, weight=1)    #column size
        self.grid(sticky=W+E+N+S)       #grid positions

        self.button = Button(self, text="Browse", command=self.load_file, width=10) #button with command function 'load_file'
        self.button.grid(row=1, column=1, sticky=W)             #button size/position

        self.label1 = Label(self, text = 'Upload')
        self.label1.grid(row =1, column= 0,sticky = W)

        self.button = Button(self, text="Assign", command=self.assign_students, width=10)  # button with command function 'load_file'
        self.button.grid(row=2, column=1, sticky=W)  # button size/position

        self.label1 = Label(self, text='Assignment')
        self.label1.grid(row=2, column=0, sticky=W)

        self.button = Button(self, text='showlist', command=self.getList, width=10)
        self.button.grid(row=2, column=0, sticky=W)

    def load_file(self):
        fname = askopenfilename(filetypes=(("CSV Files", "*.csv"),("All files", "*.*") ))  #files able to be viewed

        file = open(fname)
        reader = csv.reader(file)


        for row in reader:
            # row = [Student Code, Surname, Forename1, Forename2, TUTOR, Course, Acad Year, Univ Email]

            self.studentList.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])


        file1 = open("staff.csv")
        reader1 = csv.reader(file1)


        for row in reader1:
            # row = [Surname, Forename, Course, Acad Year, Univ Email, Working Hours]

            self.tutorList.append([row[0],row[1],row[2],row[3],row[4],row[5]])

            print(studentLists)



    def assign_students(self):

        global tutorAssignedStudents
        lastAssignedStudent = 0
        recordsAssigned = []

        for t in self.tutorList:
            assignedStudentRecordCount = 0
            assignedStudentCount = 0

            for s in self.studentList:
                assignedStudentRecordCount += 1           #counts the row position in the studentList

                if (len(recordsAssigned) > 0) and not(assignedStudentRecordCount in recordsAssigned):


                    if t[2] == s[5] and s[6] == t[3]:#course and acadYear must match
                        assignedStudentCount += 1

                        recordsAssigned.append(assignedStudentRecordCount)

                        tutorAssignedStudents.append([s[0],s[1],s[2],s[3],t[1] +" "+ t[0],s[5],s[6],s[7]])
                        lastAssignedStudent = assignedStudentRecordCount      #keeps a record of where loop was in the array from last assignment

                        if (assignedStudentCount >= 6 and t[5] == 'PT') or (assignedStudentCount >= 11 and t[5] == 'FT'): #max of 6 is PT max of 11 if FT
                            break
                elif len(recordsAssigned) == 0:
                    if t[2] == s[5] and s[6] == t[3]:#course and acadYear must match
                        assignedStudentCount += 1

                        recordsAssigned.append(assignedStudentRecordCount)

                        tutorAssignedStudents.append([s[0],s[1],s[2],s[3],t[1] +" "+ t[0],s[5],s[6],s[7]])
                        lastAssignedStudent = assignedStudentRecordCount      #keeps a record of where loop was in the array from last assignment

                if assignedStudentCount == 120:
                    break

        return tutorAssignedStudents

    def getList(self):
        print (tutorAssignedStudents)

if __name__ == "__main__":
    MyFrame().mainloop()        