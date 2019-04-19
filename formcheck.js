// formcheck.js
// runs all the client side validation for the signup, login, and message board
// Jacob Harrison

// check if the page has been reloaded
if (performance.navigation.type == 1) {
  console.info( "This page is reloaded" );
} else {
  console.info( "This page is not reloaded");
  // see which URL the user just came from
  var oldURL = document.referrer;
  // the user came from signup.html and is currently in signup.html it means the username is already being used so print out an alert that the username already exists
  if (oldURL == "http://midn.cyber.usna.edu/~m202556/project02/signup.html" && document.location=="http://midn.cyber.usna.edu/~m202556/project02/signup.html") {
    alert("Username already exists");
    document.getElementById('usernameerrors').innerHTML="Username exists";
    //document.getElementById('usernameerrors').innerHTML="Username already exists";
  }
  // if the user came from login.html and is currently in login.html that means the login credentials were invalid so send an alert saying they were invalid
  if (oldURL == "http://midn.cyber.usna.edu/~m202556/project02/login.html" && document.location=="http://midn.cyber.usna.edu/~m202556/project02/login.html") {
    alert("Invalid credentials");
  }
}





//the overall function to check and validate on submit that the form is filled out correctly based on the requirements
function validateForm() {
  //make sure first/last name text box isn't empty
  if (document.forms["signupform"]["fl_name"].value == "") {
    document.getElementById('fl_name_errors').innerHTML="Please fill out first & last name";
    return false;
  }
  var x = document.forms["signupform"]["fl_name"].value;
  if (x.length > 50) {
    document.getElementById('fl_name_errors').innerHTML="Maximum of 50 characters for name";
    return false;
  }
  // make sure username text box isn't empty and return error if it is
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  var x = document.forms["signupform"]["username"].value;
  if (x.length > 20) {
    document.getElementById('usernameerrors').innerHTML="Maxiumum of 20 characters for username";
    return false;
  }
  var x = document.forms["signupform"]["pswd"].value;
  if (x.length > 30) {
    document.getElementById('pswderrors').innerHTML="Maxiumum of 30 characters for password";
    return false;
  }
  //if the password is less than length of 6 return error
  if (x.length < 6) {
     document.getElementById('pswderrors').innerHTML="Password must be at least 6 characters";
     return false;
  }
  //if there's no digit in the password return an error
  if (/\d/.test(x) == false) {
    document.getElementById('pswderrors').innerHTML="Password must contain at least 1 number";
    return false;
  }
  //check that both password requirements are met to clear error box
  if (x.length > 5 && /\d/.test(x) == true) {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
}

// function to validation the login form on submit
function validateForm_login() {
  // make sure username text box isn't empty
  var y = document.forms["signupform"]["username"].value;
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  if (document.forms["signupform"]["username"].length > 20) {
    document.getElementById('usernameerrors').innerHTML="Maxiumum of 20 characters for username";
    return false;
  }
  var z = document.forms["signupform"]["pswd"].value;
  // make sure password text box isn't empty
  if (document.forms["signupform"]["pswd"].value == "") {
    document.getElementById('pswderrors').innerHTML="Please fill out Password";
    return false;
  }
  if (document.forms["signupform"]["pswd"].length > 30) {
    document.getElementById('pswderrors').innerHTML="Maxiumum of 30 characters for password";
    return false;
  }
}

// function for validating just the first/last name textbox onblur
// and that it gets filled in
function validate_fl_name() {
  // if the textbox is empty return an error message
  if (document.forms["signupform"]["fl_name"].value == "") {
    document.getElementById('fl_name_errors').innerHTML="Please fill out first & last name";
    return false;
  }
  // if textbox is not empty erase the error message
  if (document.forms["signupform"]["fl_name"].value != "") {
    document.getElementById('fl_name_errors').innerHTML="";
    return true;
  }
  var x = document.forms["signupform"]["fl_name"].value;
  if (x.length > 50) {
    document.getElementById('fl_name_errors').innerHTML="Maximum of 50 characters for name";
    return false;
  }
}

// function for validating just the username textbox onblur
// and that it gets filled in
function validateUsername() {
  // if the textbox is empty return an error message
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  var x = document.forms["signupform"]["username"].value;
  if (x.length > 20) {
    document.getElementById('usernameerrors').innerHTML="Maxiumum of 20 characters for username";
    return false;
  }
  var y = document.forms["signupform"]["username"]
  if (x.length < 21 && (y.value!="") == true) {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
  // if textbox is not empty erase the error message
  // if (document.forms["signupform"]["username"].value != "") {
  //   document.getElementById('usernameerrors').innerHTML="";
  //   return true;
  // }
}

// function for validating just the password textbox onblur
// and that it gets filled in with the correct requirements
function validatePswd() {
  var x = document.forms["signupform"]["pswd"].value;
  //if the password is less than length of 6 return error
  if (x.length < 6) {
     document.getElementById('pswderrors').innerHTML="Password must be at least 6 characters";
     return false;
  }
  if (x.length > 30) {
    document.getElementById('pswderrors').innerHTML="Maxiumum of 30 characters for password";
    return false;
  }
  //if there's no digit return an error
  if (/\d/.test(x) == false) {
    document.getElementById('pswderrors').innerHTML="Password must contain at least 1 number";
    return false;
  }
  //check that both password requirements are met to clear error box
  if (x.length > 5 && /\d/.test(x) && x.length < 31 == true) {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
}

// function for validating the password textbox on the login page
function validatePswd_login() {
  // make sure text is entered into the password text box
  if (document.forms["signupform"]["pswd"].value == "") {
    document.getElementById('pswderrors').innerHTML="Please fill out Password";
    return false;
  }
  var x = document.forms["signupform"]["pswd"].value;
  if (x.length > 30) {
    document.getElementById('pswderrors').innerHTML="Maxiumum of 30 characters for password";
    return false;
  }
  // delete the error if the password thas text typed into it
  if (document.forms["signupform"]["pswd"].value != "") {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
  y = document.forms["signupform"]["pswd"]
  if (x.length < 31 && (y.value!="") == true) {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
}
