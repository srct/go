import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, Link } from 'react-router-dom';

import './index.css';

import { HomePage, AboutPage } from './Components';

const Dhaynes = () => <p>dhaynes</p>;

const App = () => (
    <div>
	<h1>Simple SPA</h1>
        <ul className="header">
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
	<div className="content">
	  <Route path="/" exact component={HomePage} />
          <Route path="/dhaynes" component={Dhaynes} />
          <Route path="/about" component={AboutPage} />
	</div>
    </div>
);

ReactDOM.render(
    <HashRouter>
        <App />
    </HashRouter>,
    document.getElementById('root')
);
