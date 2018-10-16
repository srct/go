import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, Link } from 'react-router-dom';
import { Button } from 'reactstrap';

import { HomePage, AboutPage, NavBar, PageTemplate } from 'Components';
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
