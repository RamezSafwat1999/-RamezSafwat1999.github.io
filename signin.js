/* ======================================================================
  Author Custom JavaScript
====================================================================== */
// Loop through Array of Objects
var objPeople = [{ // Object @ 0 index
        email: "41710191",
        password: "41710191"
    },
    { // Object @ 1 index
        email: "41710192",
        password: "4170192"
    },
    { // Object @ 2 index
        email: "ramez@acu",
        password: "ramez"
    },
    { // Object @ 3 index
        email: "12345678    ",
        password: "12345678"
    },

]

function getInfo() {
    var email = document.getElementById('email').value
    var password = document.getElementById('password').value

    for (var i = 0; i < objPeople.length; i++) {
        // check is user input matches email and password of a current index of the objPeople array
        if (email == objPeople[i].email && password == objPeople[i].password) {
            console.log(email + " is logged in!!!")
                // stop the function if this is found to be true
            return
        }
    }
    console.log("incorrect email or password")
}