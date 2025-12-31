student_db = {
    101: {'name': 'Vaibhav Patil', 'course': 'data science', 'tfees': 40000, 'pfees': 30000, 'rfees': 10000}
}

course_fees = {
    'data science': 40000,
    'web development': 30000,
    'AWS': 20000,
    'Testing': 15000
}

print("The Kiran Academy".center(100, '-'))

while True:
    print('''
    1. Add Student Data
    2. Display Student Data
    3. Update Student Data
    4. Delete Student Data
    5. Filter Student Data
    6. Logout
    ''')

    ch = input("Enter Your Choice : ")

    if ch == '1':
        name = input("Name : ")
        courses = list(course_fees.keys())
        sr = 1
        for course in courses:
            print(f'{sr}. {course}')
            sr += 1

        ch_course = int(input("Select Your Course : "))
        index = ch_course - 1
        course = courses[index]

        fees = course_fees[course]
        print(f'Fees for {course} is {fees}')

        dis = int(input("Discount (%): "))
        tfees = fees - fees * dis / 100
        print(f'Fees after {dis}% discount is {tfees}')

        pfees = int(input("Enter Paid Fees : "))
        rfees = tfees - pfees

        print(f'Total Fees : {tfees}\nPaid Fees : {pfees}\nRemaining Fees : {rfees}')

        reg = len(student_db) + 101
        student_db[reg] = {'name': name, 'course': course, 'tfees': tfees, 'pfees': pfees, 'rfees': rfees}
        print("Added Successfully......")

    elif ch == '2':
        print('-' * 125)
        print(f"| {'Reg No':^10} | {'Student Name':^20} | {'Course Name':^20} | {'Total Fees':^15} | {'Paid Fees':^15} | {'Remaining Fees':^15} |")
        print('-' * 125)
        for reg in student_db:
            data = student_db[reg]
            print(f"| {reg:^10} | {data['name']:^20} | {data['course']:^20} | {data['tfees']:^15} | {data['pfees']:^15} | {data['rfees']:^15} |")
        print('-' * 125)

    elif ch == '3':
        pass  # update (to be implemented later)

    elif ch == '4':
        pass  # delete (to be implemented later)

    elif ch == '5':
        pass  # filter (to be implemented later)

    elif ch == '6':
        break  # logout

    else:
        print("Invalid Choice! Please try again.")
