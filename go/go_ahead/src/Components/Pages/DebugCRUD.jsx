import React from "react";
import {
  AuthedPageTemplate,
  DebugRead,
  DebugCreate,
  DebugDelete,
  DebugUpdate
} from "Components";

class DebugCRUD extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <AuthedPageTemplate>
        <DebugCreate />

        <h3>Read</h3>
        <DebugRead />

        <h3>Update</h3>
        <DebugUpdate />

        <h3>Delete</h3>
        <DebugDelete />
      </AuthedPageTemplate>
    );
  }
}

export default DebugCRUD;
