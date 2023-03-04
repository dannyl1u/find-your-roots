import logo from './logo.svg';
import React, { Component }  from 'react';
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState()
  useEffect(() => {
  // Using fetch to fetch the api from 
  // flask server it will be redirected to proxy
  fetch("http://localhost:5000/getNodes").then((res) =>
      res.json().then((data) => {
          // Setting a data from api
          setData(data[0])
          console.log(data.name)
      })
  );
}, []);

  return (
    <div className="App">
      <h1>
        Name: {data && data.name}
      </h1>
      <h2>
        Age: {data && data.age}
      </h2>

    </div>
  );
}

export default App;
