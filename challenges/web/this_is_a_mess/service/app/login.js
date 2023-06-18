function login(){
    const username = document.getElementById("uname").value;
    const password = document.getElementById("psw").value;
    if (username=="user" && password=="pass"){
        window.location.href = "fake.html";
        alert("You have successfully logged in.");
    } else{
        alert("YOu are not a surgeon");
    }
}