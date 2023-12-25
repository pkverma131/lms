import React from 'react';
import './App.css';
import Navbar from './Navbar';
import Home from './Home';
import Course from './Course';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
        <Home />
        <Course />
      </header>
    </div>
  );
}

export default App;
