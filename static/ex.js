// Client-side validation using JavaScript
document.getElementById("registrationForm").onsubmit = function(event) {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    if (password !== confirmPassword) {
        alert("Passwords do not match");
        event.preventDefault(); // Prevent form submission
    }
};

function validateForm() {
    var email = document.getElementById("email").value;
    var emailError = document.getElementById("emailError");

    Regular expression for email validation
    var emailRegex = /^[^\s@]+@[^\s@]+\.(email\.com|outlook\.com|yahoo\.com)$/;

    if (!emailRegex.test(email)) {
        emailError.textContent = "Please enter a valid email address with domain email.com, outlook.com, or yahoo.com.";
        return false; // Prevent form submission
    } else {
        emailError.textContent = ""; // Clear error message
        return true; // Allow form submission
    }
}