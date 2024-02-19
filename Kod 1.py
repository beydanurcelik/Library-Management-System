##Akbank & Global AI Hub Python Bootcamp Bitirme Projesi
##19/02/2024 - Beyda Nur Çelik
##
##Library Management System
##In this project you will be building “Library Management System” using object-oriented programming techniques. This program will use books.txt file that you will create as a database where each line will represent a single book. At each line, book name, author, release date and number of pages will be kept and separated with a comma.
##
##Proje için düzenlenen klasörlerin bilgileri:
##Kod dosyası: C:\Users\USER\Desktop\Python Bootcamp Projesi\Proje Kod Dosyasi\Kod 1.py
##Çalışma dosyası: C:\Users\USER\Desktop\Python Bootcamp Projesi\Proje Calismasi
##

##1. Adım / a. yönergesi

class Library:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.file = open(self.file_path, "a+")
        except FileNotFoundError:
            import os
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

##2. Adım / a. yönergesi

    def list_books(self):
            self.file.seek(0)  
            lines = self.file.read().splitlines()  
            for line in lines:
                book_info = line.split(",")
                book_name = book_info[0]
                author = book_info[1]
                print(f"{book_name}, {author}")

##2. Adım / b. yönergesi

    def add_book(self):
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            release_year = input("Enter release year: ")
            publisher = input ("Enter publisher: ")
            num_pages = input("Enter number of pages: ")
            category = input("Enter book category: ")
            language = input("Enter book language: ")

            book_info = f"{book_title},{book_author},{release_year},{num_pages},{category},{language}\n"
            self.file.write(book_info)
            print("Book added successfully!")

##2. Adım / c. yönergesi

    def remove_book(self):
            title_to_remove = input("Enter the title of the book to remove: ")
            self.file.seek(0)  
            lines = self.file.readlines()  

            updated_lines = [line for line in lines if not line.startswith(title_to_remove)]

            self.file.seek(0)
            self.file.truncate()

            self.file.writelines(updated_lines)
            print("Book removed successfully!")

##3. Adım / a. yönergesi

lib = Library("C:\\Users\\USER\\Desktop\\Python Bootcamp Projesi\\Proje Calismasi\\books.txt")

##4. Adım / a. yönergesi

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

##4. Adım / b. yönergesi

    choice = input("Enter your choice: ")

##4. Adım / c. yönergesi

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice.lower() == "q":
        break
    else:
        print("Invalid choice. Please try again.")
































