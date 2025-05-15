# Description
This project is the React frontend part of an educational  project, which demonstrates connection to the backend for obtaining data and performing CRUD operations on it.
Before running the project ensure that the backend is running.
In order to configure the base URL for connecting to the backend use .env file (variable `REACT_APP_BASE_URL`). In order to obtain a configuration file, rename the [.env.example](./.env.example) into `.env`. 
 

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm install`
First of all run `npm install` for installing  node modules.

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### Run mock server
To run mock server you need to install and run json server in to console.

`npm install -g json-server`

`json-server db.json -p 5000`

