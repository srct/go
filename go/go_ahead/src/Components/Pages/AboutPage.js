import React from 'react';

import { PageTemplate } from 'Components';

export default class AboutPage extends React.Component {
    state = {};
    render() {
        return (
            <PageTemplate page={'about'}>
                <p>About page</p>
            </PageTemplate>
        );
    }
}
