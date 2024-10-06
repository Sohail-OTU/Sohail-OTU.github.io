#!/usr/bin/env python
# coding: utf-8

# In[ ]:


########################### Created by Sohail Baig, Ahmed Amoodi, Ahmer Othi ###########################################
#### Sohail Baig - 100924522
#### Ahmed Amoodi - 100915352
#### Ahmer Imran Othi - 100920172


#############################################  Student Ledger #######################################################

import os
from tabulate import tabulate

def table_of_data(x):
    headerss = ["Student #", "First Name", "Middle Name", "Last Name", "Date of Birth", "Gender", "Department", "Email", "Phone Number", "Address", "Emergency", "Courses", "Fees", "Awards & Financial Aid", "Final Grades"]
    table = tabulate(x, headers = headerss, tablefmt = "grid")
    return table

def table_of_data_specific(student_details):
    headerss = ["Student #", "First Name", "Middle Name", "Last Name", "Date of Birth", "Gender", "Department", "Email", "Phone Number", "Address", "Emergency", "Courses", "Fees", "Awards & Financial Aid", "Final Grades"]
    table = tabulate(student_details, headers = headerss, tablefmt = "grid")
    return table
    
print("\t\t\t\t\tAdmin Login Page\n\n")
student_data = []
student_number = 0
end_1 = False
end_2 = False

while True:
    end_1 = False
## This block of code is the first opening part of the ledger; The login page.
    user_name = input("\t\t\tUsername: ")
    pass_word = input("\t\t\tPassword: ")
    
    while not end_1:
        end_2 = False
        if user_name != 'Admin' or pass_word != 'password':
            print("\n\t\t\t\tIncorrect User Credentials\n")
            break
        
        ## Now we move on to the main page where we have 4 options:
        ## 1 - Add a new student
        ## 2 - Display student database
        ## 3 - Search student details
        ## 4 - Exit system
        ## If they exit system it should just go back to the login page
        print("\n\n\n\t\t\t\t\tStudent Ledger")
        print("\n\t\t[1] - Add a New Student \t\t[2] - Display Student Database")
        print("\t\t[3] - Search Student Details \t\t[4] - Exit System")
        
        while not end_2:
            ledger_menu = input("\n\t\t\t\t\t")
            
            if ledger_menu == '1':
                print("\n\t\t\t\t\tNew Student Details\n")

                while not end_2:
                    first_name = input("\t\tFirst Name: ")
                    middle_name = input("\t\tMiddle Name: ")
                    last_name = input("\t\tLast Name: ")
                    dob = input("\t\tDate of Birth: ")
                    gender = input("\t\tGender: ")
                    department = input("\t\tDepartment: ")
                    email = input("\t\tEnter Email: ")
                    phone_number = input("\t\tPhone Number: ")
                    address = input("\t\tAddress: ")
                    emergency = input("\t\tEmergency Contact: ")
                    opt_course = input("\t\tCourses Opted: ")
                    fees_info = input("\t\tInformation About Fees: ")
                    award_finance = input("\t\tAwards & Financial Aid: ")
                    final_grades = input("\t\tFinal Grades: ")
                    student_number += 1
                    student_details = (student_number, first_name, middle_name, last_name, dob, gender, department, email, phone_number, address, emergency, opt_course, fees_info, award_finance, final_grades)
                    
                    save_details = input("\n\t\tSave Student Details? (Y/N) ")
                    if save_details == 'Y':
                        student_data.append(student_details)
                        student_details = []
                    elif save_details == 'N':
                        student_number -= 1
                        end_2 = True
                        break
                    
                    add_new_student = input("\n\t\tAdd More Students? (Y/N) ")
                    if add_new_student == 'Y':
                        continue
                    elif add_new_student == 'N':
                        end_2 = True
                        break
                
            elif ledger_menu == '2':
                if student_data:
                    print(table_of_data(student_data))
                    returnn = input("\t\t\t\tReturn to menu? (Y): ")
                    while returnn != 'Y':
                        returnn = input("\t\t\t\tReturn to menu? (Y): ")
                    end_2 = True
                    break
                else:
                    print("\n\t\t\t\tNo data available. Please add a new student.")
                    returnn = input("\t\t\t\tReturn to menu? (Y): ")
                    while returnn != 'Y':
                        returnn = input("\t\t\t\tReturn to menu? (Y): ")
                    end_2 = True
                    break
            
            elif ledger_menu == '3':

                user_search = input("\t\t\tSearch student databases for key words, numbers, or names. \n\t\t\t(\"exit\" to exit database search): ")
                if user_search == 'exit':
                    end_2 = True
                    break
                while not end_2:
                    specific_student = []
                    for student in student_data:
                        if user_search in str(student):
                            specific_student.append(student)
                    if specific_student:
                        print(table_of_data_specific(specific_student))
                    else:
                        print("\t\t\tNo Results")
                    user_search = input("\t\t\tSearch student databases for key words, numbers, or names. \n\t\t\t(\"exit\" to exit database search): ")
                    if user_search == 'exit':
                        end_2 = True
                        
                    

                    
                
            elif ledger_menu == '4':
                print("\n\t\t\t\tReturning to Login Page...\n\n\t\t\t\t\tAdmin Login Page")
                end_1 = True
                break
                
            else:
                print("\n\t\t\tError... Refer To One of The Menus Above.\n")  


# In[ ]:




