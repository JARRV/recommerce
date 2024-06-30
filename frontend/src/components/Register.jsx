// src/components/SignUp.js

import React, { useState } from 'react';
import axios from 'axios';

const UserSignUp = async (userData) => {
    try {
        const response = await axios.post('http://localhost:8000/signup/', userData);
        return response.data;
    } catch (error) {
        console.error('Error Signing Up: ', error);
        throw error;
    }
};

const SignUp = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        full_name: '',
        gender: 'M', // Default value
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
            const data = await UserSignUp(formData);
            console.log('User signed up:', data);
        } catch (error) {
            console.error('Error signing up:', error);
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
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Email"
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
            <input
                type="text"
                name="full_name"
                value={formData.full_name}
                onChange={handleChange}
                placeholder="Full Name"
                required
            />
            <select name="gender" value={formData.gender} onChange={handleChange}>
                <option value="M">Male</option>
                <option value="F">Female</option>
                <option value="O">Other</option>
            </select>
            <button type="submit">Sign Up</button>
        </form>
    );
};

export default SignUp;
