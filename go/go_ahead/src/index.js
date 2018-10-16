import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, Link } from 'react-router-dom';
import { Button } from 'reactstrap';

import { HomePage, AboutPage, NavBar } from 'Components';

const Dhaynes = () => <p>dhaynes</p>;

const App = () => (
    <div>
        <NavBar />
        <Route path="/" exact component={HomePage} />
        <Route path="/dhaynes" component={Dhaynes} />
        <Route path="/about" component={AboutPage} />
    </div>
);

ReactDOM.render(
    <HashRouter>
        <App />
    </HashRouter>,
    document.getElementById('root')
);
