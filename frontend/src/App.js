import logo from './logo.svg';
import React, {Component} from 'react'
import './App.css';
import testAPI from './api/testApi';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      grades: [],
      error: null
    };
  }

  getAllGrades = () => {
    testAPI.getAPI().getAllGrades()
    .then(gradingBOs =>
        this.setState({
            grades: gradingBOs,
            error: null
        })).catch(e =>
            this.setState({
                grades:[],
                error: e
            }))
  } 


  componentDidMount(){
    this.getAllGrades();
  }

  render(){

    console.log('Grades: '+this.state.grades.length)
    return (
      <div className="App">
        <h1>Test API</h1>
        {this.state.grades.map(grade =>(
          <>
          <b>{grade.getGrade()}</b>
          <br/>
          </>
        ))}
      </div>
    );
  }
}

export default App;
