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
      