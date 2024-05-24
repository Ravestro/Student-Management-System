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