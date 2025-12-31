student_db = {
    101: {'name': 'vaibhav patil', 'course': 'data science', 'tfees': 40000, 'pfees': 30000, 'rfees': 10000}
}
course_fees = {'Data Science': 40000, 'Web Development': 30000, 'Aws': 20000, 'Testing': 15000}

admin_user = "admin"
admin_pass = "1234"

# LOGIN SYSTEM
while True:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == admin_user and password == admin_pass:
        print("\nLogin Successful!\n")
        break
    else:
        print("Invalid Username or Password! Try again\n")

print('The Kiran Academy'.center(100, '-'))

while True:
    # Inner loop to validate menu choice
    while True:
        print('''
        1. Add Student Data
        2. Display Student Data
        3. Update Student Data
        4. Delete Student Data    
        5. Filter Student Data
        6. Logout
        7. Change Admin Password
        ''')
        try:
            ch = int(input("Enter Your Choice (1–7): "))
            if 1 <= ch <= 7:
                break
            else:
                print("Invalid Choice! Please enter a number between 1 and 7.\n")
        except ValueError:
            print("Invalid Input! Please enter a valid number.\n")

    # MAIN MENU LOGIC
    if ch == 1:
        name = input("Name: ")
        courses = list(course_fees.keys())
        print('Available Courses: ')
        sr = 1
        for course in courses:
            print(f'{sr}. {course}')
            sr += 1
        ch1 = int(input("Select Your Course: "))
        if 1 <= ch1 <= len(courses):
            course = courses[ch1 - 1]
        else:
            print("Invalid Course Selection! Returning to main menu...\n")
            continue

        fees = course_fees[course]
        print(f'Fees for {course} is {fees}')
        dis = eval(input("Discount (%): "))
        tfees = fees - fees * dis / 100
        print(f'Fees after {dis}% discount is {tfees}')
        pfees = eval(input("Enter Paid Fees: "))
        rfees = tfees - pfees
        reg = len(student_db) + 101
        student_db[reg] = {'name': name, 'course': course, 'tfees': tfees, 'pfees': pfees, 'rfees': rfees}
        print("Added successfully....")

    elif ch == 2:
        if not student_db:
            print("No student data available.")
        else:
            print('-' * 125)
            print(f"|{'Reg No':^20}|{'StudentName':^20}|{'CourseName':^20}|{'TotalFees':^20}|{'PaidFees':^20}|{'RemainingFees':^20}|")
            print('-' * 125)
            for reg, s in student_db.items():
                print(f"|{reg:^20}|{s['name']:^20}|{s['course']:^20}|{s['tfees']:^20}|{s['pfees']:^20}|{s['rfees']:^20}|")
                print('-' * 125)

    elif ch == 3:
        reg = int(input("Reg No: "))
        if reg in student_db:
            print('''
                1. Name
                2. Fees
                3. Change Course
            ''')
            ch2 = int(input("Enter Your Choice: "))
            if ch2 == 1:
                uname = input('New Name: ')
                student_db[reg]['name'] = uname
                print('Updated successfully')
            elif ch2 == 2:
                print(f"Course Name: {student_db[reg]['course']} \nTotal Fees: {student_db[reg]['tfees']} \nPaid Fees: {student_db[reg]['pfees']} \nRemaining Fees: {student_db[reg]['rfees']}")
                fees = eval(input("Enter Amount to Pay: "))
                student_db[reg]['pfees'] += fees
                student_db[reg]['rfees'] -= fees
                print('Thank You, Payment Updated')
            elif ch2 == 3:
                new_course = input("Enter New Course: ")
                if new_course in course_fees:
                    student_db[reg]['course'] = new_course
                    student_db[reg]['tfees'] = course_fees[new_course]
                    print("Course updated successfully")
                else:
                    print("Invalid Course")
        else:
            print("Registration number not found.")

    elif ch == 4:
        reg = int(input("Reg no: "))
        if reg in student_db:
            student_db.pop(reg)
            print('Deleted successfully..')
        else:
            print('Invalid Registration Number')

    elif ch == 5:
        cname = input("Enter Course Name to Filter: ")
        found = False
        print('-' * 125)
        print(f"|{'Reg No':^20}|{'StudentName':^20}|{'CourseName':^20}|{'TotalFees':^20}|{'PaidFees':^20}|{'RemainingFees':^20}|")
        print('-' * 125)
        for reg, s in student_db.items():
            if s['course'].lower() == cname.lower():
                found = True
                print(f"|{reg:^20}|{s['name']:^20}|{s['course']:^20}|{s['tfees']:^20}|{s['pfees']:^20}|{s['rfees']:^20}|")
                print('-' * 125)
        if not found:
            print("No students found for this course.")

    elif ch == 6:
        print("Logging out... Goodbye!")
        break

    elif ch == 7:
        old_pass = input("Enter Old Password: ")
        if old_pass == admin_pass:
            new_pass = input("Enter New Password: ")
            admin_pass = new_pass
            print("Admin password changed successfully!")
        else:
            print("Incorrect old password!")
