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
  }
  // if the user came from login.html and is currently in login.html that means the login credentials were invalid so send an alert saying they were invalid
  if (oldURL == "http://midn.cyber.usna.edu/~m202556/project02/login.html" && document.location=="http://midn.cyber.usna.edu/~m202556/project02/login.html") {
    alert("Failed logon attempt");
  }
}

// function that validates the entered CAPTCHA code, reloads the login page if there's an error
function checkform(theform){
var why = "";

if(theform.CaptchaInput.value == ""){
why += "- Please Enter CAPTCHA Code.\n";
//window.location.replace("http://midn.cyber.usna.edu/~m202556/project02/login.html")

}
// print the error message if no value is entered
if(theform.CaptchaInput.value != ""){
if(ValidCaptcha() == false){
why += "- The CAPTCHA Code Does Not Match.\n";
}
}
if(why != ""){
console.log(why);
alert(why);
window.location.replace("http://midn.cyber.usna.edu/~m202556/project02/login.html")
return false;
}
if(why == ""){
  console.log(why);
  return true;
}
}


// Validate input against the generated number
function ValidCaptcha(){
var str1 = removeSpaces(document.getElementById('txtCaptcha').value);
var str2 = removeSpaces(document.getElementById('CaptchaInput').value);
console.log(str1);
console.log(str2);
if (str1 == str2){
return true;
// if strings don't match reload the login page with invalid credentials
}else{
//window.location.replace("http://midn.cyber.usna.edu/~m202556/project02/login.html")
return false;
}
}

// Remove the spaces from the entered and generated code
function removeSpaces(string){
return string.split(' ').join('');
}


//the overall function to check and validate on submit that the signup form is filled out correctly based on the requirements
function validateForm() {
  //make sure first/last name text box isn't empty
  if (document.forms["signupform"]["fl_name"].value == "") {
    document.getElementById('fl_name_errors').innerHTML="Please fill out first & last name";
    return false;
  }
  // make sure first/last name is not more than 50 characters
  var x = document.forms["signupform"]["fl_name"].value;
  if (x.length > 50) {
    document.getElementById('fl_name_errors').innerHTML="Maximum of 50 characters for name";
    return false;
  }
  // special character checking
  var x = document.forms["signupform"]["fl_name"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('fl_name_errors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
  // make sure username text box isn't empty
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  // make sure username is not more than 30 characters
  var x = document.forms["signupform"]["username"].value;
  if (x.length > 30) {
    document.getElementById('usernameerrors').innerHTML="Maxiumum of 30 characters for username";
    return false;
  }
  // special character checking
  var x = document.forms["signupform"]["username"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('usernameerrors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
  // make sure password is not more than 30 characters
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
  // special character checking
  var x = document.forms["signupform"]["pswd"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('pswderrors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
}

// function to validation the login form on submit
function validateForm_login() {
  // make sure username text box isn't empty
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  // make sure username isn't more than 30 characters
  var x = document.forms["signupform"]["username"].value;
  if (x.length > 30) {
    document.getElementById('usernameerrors').innerHTML="Maxiumum of 30 characters for username";
    return false;
  }
  // special character checking
  var x = document.forms["signupform"]["username"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('usernameerrors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
  // make sure password text box isn't empty
  if (document.forms["signupform"]["pswd"].value == "") {
    document.getElementById('pswderrors').innerHTML="Please fill out Password";
    return false;
  }
  // make sure password isn't more than 30 characters
  var y = document.forms["signupform"]["pswd"].value;
  if (y.length > 30) {
    document.getElementById('pswderrors').innerHTML="Maxiumum of 30 characters for password";
    return false;
  }
  // special character checking
  var x = document.forms["signupform"]["pswd"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('pswderrors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
}

// function for validating just the first/last name textbox onblur
// and that it gets filled in correctly
function validate_fl_name() {
  // special character checking
  var x = document.forms["signupform"]["fl_name"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('fl_name_errors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
  // if the textbox is empty return an error message
  if (document.forms["signupform"]["fl_name"].value == "") {
    document.getElementById('fl_name_errors').innerHTML="Please fill out first & last name";
    return false;
  }
  // make sure first/last name isn't more than 50 characters
  var x = document.forms["signupform"]["fl_name"].value;
  if (x.length > 50) {
    document.getElementById('fl_name_errors').innerHTML="Maximum of 50 characters for name";
    return false;
  }
  // if all requirements are met return true and remove error
  var y = document.forms["signupform"]["fl_name"];
  if (x.length < 51 && (y.value!="") && (/[!@#$%^&*(),.?":{}|<>]/g.test(x) != true) == true) {
    document.getElementById('fl_name_errors').innerHTML="";
    return true;
  }
}

// function for validating just the username textbox onblur
// and that it gets filled in correctly
function validateUsername() {
  var x = document.forms["signupform"]["username"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('usernameerrors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
  // if the textbox is empty return an error message
  if (document.forms["signupform"]["username"].value == "") {
    document.getElementById('usernameerrors').innerHTML="Please fill out Username";
    return false;
  }
  // make sure username isn't more than 30 characters
  var x = document.forms["signupform"]["username"].value;
  if (x.length > 30) {
    document.getElementById('usernameerrors').innerHTML="Maxiumum of 30 characters for username";
    return false;
  }
  // if all requirements are met return true and remove error
  var y = document.forms["signupform"]["username"]
  if (x.length < 31 && (y.value!="") && (/[!@#$%^&*(),.?":{}|<>]/g.test(x) != true) == true) {
    document.getElementById('usernameerrors').innerHTML="";
    return true;
  }
}

// function for validating just the password textbox onblur
// and that it gets filled in correctly
function validatePswd() {
  // special character checking
  var x = document.forms["signupform"]["pswd"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('pswderrors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
  var x = document.forms["signupform"]["pswd"].value;
  //if the password is less than length of 6 return error
  if (x.length < 6) {
     document.getElementById('pswderrors').innerHTML="Password must be at least 6 characters";
     return false;
  }
  // make sure the password isn't more than 30 characters
  if (x.length > 30) {
    document.getElementById('pswderrors').innerHTML="Maxiumum of 30 characters for password";
    return false;
  }
  //if there's no digit return an error
  if (/\d/.test(x) == false) {
    document.getElementById('pswderrors').innerHTML="Password must contain at least 1 number";
    return false;
  }
  //check that password requirements are met to clear error box
  if (x.length > 5 && /\d/.test(x) && x.length < 31 && (/[!@#$%^&*(),.?":{}|<>]/g.test(x) != true) == true) {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
}

// function for validating the password textbox on the login page
function validatePswd_login() {
  // special character checking
  var x = document.forms["signupform"]["pswd"].value;
  if (/[!@#$%^&*(),.?":{}|<>]/g.test(x) == true) {
    document.getElementById('pswderrors').innerHTML='These characters are not allowed: !@#$%^&*(),.?":{}|<>';
    return false;
  }
  // make sure text is entered into the password text box
  if (document.forms["signupform"]["pswd"].value == "") {
    document.getElementById('pswderrors').innerHTML="Please fill out Password";
    return false;
  }
  // make sure password isn't more than 30 characters
  var x = document.forms["signupform"]["pswd"].value;
  if (x.length > 30) {
    document.getElementById('pswderrors').innerHTML="Maxiumum of 30 characters for password";
    return false;
  }
  // if all requirements are met return true and remove error
  var y = document.forms["signupform"]["pswd"]
  if (x.length < 31 && (y.value!="") && (/[!@#$%^&*(),.?":{}|<>]/g.test(x) != true) == true) {
    document.getElementById('pswderrors').innerHTML="";
    return true;
  }
}
