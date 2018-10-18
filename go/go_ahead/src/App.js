import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, Link } from 'react-router-dom';
// Apply Global Masonstrap styling
import "masonstrap/build/css/masonstrap.min.css";
import "masonstrap/build/js/masonstrap.min.js";
import { Routes } from 'Utils';

// const App = () => (
//     <PageTemplate>
//         <Routes />
//     </PageTemplate>
// );

ReactDOM.render(
    <HashRouter>
        <Routes />
    </HashRouter>,
    document.getElementById('root')
);
