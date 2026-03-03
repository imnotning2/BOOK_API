from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory database for simplicity)
books = [
    {
        "id": 1,
        "title": "Frozen",
        "author": "Jennifer Lee",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
        "price": 19.99
    },
    {
        "id": 2,
        "title": "The Lion King",
        "author": "Roger Allers",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
        "price": 17.99
    },
    {
        "id": 3,
        "title": "Beauty and the Beast",
        "author": "Gary Trousdale",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/e/e9/Beauty_and_the_Beast_1991_poster.jpg",
        "price": 16.50
    },
    {
        "id": 4,
        "title": "Aladdin",
        "author": "Ron Clements",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/5/58/Aladdinposter.jpg",
        "price": 15.75
    },
    {
        "id": 5,
        "title": "Moana",
        "author": "John Musker",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
        "price": 18.25
    },
    {
        "id": 6,
        "title": "Tangled",
        "author": "Nathan Greno",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",
        "price": 14.99
    },
    {
        "id": 7,
        "title": "Encanto",
        "author": "Jared Bush",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/1/15/Encanto_poster.jpg",
        "price": 20.00
    },
    {
        "id": 8,
        "title": "Cinderella",
        "author": "Wilfred Jackson",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/5/54/Cinderella_%281950_film%29.jpg",
        "price": 13.99
    }
]

# Create (POST) operation
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)
    return jsonify(new_book), 201

# Read (GET) operation - Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify({"books": books})

# Read (GET) operation - Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Update (PUT) operation
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Delete operation
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"})
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
