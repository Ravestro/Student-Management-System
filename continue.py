def continue_function(cursor):
    while True:
        value = input("\n Do you wish to proceed: if yes type Y else type N: ")
        if value == 'Y':
            main_function(cursor)
        elif value == 'N':
            print("The program has ended. Thank you")
            exit()
 