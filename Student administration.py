# Python-Language-Projects
import csv

def write_into_csv(info_list):
    with open('student_information.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Name", "Age", "Contact Number","E-Mail ID"])

        writer.writerow(info_list)


condition = True

while(condition):
    student_info = input("Enter student information in the following format (Name Age Contact_Number E-mail_ID): ")

    print("Entered information: "+student_info)

    student_info_list = student_info.split(' ')
    print("Entered split up information is: " + str(student_info_list))
    
    write_into_csv(student_info_list)

    condition_check = input("Enter (yes/no) if you want to enter information for student: ")
    if condition_check == "yes":
        condition = True

    elif condition_check == "no":
        condition = False
    
#.................>>>>>>>>>>>>>>>>>>>>>>>>>>>>HAPPY CODING<<<<<<<<<<<<<<<<<<....................
