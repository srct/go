import React from 'react';

import { NavBar } from 'Components';

export default class PageTemplate extends React.Component {
    render() {
        return (
            <div>
                <NavBar page={this.props.page} />
                <div>{this.props.children}</div>
            </div>
        );
    }
}
