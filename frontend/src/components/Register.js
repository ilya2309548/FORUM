import React, { useState } from 'react';
import api from '../utils/api';
import { saveToken } from '../utils/auth';

const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post('/register', { username, password });
            saveToken(response.data.token);
            // Здесь можно перенаправить пользователя или показать сообщение
        } catch (error) {
            console.error("Ошибка регистрации:", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
                required
            />
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
            />
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;
