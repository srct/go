import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, Link } from 'react-router-dom';

import { HomePage } from './Components';
import { ABoutPage } from './Components';

const Dhaynes = () => <p>dhaynes</p>;

const App = () => (
    <div>
        <ul>
            <li>
                <Link to="/">Home</Link>
            </li>
            <li>
                <Link to="/dhaynes">dhaynes</Link>
            </li>
            <li>
                <Link to="/About">About</Link>
            </li>
         </ul>
        <Route path="/" exact component={HomePage} />
        <Route path="/dhaynes" component={Dhaynes} />
        <Route path="/About" component={AboutPage} />
    </div>
);

ReactDOM.render(
    <HashRouter>
        <App />
    </HashRouter>,
    document.getElementById('root')
);
