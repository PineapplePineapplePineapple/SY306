//the overall function to check and validate on submit that my form
//is filled out correctly based on the requirements
function validateForm() {
  //make sure first/last name text box isn't empty
  if (document.forms["signupform"]["fl_name"].value == "") {
    document.getElementById('fl_name_errors').innerHTML="Please fill out first & last name";
    return false;
  }
  // make sure username text box isn't empty
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  var x = document.forms["signupform"]["pswd"].value;
  //if the password is less than length of 6 return error
  if (x.length < 6) {
     document.getElementById('pswderrors').innerHTML="Password must be at least 6 characters";
     return false;
  }
  //if there's no digit return an error
  if (/\d/.test(x) == false) {
    document.getElementById('pswderrors').innerHTML="Password must contain at least 1 number";
    return false;
  }
  //check that both password requirements are met to clear error box
  if (x.length > 5 && /\d/.test(x) == true) {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
  var y = document.forms["signupform"]["textarea"].value;
  // if the textarea contains "<" then go into the if statement
  if (/</g.test(y) == true) {
    // replace all < with &lt;
    var y = y.replace(/</g, "&lt;");
    // write the updated string to the textarea
    document.forms["signupform"]["textarea"].value = y;
  }
}

// function for validating just the first/last name textbox onblur
// and that it gets filled in
function validatefl_name() {
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
}

// function for validating just the username textbox onblur
// and that it gets filled in
function validateUsername() {
  // if the textbox is empty return an error message
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  // if textbox is not empty erase the error message
  if (document.forms["signupform"]["username"].value != "") {
    document.getElementById('usernameerrors').innerHTML="";
    return true;
  }
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
  //if there's no digit return an error
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

function validateTextarea() {
  var x = document.forms["signupform"]["textarea"].value;
  // if the textarea contains "<" then go into the if statement
  if (/</g.test(x) == true) {
    // replace all < with &lt;
    var x = x.replace(/</g, "&lt;");
    // write the updated string to the textarea
    document.forms["signupform"]["textarea"].value = x;
  }
}
