import React from 'react';

import { NavBar } from 'Components';

export default class PageTemplate extends React.Component {
    render() {
        return (
            <div style={[styles.container, this.props.style]}>
                <NavBar />
                <div>{this.props.children}</div>
            </div>
        );
    }
}
