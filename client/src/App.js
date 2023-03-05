import logo from './logo.svg';
import React, { Component }  from 'react';
import './App.css';
import { useState, useEffect } from 'react';
// import {Person} from 'components/Person'
import FamilyTree from './mytree'


let personId = 1;
let prevPersonId = 0;

function App() {
  const [data, setData] = useState([])
  useEffect(() => {
  // Using fetch to fetch the api from 
  // flask server it will be redirected to proxy
  fetch("http://localhost:5000/getNodes").then((res) =>
      res.json().then((data) => {
          // Setting a data from api
          setData(data)

          console.log(data[0])
          console.log(data[1])

      })

      
  );
}
, []);

  return (
  //   <h1>hello</h1>
  // )
      // <div>{data && data.map}</div>
  //   <div>
  //   <FamilyTree nodes={
  //     data.map((e) => (

  //        { id: 1, mid: 1, fid: 2, name: 'Savin Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/1.jpg'  }
        
  //       //{ id: 1, pids: [2], name: "asdf", gender: 'female'  }
  //       // { id: 2, pids: [1], name: 'Ava Field', gender: 'male', img: 'https://cdn.balkan.app/shared/m30/5.jpg' },
  //       // { id: 3, mid: 1, fid: 2, name: 'Peter Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/2.jpg' },
  //       // { id: 4, mid: 1, fid: 2, name: 'Savin Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/1.jpg'  },
  //       // { id: 5, mid: 1, fid: 2, name: 'Emma Stevens', gender: 'female', img: 'https://cdn.balkan.app/shared/w10/3.jpg' ]
  //     ))
  // } /> 
  // </div>
  
//   data && <FamilyTree nodes={ [

//       { id: 1, pids: [2], name: data.name, gender: 'female', img: 'https://cdn.balkan.app/shared/2.jpg'  },
//       { id: 2, pids: [1], name: 'Ava Field', gender: 'male', img: 'https://cdn.balkan.app/shared/m30/5.jpg' },
//       { id: 3, mid: 1, fid: 2, name: 'Peter Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/2.jpg' },
//       { id: 4, mid: 1, fid: 2, name: 'Savin Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/1.jpg'  },
//       { id: 5, mid: 1, fid: 2, name: 'Emma Stevens', gender: 'female', img: 'https://cdn.balkan.app/shared/w10/3.jpg' }
//   ]
// } />

//   <FamilyTree nodes={ [
//       { id: 1, pids: [2], name: data.name, gender: 'female', img: 'https://cdn.balkan.app/shared/2.jpg'  },
//       { id: 2, pids: [1], name: 'Ava Field', gender: 'male', img: 'https://cdn.balkan.app/shared/m30/5.jpg' },
//       { id: 3, mid: 1, fid: 2, name: 'Peter Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/2.jpg' },
//       { id: 4, mid: 1, fid: 2, name: 'Savin Stevens', gender: 'male', img: 'https://cdn.balkan.app/shared/m10/1.jpg'  },
//       { id: 5, mid: 1, fid: 2, name: 'Emma Stevens', gender: 'female', img: 'https://cdn.balkan.app/shared/w10/3.jpg' }
//   ]
// } />

    <div>
    {data && (
      <ul>
        {data.map(person => {
          // personId++

          //<li> {person.name} {person.age} {person.id} </li>
          return <FamilyTree nodes={
            [{id: person.id, pids: [person.id], name: person.name, gender: 'female', img: 'https://cdn.balkan.app/shared/2.jpg'}]}/>
            
          })}
        
        
      </ul>
    )}
  </div>

  );
}

export default App;