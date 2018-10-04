import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';

import { HomePage } from './Components';

// const App = () => (
//     <div>
//         <Header />
//         <HomePage />
//     </div>
// );

ReactDOM.render(
    <BrowserRouter>
        <HomePage />
    </BrowserRouter>,
    document.getElementById('root')
);
