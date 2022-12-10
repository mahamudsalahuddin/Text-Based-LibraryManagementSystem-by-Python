import datetime
import os
os.getcwd()
#The os.getcwd() method is used to get the current working directory of a process.

class LMS:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id): {'books_title': line.replace("\n", ""), 'lender_name': '', 'lend_date': '', 'status': 'Available'}})
            id += 1

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books ID", "\t", "Title", "\t\t\t\t", "Status", "\t\t", "Lender Name", "\t\t", "Lending Date")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("status"), "]", "\t", value.get("lender_name"), "\t", value.get("lend_date"))

    def Issue_books(self):
        books_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == 'Available':
                print(
                    f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
                return self.lend_books()
            elif self.books_dict[books_id]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['lend_date'] = current_date
                self.books_dict[books_id]['status'] = 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter Books Title : ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 20:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict)) + 1): {'books_title': new_books, 'lender_name': '', 'lend_date': '', 'status': 'Available'}})
            print(f"The books '{new_books}' has been added successfully !!!")

    def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status'] = 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")



def commonF():
    try:
        mylms = LMS("list_of_books.txt", "Python")
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To Python's Library Management System---------\n")
            print("Press D To Display Books")
            print("Press I To Issue Books")
            print("Press A To Add Books")
            print("Press R To Return Books")
            print("Press Q To Quit")
            key_press = input("Press Key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.Issue_books()

            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books()

            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")

# =============================================== Code start from here ==============================================================
# ======================================= for Sign in ===============================================
print(f"\n----------Welcome To Python's Library Management System---------\n")
print("Enter 1 for sign in")
print("Enter 2 for sign up")
n = input("> ")
notFound = 0
if n == "1":
    print("=========================== SIGN IN =====================================")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("validation.txt", "r") as file:
        l = file.readlines()
    for line in l:
        lines = line.split()
        if lines[1] == password  and lines[0] == username:
            notFound=1
    if notFound == 0:
        print("Invalid Username or Password!")
    else:
        print("Successfully Login")
        commonF()

# =====================================For sign up=====================================================
elif n == "2":
    print("=========================== SIGN UP =====================================")
    username1 = input("Enter username: ")
    password1 = input("Enter password: ")
    with open("validation.txt", "a") as file:
        file.write("\n"+username1+"      "+password1)
    print("Successfully Created!!")

