import React, { Component } from 'react';
import logo from './logo.gif';
import './App.css';
import { Button, Modal, ModalHeader, ModalBody, ModalFooter, Collapse, NavbarToggler, NavbarBrand, Nav, Navbar, NavItem, NavLink } from 'reactstrap';
import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faCoffee,
  faCog,
  faSpinner,
  faQuoteLeft,
  faSquare,
  faCheckSquare,
  faCloud,
  faCloudUploadAlt
} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

library.add(
  faCloud,
  faCloudUploadAlt,
  faCoffee,
  faCog,
  faSpinner,
  faQuoteLeft,
  faSquare,
  faCheckSquare
)

// var Modal = ReactBootstrap.Modal;

class App extends Component {
  constructor(props) {
    super(props);

    this.toggleNavbar = this.toggleNavbar.bind(this);
    this.state = {
      modal: false,
      collapsed: true
    };
    
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({
      modal: !this.state.modal
    });
  }

  toggleNavbar() {
    this.setState({
      collapsed: !this.state.collapsed
    });
  }

  render() {
    return (
      <div className="App">
      {/* APP STARTS HERE */}

      {/* <NAVBAR> */}
      <div className="nav-color">
        <Navbar color="faded" light>
          <NavbarBrand href="/" className="mr-auto">FireWatch</NavbarBrand>
          <NavbarToggler onClick={this.toggleNavbar} className="mr-2" />
          <Collapse isOpen={!this.state.collapsed} navbar>
            <Nav navbar>
              <NavItem>
                <NavLink href="https://yeet.yee">Link Daniel Cant see</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="https://github.com/rshah2020/DanielCannotAccessThisSecretRepo">Another Link Daniel Cant see</NavLink>
              </NavItem>
            </Nav>
          </Collapse>
        </Navbar>
      </div>
      {/* </NAVBAR> */}

      <div>
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          
          <h1 className="App-title">
            Welcome to FireWatch! 
          </h1>


        <div>
          <button color="success" className="btn btn-success" onClick={this.toggle}>
            <FontAwesomeIcon icon={"cloud-upload-alt"} />
            &nbsp;&nbsp;Add Risk
          </button>

          {/* <MODAL> */}
          
          <Modal isOpen={this.state.modal} toggle={this.toggle} className={this.props.className}>
            <ModalHeader toggle={this.toggle}>Modal title</ModalHeader>
            <ModalBody>
              <form action="http://localhost:5000/api/addrisk" method="post" enctype="multipart/form-data">
              Select an image
                <input type="file" name="image" />
                <input type="submit" value="Upload Image" name="submit" />
              </form>
            </ModalBody>
            <ModalFooter>
              <Button color="primary" onClick={this.toggle}>Cancel</Button>
            </ModalFooter>
          </Modal>
          
          {/* </MODAL> */}

        </div>

        </div>
        
        <p className="App-footer">
          FireWatch was made by a group of broke high school students. &copy; 2018
        </p>
      </div>
      {/* APP ENDS HERE */}
      </div>
    );
  }
}

export default App;
