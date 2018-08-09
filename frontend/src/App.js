import React, { Component } from 'react';
import './App.css';


function Element(props) {
    return (
        <tr>
            <td className={props.style}>
            {props.value}
            </td>
        </tr>
    );
}

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            list: null,
            url: '',
            td_pos:"td_pos",
            td_neg:"td_neg",
            body:"body_color"
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({url: event.target.value});
    }

    handleSubmit(event) {
        // I really need to learn Regex

        let video_id_extracted = this.state.url.match(/(?:https?:\/{2})?(?:w{3}\.)?youtu(?:be)?\.(?:com|be)(?:\/watch\?v=|\/)([^\s&]+)/);
        fetch('http://127.0.0.1:8000/api/' + video_id_extracted[1])
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                this.setState({list: data});
            });
        event.preventDefault();
    }

    renderElement(i) { // Method that creates Button for each course and attaches onClick style decider props.
        return (
            <Element value={this.state.list[i].text}
                    style={this.state.list[i].sentiment === 'pos' ? this.state.td_pos : this.state.td_neg}/>
        );
    }

    render() {
        document.title = "Youtube Comment Analysis";
        let pos=0;
        let neg=0;
        let elements=[];
        if(this.state.list!=null) {
            for (let i = 0; i < this.state.list.length; i++) {
                elements.push(this.renderElement(i));
                if(this.state.list[i].sentiment==='pos'){
                    pos++;
                }
                else{
                    neg++;
                }
            }
        }
        if(neg === pos && pos === 0){
            document.body.style.backgroundColor = "#f2f2f2";
        }
        else if(pos>neg){
            document.body.style.backgroundColor = "#e6ffcc";
        }
        else if(pos<neg){
            document.body.style.backgroundColor = "#ffcccc";
        }
        else if(pos===neg){
            document.body.style.backgroundColor = "#ffffcc";
        }
        return (


            <div>
                <h1>Youtube Comment Analysis</h1>
                <div className="form_search">
                    <form onSubmit={this.handleSubmit}>
                        <label className="search_text">
                            Enter URL &nbsp;
                            <input type="text" size="75" className="search" value={this.state.url}
                                   onChange={this.handleChange}/>
                        </label>
                        <input className="search_button" type="submit" value="Go"/>
                    </form>
                </div>
                <div className="comments">
                <table>
                    <tbody>
                    {elements}
                    </tbody>
                </table>
                </div>
            </div>

        )
    }

}
export default App;
