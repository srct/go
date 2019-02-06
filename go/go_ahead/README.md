# go_ahead | The react app

[React is a JavaScript library for building user interfaces.](https://reactjs.org/) The focus of the library is on component design and implementation.

I'll be the first one to admit that it is very daunting to jump into a React project if you are unfamiliar with the library, javascript, and general modern web developemnt trends. To help with that learning curve I have two suggested resources:

1. [A re-introduction to JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript) | A great start to reviewing JS and how you can translate knowledge from other languages into it.
1. [React Main Concepts](https://reactjs.org/docs/hello-world.html) | A step by step walkthrough of React, component architecture, and how you can best utilize the React API.

## React project structure

Take a chance to review the layout of the app:

```
src/
├── App.jsx                     | The entry point for our React app.
├── Components
│   ├── Molecules               | All reusable components that are individual.
│   │   └── index.js
│   ├── Organisms               | Containers for molecule components.
│   │   └── index.js
│   ├── Pages                   | Containers for organisms.
│   │   └── index.js
│   ├── Templates               | Containers for pages.
│   │   └── index.js
│   └── index.js
└── Utils                       | Misc. standalone JS functions.
    └── index.js
```

## Dev work

Since we will need to rebuild our app on a regular basis as we edit the javascript we need to start a process that watches the code and rebuilds the app.

You'll need [node installed](https://nodejs.org/en/download/package-manager/).

```sh
npm install -g yarn
yarn
yarn dev
```

This starts a foreground process that will rebuild the React site whenever
there is a change.

Make sure you are running this alongside the docker-compose process so that you can visit the site at [127.0.0.1:8000](http://127.0.0.1:8000)

All react errors are printed to the webpack console stdout.

Make sure to check your web browser's JS console as well!
