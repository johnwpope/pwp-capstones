class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
		
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("users: " + self.name +" email has been updated.")

    def __repr__(self):
        return "User: " + self.name + ", e-mail address: " + self.email + ", books read: " + str(self.books.value())

    def __eq__(self, other_user):
        if (self.name == other_user.name and self.email == other_user.email):
            return True
        else:
            return "User is not the same."
		   
    def read_book(self, book, rating):
        self.books[book] = rating
        return self.books
		
    def get_average_rating(self):
        average = 0
        for i in self.books:
            average += i.books.value
        average = average / (len(self.books) + 1)
        return average
	
		   
class Book:
   def __init__(self, title, isbn):
       self.title = title
       self.isbn = isbn
       self.ratings = []
		
   def get_title(self):
       return self.title

   def get_isbn(self):
       return self.isbn

   def set_isbn(self, new_isbn):
       self.isbn = new_isbn
       print("This book: " + self.title +" has had its ISBN updated")
       return self.isbn
	
   def add_ratings(self, rating):

       if (int(rating) >= 0 and int(rating) <= 4):
           self.ratings = int(rating)
       else:
           print("Invalid Rating")
	
   def __eq__(self, new_book):
       if (self.title == new_book.title and self.isbn == new_book.isbn):
           return True
       else:
           return "The books are not the same"
		   
   def get_average_rating(self):
       average = 0
       for i in self.ratings:
           average += i.ratings
		   
       average = average / (len(self.ratings) + 1)
       return average
		
   def __hash__(self):
       return hash((self.title, self.isbn))
		

		
class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
	    		
    def get_author(self):
        return self.author
		
    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
	
    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " on " + self.subject

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if self.users is None:
                print("No user with email ", email)
                #self.users.update({name, email})
        else:
            for i in self.users:
                if i == email:
                    User.read_book(self, book, rating)
                    #Book.add_ratings(self, rating)       
                else:
                    print("No user with email ", email)

        for i in self.books:
  
            if i == book:
                print(self.books[i])
        else:
            self.books[book] = 1

    def add_user(self, name, email, user_books = None):
        self.users[name] = email
        if user_books is not None:
            for i in user_books:
                self.add_book_to_user(self, i, email)
        return self

    def print_catalog(self):
        for i in self.books:
            print(i.title)
            
    def print_users(self):
        for i in self.users:
            print(i.user)

    def get_most_read_book(self):
        most_read = ""
        read_amount = 0
        for i in self.books:
            if len(i.ratings) >= read_amount:
                read_amount = len(i.ratings)
                most_read = i.title
        return most_read

    def highest_rated_book(self):
        highest_rated = ""
        highest_rating = 0
        for i in self.books:
            if i.get_average_rating() >= highest_rating:
                highest_rating = i.get_average_rating()
                highest_rated = i.title
        return highest_rated

    def most_positive_user(self):
        most_positive_value = 0
        hold = ""
        for i in self.users:
            if i.get_average_rating() >= most_positive_value:
                most_positive_value = i.get_average_rating()
                hold = i.title
        return hold
        
