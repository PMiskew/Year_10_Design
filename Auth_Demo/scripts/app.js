var uNames = ["user1@test.com","user2@test.com","user3@test.com"] //stores user names
var pWords = ["pword1","pword2","pword3"] //stores passwords
var permissions = [0,0,0,0] //keeps track of permission levels
var uName = null
var pWord = null


var landing_content = document.getElementById("landing")
var home_content = document.getElementById("home")
home_content.style.display = "none";


function getUser() {
	return uName;

}


function checkCred(name,pwd) {

	for (i = 0; i < uNames.length; i = i + 1) {
		if (uNames[i] === name) {
			if (pWords[i] == pwd) {
				return true;
			}
			return false;
		}
	}
	return false; //password not in list
}

//checkCred("user1","pword1")

/*
Problem: With this approach we cannot easily pass along the 
user name and password.  Since when we load a new page the app.js
gets run again and the result is that the user name and password
gets reset to null.  This means if data is being collected or the 
display is being customized you cannot link it to the user. 
*/
function loginA(e) {
	
    e.preventDefault() //stops page from reloading
    const email =  loginForm['login-email'].value;
    const password = loginForm['login-password'].value;
    console.log(email)
    loginForm.reset();

    if (checkCred(email,password) === true) {
    	uname = email
    	pword = password
    	window.open("landing.html","_self")
    }
    else {
    	const modal = document.querySelector('#modal-login');
		M.Modal.getInstance(modal).close();
    }
    
}

/*
Better: This just updates the page as a whole
*/
function loginB(e) {

    e.preventDefault() //stops page from reloading
    const email =  loginForm['login-email'].value;
    const password = loginForm['login-password'].value;
    loginForm.reset();

    if (checkCred(email,password) === true) {
        uname = email
        pword = password
        e.preventDefault() //stops page from reloading
        home_content.style.display = "block";
        landing_content.style.display = "none";
    }
   
    const modal = document.querySelector('#modal-login');
    M.Modal.getInstance(modal).close();
    
}

function logout() {
    console.log("LOGOUT")
    home_content.style.display = "none";
    landing_content.style.display = "block";
    uName = null
    pWord = null
}


//Change this to LoginA and LoginB to simulate new page load verse 
//same page
const loginForm = document.querySelector('#login-form')
loginForm.addEventListener('submit',loginB);

const logout_BTN = document.getElementById("logout_btn")
logout_BTN.addEventListener('click',logout)


