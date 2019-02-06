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
        <div className="my-3">
          <DebugCreate />
        </div>

        <div className="my-3">
          <DebugRead />
        </div>

        <div className="my-3">
          <DebugUpdate />
        </div>

        <div className="my-3">
          <DebugDelete />
        </div>
      </AuthedPageTemplate>
    );
  }
}

export default DebugCRUD;
