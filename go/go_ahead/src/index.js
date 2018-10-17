import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, NavLink } from 'react-router-dom';

import './index.css';

import { HomePage, AboutPage } from './Components';

const Dhaynes = () => <p>dhaynes</p>;

const App = () => (
    <div>
	<h1>SRCT Go</h1>
        <ul className="header">
            <li>
                <NavLink exact to="/">Home</NavLink>
            </li>
            <li>
                <NavLink to="/dhaynes">dhaynes</NavLink>
            </li>
            <li>
                <NavLink to="/About">About</NavLink>
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

//References
//https://www.kirupa.com/react/creating_single_page_app_react_using_react_router.htm

