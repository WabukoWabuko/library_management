import React, { useState } from 'react';
import axios from 'axios';

function Transactions() {
  const [bookId, setBookId] = useState('');
  const [memberId, setMemberId] = useState('');
  const [transactionId, setTransactionId] = useState('');
  const [message, setMessage] = useState('');

  const issueBook = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/issue/', { book_id: bookId, member_id: memberId });
      setMessage(response.data.message);
    } catch (error) {
      setMessage(error.response.data.error);
    }
    setBookId('');
    setMemberId('');
  };

  const returnBook = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/return/', { transaction_id: transactionId });
      setMessage(`Returned: ${response.data.message}, Fee: KES ${response.data.fee}`);
    } catch (error) {
      setMessage(error.response.data.error);
    }
    setTransactionId('');
  };

  return (
    <div>
      <h2>Transactions</h2>
      <h3>Issue Book</h3>
      <form onSubmit={issueBook} className="mb-3">
        <input
          type="number"
          className="form-control d-inline w-25 me-2"
          placeholder="Book ID"
          value={bookId}
          onChange={(e) => setBookId(e.target.value)}
        />
        <input
          type="number"
          className="form-control d-inline w-25 me-2"
          placeholder="Member ID"
          value={memberId}
          onChange={(e) => setMemberId(e.target.value)}
        />
        <button type="submit" className="btn btn-success">Issue</button>
      </form>
      <h3>Return Book</h3>
      <form onSubmit={returnBook} className="mb-3">
        <input
          type="number"
          className="form-control d-inline w-25 me-2"
          placeholder="Transaction ID"
          value={transactionId}
          onChange={(e) => setTransactionId(e.target.value)}
        />
        <button type="submit" className="btn btn-warning">Return</button>
      </form>
      {message && <p className="alert alert-info">{message}</p>}
    </div>
  );
}

export default Transactions;
