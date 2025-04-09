import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Members() {
  const [members, setMembers] = useState([]);
  const [name, setName] = useState('');

  useEffect(() => {
    fetchMembers();
  }, []);

  const fetchMembers = async () => {
    const response = await axios.get('/api/members/');
    setMembers(response.data);
  };

  const addMember = async (e) => {
    e.preventDefault();
    await axios.post('/api/members/', { name, debt: 0 });
    fetchMembers();
    setName('');
  };

  return (
    <div>
      <h2>Members</h2>
      <form onSubmit={addMember} className="mb-3">
        <input
          type="text"
          className="form-control d-inline w-50 me-2"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">Add Member</button>
      </form>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Debt (KES)</th>
          </tr>
        </thead>
        <tbody>
          {members.map((member) => (
            <tr key={member.id}>
              <td>{member.id}</td>
              <td>{member.name}</td>
              <td>{member.debt}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Members;
