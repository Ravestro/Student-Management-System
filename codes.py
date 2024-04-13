#importing modules
import mysql.connector
import csv
import re
import pandas as pd

#Defining function to add new student (such as name, age, parent’s detail, address, mobile number, gender, school details, etc)
def insert_student(cursor,table_name,column_names,values):
    try:
        columns = ', '.join(column_names)
        query = f'INSERT INTO {table_name} ({columns})  VALUES ({", ".join(["%s"]*len(column_names))})'
        cursor.execute(query, values)
        connection.commit()
        print("\n Added student details")
    except Exception as err:
        print(f"Error: {err}")
     

#Defining function to view student details
def show_detail(cursor,table_name,id,key):
     try:
         query = f"SELECT * FROM {table_name} where id = '{id}' "
         cursor.execute(query)
         result = cursor.fetchall()
         if result:
            for row in result:
                dictionary = dict(zip(key,row))
                for x,y in dictionary.items():
                    print(f"{x}:{y} \n",end = '')     
         else:
             print("\n Id not present in the database")
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to update student information (name can’t be updated)
def update_detail(cursor,table_name,id):
     try:
         query = f"SELECT student_name FROM {table_name} where id = '{id}'"
         cursor.execute(query)
         name = cursor.fetchall()
         print(name)
         choice = int(input('''
                 Do you want to change age? Press 1 \n 
                 Do you want to change guardian? Press 2 \n
                 Do you want to change year? Press 3 \n
                 Do you want to change address? Press 4 \n
                 Do you want to change gender? Press 5 \n 
                 Do you want to change mobile_number? Press 6 \n
                 Do you want to change college name? Press 7 
                '''))

         if choice == 1:
             age = input("Enter the age : ")
             query = f"update {table_name} set age = {age} where id = '{id}'"
             cursor.execute(query)

         elif choice == 2:
             guardian = input("Enter the guardian's name : ")
             query = f"update {table_name} set guardian = '{guardian}' where id = '{id}' "
             cursor.execute(query)

         elif choice == 3:
             year = input("Enter the year : ")
             query = f"update {table_name} set year = {year} where id = '{id}'"
             cursor.execute(query)

         elif choice == 4:
             address = input("Enter the address : ")
             query = f"update {table_name} set address = %s where id = %s "
             cursor.execute(query,(address,id))

         elif choice == 5:
             gender = input("Enter the gender : ")
             query = f"update {table_name} set gender = '{gender}' where id = '{id}' "
             cursor.execute(query)

         elif choice == 6:
             mobile_number = input("Enter the mobile number : ")
             query = f"update {table_name} set mobile number = {mobile_number} where id = '{id}'"
             cursor.execute(query)

         elif choice == 7:
             college_name = input("Enter the college name : ")
             query = f"update {table_name} set college_name = %s where id = %s "
             cursor.execute(query,(college_name,id))
         else:
             print("Invalid choice")

         connection.commit()
         if choice <= 7:
             print("Updated the details")
    
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to delete student record
def delete_detail(cursor,table_name,id):  
    try:
         query = f"select count(*) from {table_name} where id = '{id}' "
         cursor.execute(query)
         result = cursor.fetchall()
         if result:
             query = f"delete from {table_name} where id = '{id}' "
             cursor.execute(query)
             connection.commit()
             print("Deleted successfully")
         else:
             print("id not present")     
    except Exception as err:
        print(f"Error: {err}")
     

#Defining function to list all students in the college (on basis of Course, Year, Gender)
def show_details(cursor,table_name,college_name):
     try:
         query = f"SELECT course_name,year,gender,student_name FROM {table_name} a join course b on a.course_id = b.course_id where college_name = '{college_name}' order by course_name, year, gender"
         cursor.execute(query)
         result = cursor.fetchall()
         column_names = ['course name','year','gender','student name']
         df = pd.DataFrame(result,columns=column_names)
         print (df)
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to assign course to each student (one student can have only 1 course)
def change_course(cursor,table_name,id):  
    try:
         query = f"select count(*) from (select course_id, TIMESTAMPDIFF(MONTH, course_start_date, current_date()) as months from {table_name} where id = '{id}') a join course b on a.course_id = b.course_id and a.months <= b.course_duration"
         cursor.execute(query)
         result = cursor.fetchone()[0]
         if result:
             print("Already pursuing a course")
         else:
            query = f"select count(*) from {table_name} where id = '{id}' and course_id is null"
            cursor.execute(query)
            check = cursor.fetchone()[0]
            if check>=1:
                course_id = input('Enter the course_id: ')
                course_start_date = input("Enter course_start_date: ")
                query = f"update {table_name} set course_id = '{course_id}', course_start_date = '{course_start_date}' where id = '{id}' and course_id is null "
                cursor.execute(query)
                connection.commit()
                print("Course id changed")
            else:
                print("You cannot assign course to this student")         
    except Exception as err:
        print(f"Error: {err}")
     

#Defining function to view student's current course
def current_course(cursor,table_name,id):
     try:
         query = f"select course_name from (select course_id, TIMESTAMPDIFF(MONTH, course_start_date, current_date()) as months from {table_name} where id = '{id}') a join course b on a.course_id = b.course_id and a.months <= b.course_duration"
         cursor.execute(query)
         result = cursor.fetchall()
         print(result)
         if result:
             print(result)
         else:
            print("Not pursuing any course currently")
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to add new teacher
def add_teacher(cursor,table_name,column_name,values):
    try:
        columns = ', '.join(column_name)
        query = f'INSERT INTO {table_name} ({columns})  VALUES ({", ".join(["%s"]*len(column_name))})'
        cursor.execute(query, values)
        connection.commit()
        print("Added the teacher detail")
    except Exception as err:
        print(f"Error: {err}")
     

#Defining function to update teacher information (name can’t be updated)
def update_detail_teacher(cursor,table_name,id):
     try:
         query = f"SELECT teacher_name FROM {table_name} where id = '{id}'"
         cursor.execute(query)
         name = cursor.fetchall()
         choice = int(input('''
                 Do you want to change age? Press 1 \n
                 Do you want to change guardian? Press 2 \n
                 Do you want to change address? Press 3 \n
                 Do you want to change gender? Press 4 \n
                 Do you want to change mobile_number? Press 5 \n
                 Do you want to change college name? Press 6
                '''))
                
         if choice == 1:
             age = input("Enter the age : ")
             query = f"update {table_name} set age = {age} where id = '{id}'"
             cursor.execute(query)

         elif choice == 2:
             guardian = input("Enter the guardian's name : ")
             query = f"update {table_name} set guardian = '{guardian}' where id = '{id}' "
             cursor.execute(query)

         elif choice == 3:
             address = input("Enter the address : ")
             query = f"update {table_name} set address = %s where id = %s "
             cursor.execute(query,(address,id))

         elif choice == 4:
             gender = input("Enter the gender : ")
             query = f"update {table_name} set gender = '{gender}' where id = '{id}' "
             cursor.execute(query)

         elif choice == 5:
             mobile_number = input("Enter the mobile number : ")
             query = f"update {table_name} set mobile number = {mobile_number} where id = '{id}'"
             cursor.execute(query)

         elif choice == 6:
             college_name = input("Enter the college name : ")
             query = f"update {table_name} set college_name = %s where id = %s "
             cursor.execute(query,(college_name,id))

         else:
             print("\n Invalid choice")

         connection.commit()
         if choice <= 6:
             print("\n Updated the details")
    
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to update student's current course (Only for 1st year students)
def update_course(cursor,table_name,id):
     try:
         query = f"SELECT year FROM {table_name} where id = '{id}'"
         cursor.execute(query)
         year = cursor.fetchone()[0]
         print(year)
         if year == "1st Year":
              query = f"select course_name from (select course_id, TIMESTAMPDIFF(MONTH, course_start_date, current_date()) as months from {table_name} where id = '{id}') a join course b on a.course_id = b.course_id and a.months <= b.course_duration"
              cursor.execute(query)
              result = cursor.fetchall()
              if result:     
                course_id = input ("Enter the new course id: ")
                query = f"update {table_name} set course_id = '{course_id}' where id = '{id}' and course_start_date = (select max(course_start_date) from {table_name} where id = '{id}')"
                cursor.execute(query)
                connection.commit()
                print("\n Updated the course id")
              else:
                  print("\n Not pursuing any course")
         else :
             print("\n Student is not from 1st year")
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to delete teacher record (to check only if she/he has worked more than 1 Month) (Soft delete)
def delete_teacher_detail(cursor,table_name,id):  
    try:
         query = f"select * from {table_name} where id = '{id}'"
         cursor.execute(query)
         result = cursor.fetchall()
         if result:
             query = f"delete from {table_name} where id = '{id}' and (CURRENT_DATE() - INTERVAL '1' MONTH > starting_date)"
             cursor.execute(query)
             query = f"select * from {table_name} where id = '{id}' and (CURRENT_DATE() - INTERVAL '1' MONTH > starting_date)"
             cursor.execute(query)
             check =  cursor.fetchall()
             if check:
                print ("Teacher hasn't worked more than 1 month")
             else:
                print('Deleted')
                connection.commit()
                
         else:
             print("Teacher detail not present")     
          
    except Exception as err:
        print(f"Error: {err}")
     

#Defining function to list all teachers (separated by gender & course they teach)
def show_teacher_details(cursor,table_name):
     try:
         query = f"SELECT gender,course_name,teacher_name FROM {table_name} a join course b on a.course_id = b.course_id order by gender,course_name"
         cursor.execute(query)
         result = cursor.fetchall()
         column_names = ['gender','course name','teacher name']
         df = pd.DataFrame(result,columns=column_names)
         print (df)
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to view teacher's and student's past courses (One teacher should at least teach 2 distinct courses)
def show_past_courses(cursor,table_name,id):
     try:
         query = f"select distinct course_name from (select course_id, TIMESTAMPDIFF(MONTH, course_start_date, current_date()) as months from {table_name} where id = '{id}') a join course b on a.course_id = b.course_id and a.months >= b.course_duration"
         cursor.execute(query)
         result = cursor.fetchall()
         if result:
             for x in result:
                print("\n")
                print(x[0])
         else:
             print("\n No past course")
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to export student data to a CSV file
def export_student_data(cursor,table_name,college_name):
     try:
         query = f"SELECT * FROM {table_name} where college_name = '{college_name}' "
         cursor.execute(query)
         result = cursor.fetchall()
         
         if result:
                file_name = college_name + '.csv'
                try:
                    with open(file_name,'w',newline='') as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow([i[0] for i in cursor.description])
                        csv_writer.writerows(result)
                        print("Exporting complete")
                except Exception as err:
                    print(f"Error: {err}")
         else:
                   print("\n Enter valid college name")
                   college_name = input("Enter the college name whose student data has to be exported: ")
                   export_student_data(cursor,table_name,college_name)

         
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to import student data from a CSV file
def import_student_data(cursor,table_name,student_file):
     try:
         try:
             with open(student_file,'r',newline='') as f:
                csv_reader = csv.reader(f)
                next(csv_reader) 
                count = 0
                for row in csv_reader:
                  student_id = row[0]
                  query = f'select count(*) from {table_name} where id = %s'
                  cursor.execute(query,(student_id,))
                  check = cursor.fetchone()[0]
                  if check >=1:
                      print(f"{student_id} data already present")
                  else:
                    query = f'INSERT INTO {table_name} VALUES ({", ".join(["%s"]*len(row))})'
                    cursor.execute(query, row)
                    count+=1
                connection.commit()
                if count >= 1:
                    print(f"\n Student data imported from {student_file} successfully.")
                else:
                    print("\n File not imported")
                 
         except Exception as err:
             print(f"Error: {err}")
             connection.rollback()
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to search student by name
def search_student_name(cursor,table_name,student_name,key):
     try:
         query = f"SELECT * FROM {table_name} where student_name = '{student_name}'"
         cursor.execute(query)
         result = cursor.fetchall()
         df = pd.DataFrame(result,columns=key)
         print(df)
         
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to search student by course
def search_course(cursor,table_name,course_name,key):
     try:
         query = f"SELECT a.* FROM {table_name} a join course b on a.course_id = b.course_id where course_name = '{course_name}'"
         cursor.execute(query)
         result = cursor.fetchall()
         df = pd.DataFrame(result,columns=key)
         print(df)
     except Exception as err:
        print(f"Error: {err}")
      

#Defining function to search teacher by name
def search_teacher_name(cursor,table_name,teacher_name,key):
     try:
         query = f"SELECT * FROM {table_name} where teacher_name = '{teacher_name}'"
         cursor.execute(query)
         result = cursor.fetchall()
         df = pd.DataFrame(result,columns=key)
         print(df)
     except Exception as err:
        print(f"Error: {err}")

def main_function(cursor):
    #Taking input
        flag = int(input ('''
                        Do you want to add new student? Press 1 \n
                        Do you want to view student details? Press 2 \n
                        Do you want to update student information? Press 3 \n
                        Do you want to delete student record? Press 4 \n
                        Do you want to list all students in the college? Press 5 \n
                        Do you want to assign course to each student (one student can have only 1 course? Press 6 \n
                        Do you want to view student's current course? Press 7 \n
                        Do you want to update student's current course (Only for 1st year students)? Press 8 \n
                        Do you want to view student's past courses (to check if the student has changed the course or is it same.) Press 9 \n
                        Do you want to add new teacher? Press 10 \n
                        Do you want to view teacher details ? Press 11 \n
                        Do you want to update teacher information? Press 12 \n
                        Do you want to delete teacher record (to check only if she/he has worked more than 1 Month)? Press 13 \n
                        Do you want to list all teachers? Press 14 \n
                        Do you want to view teacher's past courses (One teacher should at least teach 2 distinct courses)? Press 15 \n
                        Do you want to Export student data to a CSV file? Press 16 \n
                        Do you want to import student data from a CSV file? Press 17 \n
                        Do you want to search student by name ? Press 18 \n
                        Do you want to search student by course? Press 19 \n
                        Do you want to Search teacher by name? Press 20 \n
                        Do you want to search teacher by course? Press 21 \n 
                    '''))

        #Assigning columns for student and teacher tables
        student_header = ['id','student_name','age','guardian','address','gender','mobile_number','college_name','branch','year','course_id','course_start_date','starting_date']
        teacher_header = ['id','teacher_name','age','guardian','address','gender','mobile_number','college_name','course_id','course_start_date','starting_date']


        # To add new student (such as name, age, parent’s detail, address, mobile number, gender, school details, etc)
        if flag ==1 :
            try:
                while True:
                    id = input('Enter the student id: ')
                    query = f"SELECT * FROM student WHERE id = '{id}'"
                    cursor.execute(query)
                    result = cursor.fetchone()
                    if result is not None:
                        print("Student id already exists. Please enter another id.")
                    else:
                        break

                student_name= input('Enter the student name: ')
                age = input('Enter the age: ')
                guardian = input('Enter the guardian: ')
                address = input('Enter the address: ')
                gender = input('Enter the gender (Male or Female): ')
                while True:
                    mobile_number = int(input('Enter the mobile number: '))
                    if len(str(mobile_number))!=10 or str(mobile_number)[0]!= '9':
                         print('Please re-enter the mobile number(10 digits starting with 9): ')
                    else:
                        break
                college_name = input('Enter the college name: ')
                year = input('Enter the year: ')
                branch = input('Enter the branch in capital: ')
                course_id = input('Enter the course id:  ')
                while True:
                    pattern = r'^\d{4}/\d{2}/\d{2}$'
                    course_start_date = input('Enter the course start date (YYYY/MM/DD): ')
                    if not bool(re.match(pattern, course_start_date)):
                         print('\n Please re-enter in (YYYY/MM/DD) format')
                    else:
                        break
                while True:
                    pattern = r'^\d{4}/\d{2}/\d{2}$'
                    starting_date = input('Enter the start date (YYYY/MM/DD): ')
                    if not bool(re.match(pattern, starting_date)):
                        print('\n Please re-enter in (YYYY/MM/DD) format')
                    else:
                        break

                values = [id,student_name,age,guardian,address,gender,mobile_number,college_name,year,branch,course_id,course_start_date,starting_date]
                insert_student(cursor,'student',student_header,values)
            except Exception as err:
                print(f"Error: {err}")

        #To view student details
        elif flag == 2:
            try:
                id = input('Enter the student id: ')
                show_detail(cursor,'student',id,student_header)
            except Exception as err:
                print(f"Error: {err}")

        #Update student information (name can’t be updated)
        elif flag == 3:
            try:
                id = input('Enter the student id: ')
                update_detail(cursor,'student',id)
            except Exception as err:
                print(f"Error: {err}")

        # Delete student record 
        elif flag == 4:
            try:
                id = input('Enter the student id: ')
                delete_detail(cursor,'student',id)
            except Exception as err:
                print(f"Error: {err}")

        # List all students in the college (on basis of Course, Year, Gender)
        elif flag == 5:
            try:
                college_name = input('Enter the college name: ')
                show_details(cursor,'student',college_name)
            except Exception as err:
                print(f"Error: {err}")

        # Assign course to each student (one student can have only 1 course)
        elif flag == 6:
            try:
                id = input('Enter the student id: ')
                change_course(cursor,'student',id)
            except Exception as err:
                print(f"Error: {err}")

        # View student's current course
        elif flag == 7:
            try:
                id = input('Enter the student id: ')
                current_course(cursor,'student',id)
            except Exception as err:
                print(f"Error: {err}")

        # Update student's current course (Only for 1st year students)
        elif flag == 8:
            try:
                id = input('Enter the student id (only 1st years): ')
                update_course(cursor,'student',id)
            except Exception as err:
                print(f"Error: {err}")

        # View student's past courses 
        elif flag == 9:
            try:
                id = input('Enter the student id: ')
                show_past_courses(cursor,'student',id)
            except Exception as err:
                print(f"Error: {err}")
                
        # Add new teacher
        elif flag == 10:
            try:
                while True:
                    id = input('Enter the teacher id: ')
                    query = f"SELECT * FROM teacher WHERE id = '{id}'"
                    cursor.execute(query)
                    result = cursor.fetchone()
                    if result is not None:
                        print("Teacher id already exists. Please enter another id.")
                    else:
                        break
                
                teacher_name= input('Enter the teacher name: ')
                age = input('Enter the age: ')
                guardian = input('Enter the guardian: ')
                address = input('Enter the address: ')
                gender = input('Enter the gender: ')
                while True:
                    mobile_number = int(input('Enter the mobile number: '))
                    if len(str(mobile_number))!=10 or str(mobile_number)[0]!= '9':
                         print('\n Please re-enter the mobile number(10 digits starting with 9): ')
                    else:
                        break
                college_name = input('Enter the college name: ')
                while True:
                    pattern = r'^\d{4}/\d{2}/\d{2}$'
                    starting_date = input('Enter the start date (YYYY/MM/DD): ')
                    if not bool(re.match(pattern, starting_date)):
                        print('\n Please re-enter in (YYYY/MM/DD) format: ')
                    else:
                        break         
                while True:
                    courses = int(input('Enter the number of courses(atleast 2): '))
                    if courses >=2:
                        break

                for i in range(int(courses)):
                    course_id = input('Enter the course_id: ')
                    while True:
                        pattern = r'^\d{4}/\d{2}/\d{2}$'
                        course_start_date = input('Enter the course start date (YYYY/MM/DD): ')
                        if not bool(re.match(pattern, course_start_date)):
                            print('\n Please re-enter in (YYYY/MM/DD) format')
                        else:
                            break
                    values = [id,teacher_name,age,guardian,address,gender,mobile_number,college_name,course_id,course_start_date,starting_date]
                    add_teacher(cursor,'teacher',teacher_header,values)  
            except Exception as err:
                print(f"Error: {err}")

        # View teacher details (such as name, address, mobile number, gender, course he/she can teach, etc)
        elif flag == 11:
            try:
                id = input('Enter the teacher id: ')
                show_detail(cursor,'teacher',id,teacher_header)
            except Exception as err:
                print(f"Error: {err}")

        # Update teacher information (name can’t be updated)
        elif flag == 12:
            try:
                id = input('Enter the teacher id: ')
                update_detail_teacher(cursor,'teacher',id)
            except Exception as err:
                print(f"Error: {err}")

        # Delete teacher record (to check only if she/he has worked more than 1 Month) 
        elif flag == 13:
            try:
                id = input('Enter the teacher id: ')
                delete_teacher_detail(cursor,'teacher',id)
            except Exception as err:
                print(f"Error: {err}")

        # List all teachers (separated by gender & course they teach)
        elif flag == 14:
            try:
                show_teacher_details(cursor,'teacher')
            except Exception as err:
                print(f"Error: {err}")

        # View teacher's past courses (One teacher should at least teach 2 distinct courses)
        elif flag == 15:
            try:
                id = input ("Enter teacher's id: ")
                show_past_courses(cursor,'teacher',id)
            except Exception as err:
                print(f"Error: {err}")

        # Export student data to a CSV file
        elif flag == 16:
            try:
                college_name = input("Enter the college name whose student data has to be exported: ")
                export_student_data(cursor,'student',college_name)
            except Exception as err:
                print(f"Error: {err}")

        # Import student data from a CSV file
        elif flag == 17:
            try:
                file_name = input("Enter the csv file name to be imported: ")
                import_student_data(cursor,'student',file_name)
            except Exception as err:
                print(f"Error: {err}")

        # Search student by name
        elif flag == 18:
            try:
                student_name = input("Enter the student name: ")
                search_student_name(cursor,'student',student_name,student_header)
            except Exception as err:
                print(f"Error: {err}")

        # Search student by course
        elif flag == 19:
            try:
                course_name = input("Enter the course name: ")
                search_course(cursor,'student',course_name,student_header)
            except Exception as err:
                print(f"Error: {err}")

        # Search teacher by name
        elif flag == 20:
            try:
                teacher_name = input("Enter the teacher name: ")
                search_teacher_name(cursor,'teacher',teacher_name,teacher_header)
            except Exception as err:
                print(f"Error: {err}")

        # Search teacher by course
        elif flag == 21:
            try:
                course_name = input("Enter the course name: ")
                search_course(cursor,'teacher',course_name,teacher_header)
            except Exception as err:
                print(f"Error: {err}")

        else:
            print("Invalid number")


def continue_function(cursor):
    while True:
        value = input("\n Do you wish to proceed: if yes type Y else type N: ")
        if value == 'Y':
            main_function(cursor)
        elif value == 'N':
            print("The program has ended. Thank you")
            exit()
      

# Connecting to database
try:
    connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Raveen123$',
            database = 'Student Management System'
        )
    cursor = connection.cursor()
    print("\n Connected to database")

#Calling main function
    
    main_function(cursor)
    continue_function(cursor)

except Exception as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    connection.close()


