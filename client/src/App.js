import logo from './logo.svg';
import React, { Component }  from 'react';
import './App.css';
import { useState, useEffect } from 'react';
// import {Person} from 'components/Person'
import FamilyTree from './mytree'

function App() {
  const [data, setData] = useState([])
  useEffect(() => {
  // Using fetch to fetch the api from 
  // flask server it will be redirected to proxy
  fetch("http://localhost:5000/getNodes").then((res) =>
      res.json().then((data) => {
          // Setting a data from api
          setData(data)
          console.log(data)
      })

      
  );
}
, []);

  return (
    <FamilyTree nodes={ data &&
      data.map((data) => (
        { id: 1, pids: [2], name: 'asdf', gender: 'female', img: 'https://cdn.balkan.app/shared/2.jpg'  },
        { id: 2, pids: [1], name: 'Ava Field', gender: 'male', img: 'https://cdn.balkan.app/shared/m30/5.jpg' },
        { id: 3, mid: 1, fid: 2, name: 'Peter Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/2.jpg' },
        { id: 4, mid: 1, fid: 2, name: 'Savin Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/1.jpg'  },
        { id: 5, mid: 1, fid: 2, name: 'Emma Stevens', gender: 'female', img: 'https://cdn.balkan.app/shared/w10/3.jpg' }
      ))
  } />
  //   <div>
  //   {data && (
  //     <ul>
  //       {data.map(person => (
  //         <li> {person.name} {person.age}</li>
  //       ))}
  //     </ul>
  //   )}
  // </div>

  );
}

export default App;