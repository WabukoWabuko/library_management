import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Books() {
  const [books, setBooks] = useState([]);
  const [name, setName] = useState('');
  const [author, setAuthor] = useState('');
  const [stock, setStock] = useState('');
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    const response = await axios.get('/api/books/');
    setBooks(response.data);
  };

  const addBook = async (e) => {
    e.preventDefault();
    await axios.post('/api/books/', { name, author, stock });
    fetchBooks();
    setName('');
    setAuthor('');
    setStock('');
  };

  const searchBooks = async () => {
    const response = await axios.get(`/api/search/?q=${search}`);
    setBooks(response.data);
  };

  return (
    <div>
      <h2>Books</h2>
      <form onSubmit={addBook} className="mb-3">
        <input
          type="text"
          className="form-control d-inline w-25 me-2"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          className="form-control d-inline w-25 me-2"
          placeholder="Author"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
        />
        <input
          type="number"
          className="form-control d-inline w-15 me-2"
          placeholder="Stock"
          value={stock}
          onChange={(e) => setStock(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">Add Book</button>
      </form>
      <div className="mb-3">
        <input
          type="text"
          className="form-control d-inline w-50 me-2"
          placeholder="Search by name or author"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <button onClick={searchBooks} className="btn btn-info">Search</button>
      </div>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Author</th>
            <th>Stock</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.id}>
              <td>{book.id}</td>
              <td>{book.name}</td>
              <td>{book.author}</td>
              <td>{book.stock}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Books;
