//the overall function to check and validate on submit that my form
//is filled out correctly based on the requirements
function validateForm() {
  //make sure first/last name text box isn't empty
  if (document.forms["signupform"]["flname"].value == "") {
    document.getElementById('flnameerrors').innerHTML="Please fill out first & last name";
    return false;
  }
  // make sure username text box isn't empty
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  // make sure email isn't empty
  if (document.forms["signupform"]["email"].value == "") {
    document.getElementById('emailerrors').innerHTML="Please fill out valid email address";
    return false;
  }
  if (document.forms["signupform"]["textarea"].value == "") {
    document.getElementById('textareaerrors').innerHTML="Please describe your Why in life";
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
  var z = document.forms["signupform"]["email"].value;
  //if the email address doesn't match the requirements of a valid email address
  // with a minimum of example@example then return an error with valid email addresses
  if (/[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*/.test(z) == false) {
    document.getElementById('emailerrors').innerHTML="Invalid email: example@cyber.com, example@cyber, example@cyber.com.regex are examples of valid email addresses";
    return false;
  }
  // if the email address is valid then erase the error message
  if (/[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*/.test(z) == true) {
    document.getElementById('emailerrors').innerHTML="";
    return true;
  }
}

// function for validating just the first/last name textbox onblur
// and that it gets filled in
function validateFLName() {
  // if the textbox is empty return an error message
  if (document.forms["signupform"]["flname"].value == "") {
    document.getElementById('flnameerrors').innerHTML="Please fill out first & last name";
    return false;
  }
  // if textbox is not empty erase the error message
  if (document.forms["signupform"]["flname"].value != "") {
    document.getElementById('flnameerrors').innerHTML="";
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

function validateEmail() {
  var x = document.forms["signupform"]["email"].value;
  //if the email address doesn't match the requirements of a valid email address
  // with a minimum of example@example then return an error with valid email addresses
  if (/[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*/.test(x) == false) {
    document.getElementById('emailerrors').innerHTML="Invalid email: example@cyber.com, example@cyber, example@cyber.com.regex are examples of valid email addresses";
    return false;
  }
  // if the email address is valid then erase the error message
  if (/[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*/.test(x) == true) {
    document.getElementById('emailerrors').innerHTML="";
    return true;
  }
}
