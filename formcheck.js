// formcheck.js
// runs all the client side for
// Jaocb Harrison

if (performance.navigation.type == 1) {
  console.info( "This page is reloaded" );
} else {
  console.info( "This page is not reloaded");
  var oldURL = document.referrer;
  if (oldURL == "http://midn.cyber.usna.edu/~m202556/Project/signup.html" && document.location=="http://midn.cyber.usna.edu/~m202556/Project/signup.html") {
    alert("Username already exists");
    document.getElementById('usernameerrors').innerHTML="Username exists";
    //document.getElementById('usernameerrors').innerHTML="Username already exists";
  }
  if (oldURL == "http://midn.cyber.usna.edu/~m202556/Project/login.html" && document.location=="http://midn.cyber.usna.edu/~m202556/Project/login.html") {
    alert("Invalid credentials");
  }
}





//the overall function to check and validate on submit that my form
//is filled out correctly based on the requirements
function validateForm() {
  //make sure first/last name text box isn't empty
  if (document.forms["signupform"]["fl_name"].value == "") {
    //**********document.getElementById('submit').disabled = true;*****************
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
  var x = document.forms["signupform"]["fl_name"].value;
  var y = document.forms["signupform"]["username"].value;
  var z = document.forms["signupform"]["pswd"].value;
  escapeHtml(x);
  escapeHtml(y);
  escapeHtml(z);
  // var x = document.forms["signupform"]["fl_name"].value;
  // if (/</g.test(x) == true) {
  //   var x = x.replace(/</g, "&lt;");
  //   document.forms["signupform"]["fl_name"].value = x;
  // }
  // if (/>/g.test(x) == true ) {
  //   var x = x.replace(/</g, "&lt;");
  //   document.forms["signupform"]["fl_name"].value = x;
  // }
  // var y = document.forms["signupform"]["username"].value;
  // var z = document.forms["signupform"]["pswd"].value;
}

function validateForm_login() {
  // make sure username text box isn't empty
  var y = document.forms["signupform"]["username"].value;
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  escapeHtml(y);
  var z = document.forms["signupform"]["pswd"].value;
  if (document.forms["signupform"]["pswd"].value == "") {
    document.getElementById('pswderrors').innerHTML="Please fill out Password";
    return false;
  }
  escapeHtml(z);
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
  escapeHtml(x);
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
  var y = document.forms["signupform"]["username"].value;
  escapeHtml(y);
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
  var z = document.forms["signupform"]["pswd"].value;
  escapeHtml(z);
}

function validatePswd_login() {
  if (document.forms["signupform"]["pswd"].value == "") {
    document.getElementById('pswderrors').innerHTML="Please fill out Password";
    return false;
  }
  if (document.forms["signupform"]["pswd"].value != "") {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
  var z = document.forms["signupform"]["pswd"].value;
  escapeHtml(z);
}


function escapeHtml(unsafe) {
  return unsafe
       .replace(/&/g, "&amp;")
       .replace(/</g, "&lt;")
       .replace(/>/g, "&gt;")
       .replace(/"/g, "&quot;")
       .replace(/'/g, "&#039;");
}
