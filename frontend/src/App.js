import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Books from './components/Books';
import Members from './components/Members';
import Transactions from './components/Transactions';

function App() {
  return (
    <Router>
      <div className="container mt-4">
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">Library</Link>
            <div className="navbar-nav">
              <Link className="nav-link" to="/books">Books</Link>
              <Link className="nav-link" to="/members">Members</Link>
              <Link className="nav-link" to="/transactions">Transactions</Link>
            </div>
          </div>
        </nav>
        <Routes>
          <Route path="/books" element={<Books />} />
          <Route path="/members" element={<Members />} />
          <Route path="/transactions" element={<Transactions />} />
          <Route path="/" element={<h1>Welcome to Library Management</h1>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
