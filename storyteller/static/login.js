function validate(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(username == "admin@gmail.com" && password == "user123")
    {
        alert ("login successful!!")
    }
    else
    {
        alert("login failed")
    }
}
