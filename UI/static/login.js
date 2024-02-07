// open form
$("#loginBtn").click(function() {
  $("#loginFormContainer").show();
});

$("#signupBtn").click(function() {
  $("#SignUpFormContainer").show();
});

// close form
$("#closeLoginForm").click(function() {
  $("#loginFormContainer").hide();
});

$("#closeSignUpForm").click(function() {
  var element = $('#submissionError')
  element.hide()
  element.text("");
  $("#SignUpFormContainer").hide();
});

// add an event listener for the login button
$("#loginSubmit").click(function(event) {
  var username = $("#username").val();
  var password = $("#password").val();
  // send an AJAX request to the server to check the login credentials
  makeAjaxRequest("POST", "/login", {username: username, password: password},login);
});

$('#registerSubmit').click(function(event) {
  event.preventDefault();
  var username = $('#regUsername').val();
  var password = $('#password1').val();
  var confirmPassword = $('#password2').val();
  var element = $('#submissionError')
  if (password == confirmPassword) {
    makeAjaxRequest("POST", "/register", {username: username, password: password});
    element.show()
    element.text("Successfully Registered. Please Login now.");
  }
  else {
    element.show()
    element.text("Passwords do not match.");
  }
});

function login(response){

window.location.href = '/home';
}
