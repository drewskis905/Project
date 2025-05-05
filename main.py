# Author: Matthew Richardson
# Description: Programs allows you to add a task, remove, postpone, and see what task you have coming up.
# Date: 12/03/24
import tasklist
import check_input
def main_menu():
    #displays the main menu and returns the user’s valid input
    user_input = check_input.get_int_range("1. Display all task\n2. Display current task\n3. Add new task\n4. Mark current task complete\n5. Postpone current task\n6. Search tasks by date\n7. Save and quit\nEnter choice: ", 1, 7)
    print()
    return user_input

def get_date():
    #prompt user to enter month, day, and year and then returns it in the correct format
    month = ''
    day = ''
    year = ''
    print("Enter new due date: ")
    user_input = check_input.get_int_range("Enter month: ", 1, 12)
    if user_input < 10:
        month = '0' + str(user_input)
    else:
        month = str(user_input)
    user_input = check_input.get_int_range("Enter day: ", 1, 31)
    if user_input < 10:
        day = '0' + str(user_input)
    else:
        day = str(user_input)
    user_input = check_input.get_int_range("Enter year: ", 2000, 2100)
    year = str(user_input)
    return month + "/" + day + "/" + year

def get_time():
    #prompt user to enter hour and minutes then returns it in the correct format
    hour = ''
    minute = ''
    user_input = check_input.get_int_range("Enter hour: ", 0, 23)
    if user_input < 10:
        hour = '0' + str(user_input)
    else:
        hour = str(user_input)
    user_input = check_input.get_int_range("Enter minute: ", 0, 59)
    if user_input < 10:
        minute = '0' + str(user_input)
    else:
        minute = str(user_input)
    return hour + ":" + minute

def main():
    tlist = tasklist.Tasklist()
    i = True
    while i:
        print("-Tasklist-")
        print("You have " + str(len(tlist)) + " tasks.")
        user_input = main_menu()
        if user_input == 1:
            if len(tlist) == 0:
                print("All task are completed!\n")
            else:
                for count, t in enumerate(tlist, 1):
                    print(f"{count}. {t}")
                print()
        
        elif user_input == 2:
            if len(tlist) == 0:
                print("All task are completed!")
            else:
                print("Current task is:")
                print(tlist.get_current_task())
                print()
        
        elif user_input == 3:
            task_description = input("Enter a task: ")
            print("Enter due date: ")
            due_month = check_input.get_int_range("Enter month: ", 1, 12)
            due_day = check_input.get_int_range("Enter day: ", 1, 31)
            due_year = check_input.get_int_range("Enter year: ", 2000, 2100)
            print("Enter time: ")
            due_hour = check_input.get_int_range("Enter hour: ", 0, 23)
            due_minute = check_input.get_int_range("Enter minute: ", 0, 59)
            date = str(due_month) + "/" + str(due_day) + "/" + str(due_year)
            time = str(due_hour) + ":" + str(due_minute)
            tlist.add_task(task_description, date, time)
        
        
        elif user_input == 4:
            if len(tlist) == 0:
                print("All task are completed!")
            else:
                print(f"Marking current task complete:\n{tlist.get_current_task()}")
                tlist.mark_complete()
                print(f"New current task is:\n{tlist.get_current_task()}\n")
        
        elif user_input == 5:
            if len(tlist) == 0:
                print("All task are completed!")
            else:
                print(f"Postponing task:\n{tlist.get_current_task()}\n")
                tlist.postpone_task(get_date(), get_time())
                print()

        elif user_input == 6:
            if len(tlist) == 0:
                print("All task are completed!")
            else:
                print("Search by Date:")
                s_month = check_input.get_int_range("Enter month: ", 1, 12)
                s_day = check_input.get_int_range("Enter day: ", 1, 31)
                s_year = check_input.get_int_range("Enter year: ", 2000, 2100)
                s_date = str(s_month) + "/" + str(s_day) + "/" + str(s_year)
                for count, t in enumerate(tlist, 1):
                    if t.date == s_date:
                        print(f"{count}. {t.description}")
                    else:
                        print("Cannot find task with that date.")
                print()
        
        
        elif user_input == 7:
            tlist.save_file()
            print("Saving list...")
            i = False
main()