import React, { useState } from 'react';
import api from '../utils/api';
import { getToken } from '../utils/auth';

const CreatePost = () => {
    const [content, setContent] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const token = getToken();
        try {
            await api.post('/posts', { content }, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            // Здесь можно показать сообщение об успешном создании поста
        } catch (error) {
            console.error("Ошибка создания поста:", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <textarea
                value={content}
                onChange={(e) => setContent(e.target.value)}
                placeholder="Write your post here..."
                required
            />
            <button type="submit">Create Post</button>
        </form>
    );
};

export default CreatePost;
