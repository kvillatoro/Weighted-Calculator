# This program converts distances in kilometers
# to miles. The result is displayed in an info
# dialog box.

import tkinter
import tkinter.messagebox

class GradeCalulatorGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create frames to group widgets.
        #self.student_name_frame = tkinter.Frame(self.main_window)
        self.assignment_frame = tkinter.Frame(self.main_window)
        self.quiz_frame = tkinter.Frame(self.main_window)
        self.participation_frame = tkinter.Frame(self.main_window)
        self.test_frame = tkinter.Frame(self.main_window)
        self.hw_frame = tkinter.Frame(self.main_window)
        self.lab_frame = tkinter.Frame(self.main_window)
        self.project_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

#####################WIDGETS#########################################################
        #Student name input
        #prompt
        #self.name_frame_label = tkinter.Label(self.student_name_frame, text= 'Enter student name: ')
        #input
       # self.name = tkinter.Entry(self.student_name_frame, width = 10)

        #Assignment widgets
        #Assignment grade input        
        self.ass_grade_label = tkinter.Label(self.assignment_frame, text='Totaled Assignment Grade: ')
        self.ass_grade = tkinter.Entry(self.assignment_frame, width=10)
        #Assignment percentage worth
        self.ass_perc_label = tkinter.Label(self.assignment_frame, text='Assignment Percentage: ')
        self.ass_perc = tkinter.Entry(self.assignment_frame, width=10)

        #Quiz Widgets
        #Quiz grade input        
        self.quiz_grade_label = tkinter.Label(self.quiz_frame, text='Totaled Quiz Grade: ')
        self.quiz_grade = tkinter.Entry(self.quiz_frame, width=10)
        #Quiz grade percentage worth
        self.quiz_perc_label = tkinter.Label(self.quiz_frame, text='Quiz Percentage: ')
        self.quiz_perc = tkinter.Entry(self.quiz_frame, width=10)

        #Participation Widgets
        #Participation grade input        
        self.participation_grade_label = tkinter.Label(self.participation_frame, text='Totaled Participation Grade: ')
        self.participation_grade = tkinter.Entry(self.participation_frame, width=10)
        #Participation percentage worth
        self.participation_perc_label = tkinter.Label(self.participation_frame, text='Participation Percentage: ')
        self.participation_perc = tkinter.Entry(self.participation_frame, width=10)

        #Test Widgets
        #Test grade input        
        self.test_grade_label = tkinter.Label(self.test_frame, text='Totaled Test Grade: ')
        self.test_grade = tkinter.Entry(self.test_frame, width=10)
        #Tests percentage worth
        self.test_perc_label = tkinter.Label(self.test_frame, text='Test Percentage: ')
        self.test_perc = tkinter.Entry(self.test_frame, width=10)

        #HW Widgets
        #HW grade input        
        self.hw_grade_label = tkinter.Label(self.hw_frame, text='Totaled Homework Grade: ')
        self.hw_grade = tkinter.Entry(self.hw_frame, width=10)
        #HW percentage worth
        self.hw_perc_label = tkinter.Label(self.hw_frame, text='Homework Percentage: ')
        self.hw_perc = tkinter.Entry(self.hw_frame, width=10)

        #Lab Widgets
        #Lab grade input        
        self.lab_grade_label = tkinter.Label(self.lab_frame, text='Totaled Lab Grade: ')
        self.lab_grade = tkinter.Entry(self.lab_frame, width=10)
        #Lab grade percentage worth
        self.lab_perc_label = tkinter.Label(self.lab_frame, text='Lab Percentage: ')
        self.lab_perc = tkinter.Entry(self.lab_frame, width=10)

        #Project Widgets
        #Project grade input        
        self.project_grade_label = tkinter.Label(self.project_frame, text='Totaled Project Grade: ')
        self.project_grade = tkinter.Entry(self.project_frame, width=10)
        #Project grade percentage worth
        self.project_perc_label = tkinter.Label(self.project_frame, text='Project Percentage: ')
        self.project_perc = tkinter.Entry(self.project_frame, width=10)
        
###############Pack the frames widgets.##########################################
        #pack Assignment Grade
        self.ass_grade_label.pack(side='left')
        self.ass_grade.pack(side='left')
        #Pack Assignment Percentage 
        self.ass_perc_label.pack(side='left')
        self.ass_perc.pack(side='left')

        #pack Quiz Grade
        self.quiz_grade_label.pack(side='left')
        self.quiz_grade.pack(side='left')
        #Pack Quiz Percentage 
        self.quiz_perc_label.pack(side='left')
        self.quiz_perc.pack(side='left')

        #pack Participation Grade
        self.participation_grade_label.pack(side='left')
        self.participation_grade.pack(side='left')
        #Pack Participation Percentage 
        self.participation_perc_label.pack(side='left')
        self.participation_perc.pack(side='left')

        #pack Test Grade
        self.test_grade_label.pack(side='left')
        self.test_grade.pack(side='left')
        #Pack Test Percentage 
        self.test_perc_label.pack(side='left')
        self.test_perc.pack(side='left')

        #pack HW Grade
        self.hw_grade_label.pack(side='left')
        self.hw_grade.pack(side='left')
        #Pack HW Percentage 
        self.hw_perc_label.pack(side='left')
        self.hw_perc.pack(side='left')

        #pack Lab Grade
        self.lab_grade_label.pack(side='left')
        self.lab_grade.pack(side='left')
        #Pack Lab Percentage 
        self.lab_perc_label.pack(side='left')
        self.lab_perc.pack(side='left')
        
        #pack project Grade
        self.project_grade_label.pack(side='left')
        self.project_grade.pack(side='left')
        #Pack project Percentage 
        self.project_perc_label.pack(side='left')
        self.project_perc.pack(side='left')
        
#######################BUTTON FRAME CREATION AND PACKING#############################################
        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
#######################################################################################

        # Pack the frames.
        self.assignment_frame.pack()
        self.quiz_frame.pack()
        self.participation_frame.pack()
        self.test_frame.pack()
        self.hw_frame.pack()
        self.lab_frame.pack()
        self.project_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

#######################################################################################
    #Calculate  
    def calculate(self):
        #Get the value entered by the user into the
        #Assignment total widget.
        aPercentage = float(self.ass_perc.get()) * .01
        aGrade = float(self.ass_grade.get())
        aTotal = aPercentage * aGrade
        #Quiz total widget.
        qPercentage = float(self.quiz_perc.get()) * .01
        qGrade = float(self.quiz_grade.get())
        qTotal = qPercentage * qGrade
        #Participation total widget.
        paPercentage = float(self.participation_perc.get()) * .01
        paGrade = float(self.participation_grade.get())
        paTotal = paPercentage * paGrade
        #Test total widget.
        tPercentage = float(self.test_perc.get()) * .01
        tGrade = float(self.test_grade.get())
        tTotal = tPercentage * tGrade
        #HW total widget.
        hPercentage = float(self.hw_perc.get()) * .01
        hGrade = float(self.hw_grade.get())
        hTotal = hPercentage * hGrade
        #Lab total widget.
        lPercentage = float(self.lab_perc.get()) * .01
        lGrade = float(self.lab_grade.get())
        lTotal = lPercentage * lGrade
        #Projects total widget.
        prPercentage = float(self.project_perc.get()) * .01
        prGrade = float(self.project_grade.get())
        prTotal = prPercentage * prGrade
        
        # Convert show grades
        total = ((aTotal) + (qTotal)+ (paTotal) + (tTotal) + (hTotal) + (lTotal) + (prTotal))   
        
        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo('TOTAL GRADE','Your grade is: ' + str(total) +'%')
        
################################REPORT CARD#########################################   
        f = open("Report_Card.txt", "w")
        f.write('\t\t')
        f.write('Grade\t')
        f.write('Percentage')
        
        f.write('\nAssignment:\t')
        f.write(str(aGrade))
        f.write('%')
        f.write('\t')
        f.write(str(aTotal))
        f.write('%')
        
        f.write('\nQuiz:\t\t')
        f.write(str(qGrade))
        f.write('%')
        f.write('\t')
        f.write(str(qTotal))
        f.write('%')
        
        f.write('\nParticipation:\t')
        f.write(str(paGrade))
        f.write('%')
        f.write('\t')
        f.write(str(paTotal))
        f.write('%')
        
        f.write('\nTest:\t\t')
        f.write(str(tGrade))
        f.write('%')
        f.write('\t')
        f.write(str(tTotal))
        f.write('%')
        
        f.write('\nHomework:\t')
        f.write(str(hGrade))
        f.write('%')
        f.write('\t')
        f.write(str(hTotal))
        f.write('%')
        
        f.write('\nLab:\t\t')
        f.write(str(lGrade))
        f.write('%')
        f.write('\t')
        f.write(str(lTotal))
        f.write('%')
        
        f.write('\nProject:\t')
        f.write(str(prGrade))
        f.write('%')
        f.write('\t')
        f.write(str(prTotal))
        f.write('%')
        
        f.write('\n\nTotal:\t\t\n')        
        f.write(str(aTotal+qTotal+paTotal+tTotal+hTotal+lTotal+prTotal))
        f.write('%')
        f.close()

# Create an instance of the KiloConverterGUI class.
grader = GradeCalulatorGUI()
