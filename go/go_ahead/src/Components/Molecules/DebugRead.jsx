import React, { useState, useEffect } from "react";
import { Button, Card, CardBody, CardTitle, Table } from "reactstrap";

const DebugRead = () => {
  const [goLinks, updateGoLinks] = useState([]);

  const getAllGoLinks = async () => {
    let response = await fetch("/api/golinks/", {
      headers: {
        "Content-Type": "application/json"
      }
    });
    let data = await response.json();
    updateGoLinks(data);
  };

  useEffect(() => {
    getAllGoLinks();
  }, []);

  return (
    <div>
      <Card>
        <CardBody>
          <CardTitle className="d-flex">
            Read
            <Button
              className="ml-auto"
              onClick={() => getAllGoLinks()}
              outline
              color="primary"
            >
              Refresh
            </Button>
          </CardTitle>

          <Table>
            <thead>
              <tr>
                <th>short</th>
                <th>destination</th>
                <th>expires</th>
              </tr>
            </thead>
            <tbody>
              {goLinks.map(goLink => (
                <tr key={goLink.short}>
                  <td>
                    <a href={`/${goLink.short}`}> /{goLink.short}</a>
                  </td>
                  <td>{goLink.destination}</td>
                  <td>{goLink.date_expires}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </CardBody>
      </Card>
    </div>
  );
};

export default DebugRead;
