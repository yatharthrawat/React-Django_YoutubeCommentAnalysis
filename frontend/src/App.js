import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
state = {
    todos: []
 };

async componentDidMount() {

    let headers = new Headers(); 
    headers.append('Access-Control-Allow-Origin', 'http://localhost:3000');
    headers.append('Access-Control-Allow-Credentials', 'true');
    try {
      const res = await fetch('http://127.0.0.1:8000/api/Zzo_m3O6dnc');
      const todos = await res.json();
      console.log(todos)
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }

render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.sentiment}</h1>
            <span>{item.text}</span>
          </div>
        ))}
      </div>
    );
  }
}          

export default App;
