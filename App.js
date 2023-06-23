import logo from './logo.svg';
import './App.css';
import Axios from 'axios'
import { Icon } from '@iconify/react';
import{ useState } from 'react';
import {BrowserRouter as Router, Switch, Routes, Route, Link} from 'react-router-dom';
import Nav from './Components/Nav';
import Header from './Components/Header';
import LinkForm from './Components/LinkForm';
function App() {
  return (
    <body>
       <div className="App">
       <Nav optionOne="Sign Up" optionTwo="Sign In" OptionThree="More" suboptionOne="Saving LinkShorts" suboptionTwo="Existing User"/>
      <Header message="Shorten a Link Below" />
      <LinkForm />
    </div>
    </body>
  
  );
}

export default App;
