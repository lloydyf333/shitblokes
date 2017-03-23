from tkinter import *
from tkinter.filedialog import askopenfilename
import csv


tutorAssignedStudents = []

class AssignMain(Frame): #name of class
    def __init__(self): #initializer
        self.studentList = []
        self.tutorList = []

        Frame.__init__(self) #Frame 
        self.master.title("Assign")       
        self.grid(sticky=W+E+N+S)       

        self.button = Button(self, text="Browse", command=self.readCSV, width=10) #command button activates function readCSV()
        self.button.grid(row=1, column=1, sticky=W)            

        self.label1 = Label(self, text = 'Upload')
        self.label1.grid(row =1, column= 0,sticky = W)

        self.button = Button(self, text="Assign", command=self.assign, width=10)  #command button activates function assign()
        self.button.grid(row=2, column=1, sticky=W)  

        self.label1 = Label(self, text='Assignment')
        self.label1.grid(row=2, column=0, sticky=W)

        self.button = Button(self, text="showlist", command=self.seeList, width=10)  #command button activates function seeList()
        self.button.grid(row=3, column=1, sticky=W)

        self.button = Button(self, text='Main Menu', command=self.backToMenu, width=10)
        self.button.grid(row=0, column=0, sticky=S)

    def readCSV(self):
        filename = askopenfilename(filetypes=(("CSV Files", "*.csv"),  #filename varible set to open dialog selction (only .csv)
                                           ("All files", "*.*") ))  #files able to be viewed

        selected_file = open(filename, newline='')
        rdr = csv.reader(selected_file)
        header = next(rdr)

        for row in rdr:

            self.studentList.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]]) #appends all information from csv to student_list in order specified

        selected_file2 = open("test.csv", newline='')
        rdr2 = csv.reader(selected_file2)
        header1 = next(rdr2)

        for row in rdr2:

            self.tutorList.append([row[0],row[1],row[2],row[3],row[4],row[5]]) #appends all information from csv to tutor_list in order specified



    def assign(self):

        global tutorAssignedStudents
        lastAssignedStudent = 0
        recordsAssigned = []

        for tut in self.tutorList:
            assignedStudentCount = 0
            assignedStudentCount = 0

            for stu in self.studentList:
                assignedStudentCount += 1           

                if (len(recordsAssigned) > 0) and not(assignedStudentCount in recordsAssigned):


                    if tut[2] == stu[5] and stu[6] == tut[3]:
                        assignedStudentCount += 1 #Makes sure course and academic year match in order to assign automatically correctly

                        recordsAssigned.append(assignedStudentCount)

                        tutorAssignedStudents.append([stu[0],stu[1],stu[2],stu[3],tut[1] +" "+ tut[0],stu[5],stu[6],stu[7]])
                        lastAssignedStudent = assignedStudentCount #records where the loop was in the array last time infomation was assigned

                        
                elif len(recordsAssigned) == 0:
                    if tut[2] == stu[5] and stu[6] == tut[3]:
                        assignedStudentCount += 1

                        recordsAssigned.append(assignedStudentCount)

                        tutorAssignedStudents.append([stu[0],stu[1],stu[2],stu[3],tut[1] +" "+ tut[0],stu[5],stu[6],stu[7]])
                        lastAssignedStudent = assignedStudentCount 

                if assignedStudentCount == 200:
                    break

        return tutorAssignedStudents

    def seeList(self):
        print (tutorAssignedStudents)


    def backToMenu(self):
        import mainmenu
        mainmenu.StartWindow()

def StartWindow():
    root = Tk()
    root.title("Assign")
    root.resizable(0,0)
    app = AssignMain(root)
    app.configure(background="white")
    root.mainloop()    
            


if __name__ == "__main__":
    AssignMain().mainloop()