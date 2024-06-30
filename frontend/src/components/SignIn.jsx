// src/components/SignIn.js

import React, { useState } from 'react';
import {UserSignIn } from '../api';

const SignIn = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await UserSignIn(formData);
      console.log('User signed in:', data);
    } catch (error) {
      console.error('Error signing in:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="username"
        value={formData.username}
        onChange={handleChange}
        placeholder="Username"
        required
      />
      <input
        type="password"
        name="password"
        value={formData.password}
        onChange={handleChange}
        placeholder="Password"
        required
      />
      <button type="submit">Sign In</button>
    </form>
  );
};

export default SignIn;
