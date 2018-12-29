import React from "react";
import { Card, CardText, CardBody, CardTitle } from "reactstrap";

import { PageTemplate } from "Components";

const AboutPage = () => {
  document.title = "About";
  return (
    <PageTemplate>
      <p>About page</p>
      <Card className="shadow-lg p-3 mb-5 bg-white rounded">
        <CardBody>
          <CardTitle>Terms of Use</CardTitle>
          <CardText>
            By using Go you acknowledge that you are a current George Mason
            Student or faculty member.
            <br />
            Additionally, any link that you create is subject to removal by Go
            admins if it is deemed to associate the univeristy with any
            <br /> derogatory or controversial matters.
            <br />
            Go admins also reserve the right to remove and ban any users who
            attempt to abuse the link creation system in any manner.
            <br />
            Since Go falls under the gmu.edu domain, users who use this service
            will act in compliance with the GMU{" "}
            <a href="https://universitypolicy.gmu.edu/policies/responsible-use-of-computing/">
              Responsible Use of Computing
            </a>{" "}
            policies.
          </CardText>
        </CardBody>
      </Card>
      <Card className="shadow-lg p-3 mb-5 bg-white rounded">
        <CardBody>
          <CardTitle>Who made Go?</CardTitle>
          <CardText>
            <p>
              Members of the
              <a href="//srct.gmu.edu">
                Student-Run Computing and Technology
              </a>{" "}
              registered student organization at{" "}
              <a href="//gmu.edu">George Mason University</a> are the clever,
              <br /> talented student developers behind Go.
            </p>
            <p>
              We are a group of creative people that like making software and
              want to give back to the Mason community at the same time.
            </p>
            <p />
            <a href="//srct.gmu.edu/contact/">Contact us</a> to get involved!
            <p />
          </CardText>
        </CardBody>
      </Card>
      <Card className="shadow-lg p-3 mb-5 bg-white rounded">
        <CardBody>
          <CardTitle>Thanks!</CardTitle>
          <CardText>
            <p>
              This project was made possible through the collective
              contributions of multiple Mason SRCT members.
              <br />
              <a href="https://git.gmu.edu/srct/go/milestones/3">Go 2.2</a>:
              <br />
              <a href="https://github.com/dhaynespls">David Haynes</a>,
              <a href="https://github.com/ocelotsloth">Mark Stenglein</a>,
              <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
                Andres Villogas
              </a>
              ,<a href="https://github.com/IAmEyad">Eyad Hasan</a>,
              <a href="https://github.com/zosman1">Zach Osman</a>,
              <a href="">Leo Grandinetti</a>,
              <a href="https://mason.gmu.edu/~gmoran/">Grady Moran</a>,
              <a href="https://github.com/zmknox">Zach Knox</a>,
              <a href="https://github.com/mike-bailey">Michael Bailey</a>,
              <a href="https://github.com/jrouly">Michel Rouly</a>,
              <a href="https://github.com/nanderson94">Nicholas Anderson</a>,
              <a href="">Kevin Mckigney</a>, and{" "}
              <a href="https://github.com/dwbond">Daniel Bond</a>.<br />
              <a href="https://git.gmu.edu/srct/go/milestones/2">Go 2.1</a>:
              <br />
              <a href="https://github.com/dhaynespls">David Haynes</a>,
              <a href="https://github.com/zosman1">Zach Osman</a>,
              <a href="https://github.com/roberthitt">Robert Hitt</a>,
              <a href="https://github.com/nanderson94">Nicholas Anderson</a>,
              <a href="https://github.com/zmknox">Zach Knox</a>,
              <a href="https://github.com/mike-bailey">Michael Bailey</a>,
              <a href="https://github.com/mdsecurity">Mattias Duffy</a>,
              <a href="https://github.com/IAmEyad">Eyad Hasan</a>, and{" "}
              <a href="https://github.com/danielkim1">Danny Kim</a>.<br />
              <a href="https://git.gmu.edu/srct/go/milestones/1">Go 2.0</a>:
              <br />
              <a href="https://github.com/dhaynespls">David Haynes</a>,
              <a href="">Matthew Rodgers</a>,
              <a href="https://github.com/nanderson94">Nicholas Anderson</a>,
              and <a href="https://github.com/dwbond">Daniel Bond</a>.<br />
              Go 1.0:
              <br />
              <a href="https://github.com/jrouly">Michel Rouly</a>,
              <a href="https://github.com/creffett">Chris Reffett</a>,
              <a href="https://github.com/nanderson94">Nicholas Anderson</a>,
              and <a href="https://github.com/akshaykarthik">Akshay Karthik</a>.
              <br />
            </p>
            <p>
              Additional thanks are due to the{" "}
              <a href="https://wiki.srct.gmu.edu/Executive_Board">
                Student-Run Computing and Technology executive board from
                2014-present
              </a>
              , and our academic advisor,
              <a href="https://cs.gmu.edu/~kdobolyi/">
                Professor Kinga Dobolyi
              </a>
              .
            </p>
          </CardText>
        </CardBody>
      </Card>
    </PageTemplate>
  );
};

export default AboutPage;
