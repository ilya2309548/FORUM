import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './components/Register';
import CreatePost from './components/CreatePost';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/register" element={<Register />} />
                <Route path="/create-post" element={<CreatePost />} />
            </Routes>
        </Router>
    );
};

export default App;
