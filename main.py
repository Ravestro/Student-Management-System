#importing modules
import mysql.connector
import csv
import re
import pandas as pd

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


     



#Calling main function
if __name__ == '__main__':

    try:
        connection,cursor = database_connect()
        main_function(cursor)
        continue_function(cursor)

    except Exception as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()


