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