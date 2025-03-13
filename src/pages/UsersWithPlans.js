import React, { useState, useEffect } from 'react';
import '../styles/UsersWithPlans.css';

function UsersWithPlans() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  // Fetch users with subscription plans
  useEffect(() => {
    const fetchUsersWithPlans = async () => {
      try {
        const response = await fetch('http://localhost:8000/users-with-plans');
        if (!response.ok) {
          throw new Error('Failed to fetch users');
        }
        const data = await response.json();
        setUsers(data.users_with_plans); // Ensure the key matches what the API returns
      } catch (error) {
        setError(error.message);
      }
    };

    fetchUsersWithPlans();
  }, []);

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div className="users-plans-container">
      <h2 className="users-plans-header">Users with Subscription Plans</h2>

      {/* Table structure */}
      <table className="users-plans-table">
        <thead>
          <tr>
            <th>User ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Plan</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.user_id}>
              <td>{user.user_id}</td>
              <td>{user.user_f_name}</td>
              <td>{user.user_l_name}</td>
              <td>{user.email}</td>
              <td>{user.plan_name || 'No plan assigned'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default UsersWithPlans;