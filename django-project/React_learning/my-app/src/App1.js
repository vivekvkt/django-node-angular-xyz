import React,{useState} from 'react';
import './App.css';
import Person from './Person/Person'

const App= props=> {

  const [personsState,setPersonsState]= useState({
    persons:[
      {
        name:'Max', age:28
      },
      {name:'Manu', age:20},
      {name:'Stephen', age:39}
    ],
    otherState : "hello vivek"
  });


  const switchhandler=()=>{
    console.log("cllicked me")
    setPersonsState({
      persons:[
        {
          name:'vivek', age:28
        },
        {name:'maximilanvivek', age:20},
        {name:'Stephen', age:39}
      ]
    })
  }
  
    return (
      <div className="App">
      <h1>hello vivek this is the first react App</h1>
      <button onClick={switchhandler}>SwitchName</button>
      <Person name="vivek" age="30"/>
      <Person name={personsState.persons[0].name} age={personsState.persons[0].age}/>
      <Person
       name={personsState.persons[0].name} 
       age={personsState.persons[0].age}
       click={switchhandler}
       />
      <Person>My Hobbies:Listeming music</Person>
      </div>
     
    );
  }


export default App;


