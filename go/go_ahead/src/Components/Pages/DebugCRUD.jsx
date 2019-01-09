import React from "react";
import {
  PageTemplate,
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
      <PageTemplate>
        <div>
          <h1>Debug CRUD Page</h1>

          <h3>Create</h3>
          <DebugCreate />

          <h3>Read</h3>
          <DebugRead />

          <h3>Update</h3>
          <DebugUpdate />

          <h3>Delete</h3>
          <DebugDelete />
        </div>
      </PageTemplate>
    );
  }
}

export default DebugCRUD;
