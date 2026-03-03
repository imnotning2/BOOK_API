const API_URL = "http://localhost:5000/books";

fetchBooks();

async function fetchBooks() {
    const response = await fetch(API_URL);
    const data = await response.json();
    displayBooks(data.books);
}

function displayBooks(books) {
    const list = document.getElementById("book-list");
    list.innerHTML = "";
    books.forEach(book => {
        const div = document.createElement("div");
        div.className = "book-card";
        div.innerHTML = `
            <h3>${book.title}</h3>
            <p>${book.author}</p>
            <button onclick="deleteBook(${book.id})">Delete</button>
        `;
        list.appendChild(div);
    });
}

async function addBook() {
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, author })
    });
    fetchBooks();
}

async function deleteBook(id) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    fetchBooks();
}