function loginFunction() {
    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;

    if ( name === "" || age === "") {
        alert("Please enter all the fields");
    }
    else {
        alert("Successful Login "+name)
    }
}

function submit(event) {
    event.preventDefault(); //preventDefault() stops browsers default behaviour. Because we want to validate the form and check details before sending to server
    let email_variable = document.getElementById("email").value;
    let password_variable = document.getElementById("password").value;

    alert("Form submitted successfully");
}