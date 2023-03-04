import logo from './logo.svg';
import React, { Component }  from 'react';
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState()
  useEffect(() => {
  // Using fetch to fetch the api from 
  // flask server it will be redirected to proxy
  fetch("http://localhost:5000/index").then((res) =>
      res.json().then((data) => {
          // Setting a data from api
          setData(data)
          console.log(data.name)
      })
  );
}, []);

  return (
    <div className="App">
       {data && data.name}
    </div>
  );
}

export default App;
