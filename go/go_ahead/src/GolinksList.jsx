import React from "react";

class GolinksList extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      error: null,
      isLoaded: false,
      golinks: []
    };
  }

  componentDidMount() {
    if (window.django.user.is_authenticated == "True") {
      fetch("/api/golinks/", {
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Authorization: "Token {props.token}"
        }
      })
        .then(res => res.json())
        .then(
          result => {
            this.setState({
              isLoaded: true,
              golinks: result
            });
          },
          // Note: it's important to handle errors here
          // instead of a catch() block so that we don't swallow
          // exceptions from actual bugs in components.
          error => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        );
    }
  }

  render() {
    const { error, isLoaded, golinks } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      if (window.django.user.is_authenticated == "True") {
        return <div>Loading...</div>;
      } else {
        return <div />;
      }
    } else {
      return (
        <div>
          {golinks.map(golink => (
            <h1 key={golink.short}>{golink.short}</h1>
          ))}
        </div>
      );
    }
  }
}

export default GolinksList;
