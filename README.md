Student Management System

This system helps users view, add, delete details of students and teachers. The system show the list of features availabe for users and upon clicking the feature, it navigates the user to the actionables in the corresponding feature.


The functions used to create database are:

1. insert_student: This function helps user add demographic and academic details of users to the database. It also checks if the entered student id is already present in the database and check whether mobile number and dates are in correct format

2. show_detail: This function helps to view student's and teacher's details when the corresponding id is entered. If id is not present in the database, it displays the same also.

3. update_detail: This function helps to update student's details like age,gender,year,address,college name 

4. delete_detail: This function helps to delete any student or teacher record upon entering the id

5. show_details: This function helps to print out the details of students(course,year,gender,student name) in the college upon entering the college name

6. change_course: This function allows user to assign course_id and course_startdate to student detail only if there are no current course and if the course_id is null for that student

7. current_course: This function helps user to know the current course pursured by any student.

8. update_course: This function allows user to update current course_id of student only if the student is a 1st year student and  pursuing any course currently.

9. add_teacher: This function helps user add demographic and academic details of teachers to the database. It also checks if the entered teacher id is already present in the database and check whether mobile number and dates are in correct format

10. update_detail_teacher: This function helps to update student's details like age,gender,address,college name 

11. delete_teacher_detail: The function helps the user to delete teacher record only if the teacher has worked more than 1 month.

12. show_teacher_details: This function helps to print out the details of teachers(gender,course,teacher name) in the college upon entering the college name

13. show_past_courses: This function allows the user to view only past courses of any teacher upon entering the teacher_id

14. export_student_data: This function exports all the student records of any particular college if the data's are present and it will be exported in the name of the college.

15. import_student_data: This function imports student data to the database if the student id doesn't exist in the database.

16. search_student_name: This function prints the details of all the students of the given name

17. search_course: This function allows the user to view details of all the students or teachers of the given name.

18. search_teacher_name: This  function prints the details of all the teachers of the given name

19. main_function: This function runs the total programme by getting details from the user and calling corresponding fucntions

20. continue_function: This function helps the programme to continue untile the user wishes to stop it.

Feedbacks:
creating modules: (requiremnts.txt,file for function definition)
Giving access to only teachers
Separate menu for students and teachers (Student, Teacher)
provision for user  to exit and go back to main menu
check if the course_id is a registered course or not
using doc string instead of comments for function def
readme formatting could be better (problem statement, Operating guidlines, Notes:)

