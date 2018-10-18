import React from 'react';
import { Button } from 'reactstrap';

export default class AuthButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { is_auth: false };
    }

    componentDidMount() {
        this.setState(() => {
            return { is_auth: window.django.user.is_authenticated == 'True' };
        });
    }

    render() {
        return (
            <div>
                {this.state.is_auth ? (
                    <Button color="info" href="/auth/logout">
                        Logout
                    </Button>
                ) : (
                    <Button color="info" href="/auth/login">
                        Login
                    </Button>
                )}
            </div>
        );
    }
}
