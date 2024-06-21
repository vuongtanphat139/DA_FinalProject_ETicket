import React from 'react';
import ReactDOM from 'react-dom'; // Thay đổi import đến react-dom
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = document.getElementById('root'); // Không cần sử dụng createRoot
ReactDOM.render(
    <React.StrictMode>
        <App></App>
    </React.StrictMode>,
    root,
);

reportWebVitals();
