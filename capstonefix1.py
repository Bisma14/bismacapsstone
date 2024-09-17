from datetime import datetime, timedelta
from tabulate import tabulate

# Books dummy data
books = [
    {"ID": 1, "title": "Introduction to Python", "genre": "Education", "stock": 10, "publication_year": 2021, "author": "John Doe","fine_per_day": 2.0},
    {"ID": 2, "title": "Data Science Handbook", "genre": "Education", "stock": 7, "publication_year": 2020, "author": "Jane Smith","fine_per_day": 2.0},
    {"ID": 3, "title": "Mysteries of the Universe", "genre": "Science", "stock": 5, "publication_year": 2022, "author": "Albert Einstein","fine_per_day": 2.0},
    {"ID": 4, "title": "The Great Novel", "genre": "Fiction", "stock": 4, "publication_year": 2019, "author": "Mark Twain","fine_per_day": 2.0},
    {"ID": 5, "title": "Ancient Civilizations", "genre": "History", "stock": 8, "publication_year": 2018, "author": "Stephen Hawking","fine_per_day": 2.0},
    {"ID": 6, "title": "Ethics in Modern Times", "genre": "Philosophy", "stock": 3, "publication_year": 2023, "author": "Aristotle","fine_per_day": 2.0},
    {"ID": 7, "title": "Physics Fundamentals", "genre": "Science", "stock": 6, "publication_year": 2021, "author": "Isaac Newton","fine_per_day": 2.0},
    {"ID": 8, "title": "Advanced AI Techniques", "genre": "Education", "stock": 5, "publication_year": 2022, "author": "Alan Turing","fine_per_day": 2.0},
    {"ID": 9, "title": "World War II", "genre": "History", "stock": 9, "publication_year": 2017, "author": "Winston Churchill","fine_per_day": 2.0},
    {"ID": 10, "title": "Quantum Computing", "genre": "Science", "stock": 7, "publication_year": 2020, "author": "Richard Feynman","fine_per_day": 2.0},
    {"ID": 11, "title": "The Art of Literature", "genre": "Fiction", "stock": 6, "publication_year": 2024, "author": "Jane Austen","fine_per_day": 2.0},
    {"ID": 12, "title": "Basic Philosophy", "genre": "Philosophy", "stock": 4, "publication_year": 2022, "author": "Socrates","fine_per_day": 2.0},
    {"ID": 13, "title": "Climate Change Impacts", "genre": "Science", "stock": 8, "publication_year": 2023, "author": "Rachel Carson","fine_per_day": 2.0},
    {"ID": 14, "title": "Moral Dilemmas", "genre": "Philosophy", "stock": 2, "publication_year": 2021, "author": "Immanuel Kant","fine_per_day": 2.0},
    {"ID": 15, "title": "Global History", "genre": "History", "stock": 5, "publication_year": 2019, "author": "Howard Zinn","fine_per_day": 2.0}
]
# Genre buku yang tersedia di perpustakaan
genres_book = ["Education","Science","History","Philosophy","Fiction"]

# Data dummy untuk peminjam buku perpustakaan
users = {
    "user1": {
        "borrowed_books": [
            {"ID": 1, "borrow_date": datetime(2024, 7, 10), "return_date": None, "deadline_date": datetime(2024, 7, 17)},
            {"ID": 4, "borrow_date": datetime(2024, 8, 15), "return_date": None, "deadline_date": datetime(2024, 8, 22)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "user2": {
        "borrowed_books": [
            {"ID": 2, "borrow_date": datetime(2024, 8, 5), "return_date": None, "deadline_date": datetime(2024, 8, 12)},
            {"ID": 8, "borrow_date": datetime(2024, 9, 1), "return_date": None, "deadline_date": datetime(2024, 9, 8)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "user3": {
        "borrowed_books": [
            {"ID": 3, "borrow_date": datetime(2024, 9, 1), "return_date": None, "deadline_date": datetime(2024, 9, 8)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "user4": {
        "borrowed_books": [
            {"ID": 5, "borrow_date": datetime(2024, 8, 10), "return_date": None, "deadline_date": datetime(2024, 8, 17)},
            {"ID": 7, "borrow_date": datetime(2024, 8, 20), "return_date": None, "deadline_date": datetime(2024, 8, 27)}
        ],
        "total_fine": 0.0,
        "payments": []
    },
    "user5": {
        "borrowed_books": [
            {"ID": 6, "borrow_date": datetime(2024, 9, 5), "return_date": None, "deadline_date": datetime(2024, 9, 12)},
            {"ID": 10, "borrow_date": datetime(2024, 9, 10), "return_date": None, "deadline_date": datetime(2024, 9, 17)}
        ],
        "total_fine": 0.0,
        "payments": []
    }
}

admin_staff = {
    "admin1": {
        "username": "admin1",
        "password": "123"
    },
    "admin2": {
        "username": "admin2",
        "password": "123"
    }
}

# Function to view available books (READ)
def view_available_books():
    headers = ["ID", "Title", "Genre", "Publication Year", "Author","Stock"]
    table = []
    for book in books:
        if book['stock'] > 0:
            table.append([book["ID"], book["title"], book["genre"], book["publication_year"], book["author"],book["stock"]])
    return tabulate(table, headers, tablefmt="grid")

# Function to add a new book and validate genre input
def validate_genre_input(genre):
    if genre.capitalize() not in genres_book:
        return f"Error: Invalid genre '{genre}'. Please select a valid genre from {genres_book}."
    return None

# Function to add a new book
def add_book(title, genre, stock, publication_year, author):
    # Validation of genre
    genre_error = validate_genre_input(genre)
    if genre_error:
        return genre_error

    current_year = 2024
    if publication_year > current_year:
        return f"Error: Publication year must be less than or equal to {current_year}."
    # Checking if there are any books in the list
    if books:
    # Create a list of all 'ID' fields from the 'books' list
        ids = []
        for book in books:
            ids.append(book['ID'])
        
        # Find the maximum 'ID' in the list of IDs
        max_id = max(ids)
        
        # Increment the maximum 'ID' by 1 to generate the new 'ID'
        new_id = max_id + 1
    else:
        # If there are no books, the new 'ID' will start at 1
        new_id = 1

    books.append({
        "ID": new_id,
        "title": title,
        "genre": genre.capitalize(),
        "stock": stock,
        "publication_year": publication_year,
        "author": author
    })
    return f"Book '{title}' added successfully with ID {new_id}."

# Function to update book stock
def update_book_stock(book_id, stock_change):
    if not isinstance(stock_change, int):
        return "Invalid input. Please enter a valid integer."
    
    for book in books:
        if book['ID'] == book_id:
            book["stock"] += stock_change
            return f"Stock updated for book ID {book_id}. New stock: {book['stock']}."
    
    return "Book not found."

# Function to delete a book
def delete_book(book_id):
    # Declare 'books' as a global variable so we can modify it
    global books

    # Initialize a new list to hold the books that are not deleted
    new_books = []

    # Iterate through the list of books
    for book in books:
        # Check if the current book's ID matches the book_id to be deleted
        if book["ID"] != book_id:
            # If it doesn't match, add the book to the new_books list
            new_books.append(book)

    # Check if the length of new_books is different from the original books list
    # This indicates whether a book was deleted or not
    if len(new_books) != len(books):
        # If a book was deleted, update the global 'books' list
        books = new_books
        return f"Book with ID {book_id} deleted successfully."
    else:
        # If no book was deleted, return a message saying the book wasn't found
        return "Book not found."


# Function to view borrowed books status for all users
def view_borrowed_books_status():
    # Define the headers for the table
    headers = ["Username", "Book ID", "Title", "Borrow Date", "Deadline Date", "Return Date", "Status", "Fine"]
    table = []

    # Iterate over all users
    for username, user in users.items():
        # Iterate over all books borrowed by the current user
        for borrowed in user["borrowed_books"]:
            # Find the corresponding book in the books list
            book = None
            for b in books:
                if b["ID"] == borrowed["ID"]:
                    book = b
                    break

            if book is not None:
                # Gather details about the borrowed book
                book_title = book["title"]
                borrow_date = borrowed["borrow_date"].strftime("%Y-%m-%d")
                deadline_date = borrowed["deadline_date"].strftime("%Y-%m-%d")
                return_date = borrowed["return_date"].strftime("%Y-%m-%d") if borrowed["return_date"] else "Not Returned"

                # Initialize fine and status variables
                fine = 0.0
                status = "Not Returned"

                # Determine the status of the book
                if borrowed["return_date"]:
                    status = "Returned"
                elif datetime.now() > borrowed["deadline_date"]:
                    overdue_days = (datetime.now() - borrowed["deadline_date"]).days
                    fine_per_day = book.get("fine_per_day", 0.0)
                    fine = overdue_days * fine_per_day

                # Add the data to the table
                table.append([username, borrowed["ID"], book_title, borrow_date, deadline_date, return_date, status, f"${fine:.2f}"])

    # Return the formatted table
    return tabulate(table, headers, tablefmt="grid")



# Function to borrow or return a book
def borrow_or_return_book(username, book_id, return_book=False):
    # Fetch the user object
    user = users.get(username)
    if not user:
        return "User not found."

    # Find the book in the list of books by its ID
    book = None
    for b in books:
        if b["ID"] == book_id:
            book = b
            break

    if not book:
        return "Book not found."

    if return_book:
        # Find the borrowed book in the user's borrowed books list
        borrowed_book = None
        for b in user["borrowed_books"]:
            if b["ID"] == book_id and b["return_date"] is None:
                borrowed_book = b
                break

        if not borrowed_book:
            return "This book was not borrowed or is already returned."

        # Update the return date and increment the stock
        borrowed_book["return_date"] = datetime.now()
        book["stock"] += 1

        # Calculate any fines
        fine = 0.0
        if borrowed_book["return_date"] > borrowed_book["deadline_date"]:
            overdue_days = (borrowed_book["return_date"] - borrowed_book["deadline_date"]).days
            fine = overdue_days * book.get("fine_per_day", 0.0)

        if fine > 0:
            user["total_fine"] += fine
            return f"Book returned successfully. You have a fine of IDR {fine:.2f} for this book. Please pay the fine."
        else:
            return "Book returned successfully. No fine due."

    else:
        # Check if the user has any outstanding fines
        if has_outstanding_fines(user):
            return "You have outstanding fines. Please pay your fines before borrowing more books."

        # Check if the book is available in stock
        if book["stock"] <= 0:
            return "Book is not available."

        # Check if the user already borrowed the book
        for borrowed in user["borrowed_books"]:
            if borrowed["ID"] == book_id and borrowed["return_date"] is None:
                return "You already borrowed this book and have not returned it yet."

        # Add the borrowed book to the user's list
        user["borrowed_books"].append({
            "ID": book_id,
            "borrow_date": datetime.now(),
            "return_date": None,
            "deadline_date": datetime.now() + timedelta(days=7)
        })
        book["stock"] -= 1

        return "Book borrowed successfully."


# Function to search books by genre
def search_books_by_genre(genre):
    # Validate if the genre is available in the predefined genres list
    genre = genre.capitalize()
    if genre not in genres_book:
        return "Invalid genre. Please choose from the available genres: " + ', '.join(genres_book)
    
    headers = ["ID", "Title", "Genre", "Stock", "Publication Year", "Author"]
    table = []
    for book in books:
        if book["genre"].lower() == genre.lower():
            table.append([book["ID"], book["title"], book["genre"], book["stock"], book["publication_year"], book["author"]])
    
    if len(table) == 0:
        return "No books found for the specified genre."
    
    return tabulate(table, headers, tablefmt="grid")

# Function to check if user has any outstanding fines for any book
def has_outstanding_fines(user):
    # Iterate over all books borrowed by the user
    for borrowed in user["borrowed_books"]:
        # Check if the book has not been returned and is overdue
        if borrowed["return_date"] is None:
            current_date = datetime.now()
            deadline_date = borrowed["deadline_date"]

            # Check if the current date is after the deadline date
            if current_date > deadline_date:
                # Calculate the number of overdue days
                overdue_days = (current_date - deadline_date).days

                # Find the corresponding book in the books list
                book = None
                for b in books:
                    if b["ID"] == borrowed["ID"]:
                        book = b
                        break

                # If the book is found, calculate the fine
                if book is not None:
                    fine_per_day = book.get("fine_per_day", 0.0)
                    fine = overdue_days * fine_per_day

                    # If there is a fine, return True (indicating outstanding fines)
                    if fine > 0:
                        return True

    # If no outstanding fines were found, return False
    return False


# Function to handle fine payment
def handle_fine_payment(username, amount):
    user = users.get(username)
    if not user:
        return "User not found."
    
    if amount > user["total_fine"]:
        return f"Error: Payment exceeds total fine amount. Your total fine is IDR {user['total_fine']:.2f}."

    user["total_fine"] -= amount
    user["payments"].append({
        "amount": amount,
        "date": datetime.now()
    })
    
    if user["total_fine"] == 0:
        return "Fine fully settled. Thank you for your payment."
    else:
        return f"Fine partially settled. Remaining fine: IDR {user['total_fine']:.2f}."

# Function to validate year input
def get_valid_year(prompt):
    while True:
        try:
            year = int(input(prompt))
            return year
        except ValueError:
            print("Invalid year. Please enter a valid integer.")

# Function to get integer input with error handling
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Login as Admin")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username in admin_staff and admin_staff[username]["password"] == password:
                print("Admin login successful.")
                admin_menu()
            else:
                print("Invalid username or password. Try again.")
        
        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Admin menu to manage books and users
def admin_menu():
    while True:
        try:
            print("\n=== Admin Menu ===")
            print("1. View Available Books")
            print("2. Add Book")
            print("3. Update Book Stock")
            print("4. Delete Book")
            print("5. View Borrowed Books Status")
            print("6. Borrow or Return Book")
            print("7. Search Book by Genre")
            print("8. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print("\nAvailable Books:")
                print(view_available_books())

            elif choice == "2":
                title = input("Enter book title: ").strip()
                genre = input(f"Enter book genre ({', '.join(genres_book)}): ").strip()
                stock = get_int_input("Enter book stock: ")
                publication_year = get_valid_year("Enter publication year: ")
                author = input("Enter author name: ").strip()
                result = add_book(title, genre, stock, publication_year, author)
                print(result)

            elif choice == "3":
                book_id = get_int_input("Enter book ID to update stock: ")
                stock_change = get_int_input("Enter stock change (positive to increase, negative to decrease): ")
                print(update_book_stock(book_id, stock_change))

            elif choice == "4":
                book_id = get_int_input("Enter book ID to delete: ")
                print(delete_book(book_id))

            elif choice == "5":
                print("\nBorrowed Books Status:")
                print(view_borrowed_books_status())

            elif choice == "6":
                username = input("Enter username: ").strip()
                book_id = get_int_input("Enter book ID: ")
                action = input("Type 'borrow' to borrow or 'return' to return: ").strip().lower()
                if action == "borrow":
                    print(borrow_or_return_book(username, book_id))
                elif action == "return":
                    result = borrow_or_return_book(username, book_id, return_book=True)
                    print(result)
                    if "fine" in result:
                        while True:
                            amount = float(input("Enter amount to pay: "))
                            payment_result = handle_fine_payment(username, amount)
                            print(payment_result)
                            if "fully settled" in payment_result:
                                break
                else:
                    print("Invalid action. Please type 'borrow' or 'return'.")

            elif choice == "7":
                genre = input("Enter genre to search: ").strip()
                print(search_books_by_genre(genre))

            elif choice == "8":
                print("Logging out...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Example usage
main_menu()
