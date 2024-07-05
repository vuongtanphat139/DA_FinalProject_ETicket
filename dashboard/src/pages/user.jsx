import axios from 'axios';
import React, { useState, useEffect } from 'react';

import './UserPage.css';

export default function UserPage() {
  const [users, setUsersAPI] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const usersPerPage = 7;
  const [editingUser, setEditingUser] = useState(null);
  const [formData, setFormData] = useState({
    username: '',
    fullname: '',
    gender: '',
    dob: '',
    phone: '',
    email: '',
    address: '',
    citizenID: ''
  });

  const fetchUser = async () => {
    try {
      const response = await axios.get("http://localhost:5000/users");
      console.log("data:", response.data);
      setUsersAPI(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchUser();
  }, []);

  // Pagination logic
  const indexOfLastUser = currentPage * usersPerPage;
  const indexOfFirstUser = indexOfLastUser - usersPerPage;
  const currentUsers = users.slice(indexOfFirstUser, indexOfLastUser);

  const totalPages = Math.ceil(users.length / usersPerPage);

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  const handleEditClick = (user) => {
    setEditingUser(user);
    setFormData({
      username: user.UserName,
      fullname: user.FullName,
      gender: user.Gender,
      dob: new Date(user.DoB).toISOString().split('T')[0],
      phone: user.Phone,
      email: user.Email,
      address: user.Address,
      citizenID: user.CitizenID
    });
  };

  const handleFormChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.put(`http://localhost:5000/profile/user/${editingUser.UserID}`, formData);
      setEditingUser(null);
      fetchUser();
    } catch (error) {
      console.error("Error updating user:", error);
    }
  };

  return (
    <div className="container">
      <h1>User</h1>
      <table className="custom-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Full Name</th>
            <th>Username</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Gender</th>
            <th>Date of Birth</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {currentUsers.map((user, index) => (
            <tr key={user.UserID}>
              <td>{indexOfFirstUser + index + 1}</td>
              <td>{user.FullName}</td>
              <td>{user.UserName}</td>
              <td>{user.Email}</td>
              <td>{user.Phone}</td>
              <td>{user.Address}</td>
              <td>{user.Gender}</td>
              <td>{new Date(user.DoB).toLocaleDateString()}</td>
              <td>
                <button type="button" className="update-button" onClick={() => handleEditClick(user)}>
                  Update
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="pagination">
        <button type="button" onClick={handlePrevPage} disabled={currentPage === 1}>
          Previous
        </button>
        <span>{`Page ${currentPage} of ${totalPages}`}</span>
        <button type="button" onClick={handleNextPage} disabled={currentPage === totalPages}>
          Next
        </button>
      </div>

      {editingUser && (
        <div className="modal">
          <form className="update-form" onSubmit={handleFormSubmit}>
            <h2>Update User</h2>
            <label htmlFor="username">
              Username:
              <input
                type="text"
                id="username"
                name="username"
                value={formData.username}
                onChange={handleFormChange}
              />
            </label>
            <label htmlFor="fullname">
              Full Name:
              <input
                type="text"
                id="fullname"
                name="fullname"
                value={formData.fullname}
                onChange={handleFormChange}
              />
            </label>
            <label htmlFor="gender">
              Gender:
              <input
                type="text"
                id="gender"
                name="gender"
                value={formData.gender}
                onChange={handleFormChange}
              />
            </label>
            <label htmlFor="dob">
              Date of Birth:
              <input
                type="date"
                id="dob"
                name="dob"
                value={formData.dob}
                onChange={handleFormChange}
              />
            </label>
            <label htmlFor="phone">
              Phone:
              <input
                type="text"
                id="phone"
                name="phone"
                value={formData.phone}
                onChange={handleFormChange}
              />
            </label>
            <label htmlFor="email">
              Email:
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleFormChange}
              />
            </label>
            <label htmlFor="address">
              Address:
              <input
                type="text"
                id="address"
                name="address"
                value={formData.address}
                onChange={handleFormChange}
              />
            </label>
            <label htmlFor="citizenID">
              Citizen ID:
              <input
                type="text"
                id="citizenID"
                name="citizenID"
                value={formData.citizenID}
                onChange={handleFormChange}
              />
            </label>
            <button type="submit">Submit</button>
            <button type="button" onClick={() => setEditingUser(null)}>Cancel</button>
          </form>
        </div>
      )}
    </div>
  );
}
