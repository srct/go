import React from 'react';

import { PageTemplate } from 'Components';

export default class HomePage extends React.Component {
    render() {
        return (
            <PageTemplate page={'home'}>
                <p>Hello World! 1</p>
            </PageTemplate>
        );
    }
}
