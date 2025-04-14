# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"You are reading '{self.title}' by {self.author}.")

# Child class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def download(self):
        print(f"Downloading '{self.title}'... File size: {self.file_size}MB")

# Create objects
book1 = Book("Think Big", "Ben Carson")
ebook1 = EBook("Digital Minimalism", "Cal Newport", 3)

# Use methods
book1.read()
ebook1.read()
ebook1.download()



# Polymorphism
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

# Create objects
car = Car()
plane = Plane()

# Use method
car.move()
plane.move()


