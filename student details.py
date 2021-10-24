import csv
def write_into_csv(info_list)
with open('student_info.csv', 'w+',newline='')as csv_file:
    writer = csv.writer(csv.file)
   if csv_file.tell() ==0:
       writer.writerow(["name","age","contact_no","email_id"])
    write.writerow(infor_list)
    
condition=true
if_name_=='_main_':
while(condition):
     student_info= input("enter some student information in the following format (name age contact_nunber email_id")
     print("entered information:" + student_info)
     
     student_info_list = student_info.split(' ')
     
     print("\n the entered information is-\nname: {}\nage: {}\ncontact_no: {}\memail_id: {}"
           .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3])) 
 choice_check = input("is the entered information correct?(yes/no):")
 ifchoice_check =="yes":
     write_into_csv(student_info_list)
     

condition_check= input("enter (yes/no) if you want to enter the information of another student")
if condition_check=="yes":
    condition=true
elif condition_check=="no":
        condition=false
elif choice_check=="no":
    print("re-enter the values")
