//Step 1: I going grab all the objects on the page I need for manipulation of page
const login_form = document.querySelector("#login_form")
const login_nav = document.getElementById("login_nav") //if this id does not exist it is set to null
const logout_nav = document.getElementById("logout_nav")
const learn_more_nav = document.getElementById("learn_more_nav")
const elements_nav = document.getElementById("elements_nav")


var users =["user1","user2","user3","user4"]
var pwords = ["pword1","pword","pword3","pword4"]




login_form.addEventListener("submit", (e) => {

	console.log(e)
	e.preventDefault() //Stops page from reloading


	user = login_form["user_name"].value
	password = login_form["user_password"].value
	console.log(user,password)

	//Step 2:
	//Create flag valid = false
	valid = false //BIG IDEA: Have a variable that validates a condidation I can act on later

	//Step 3:
	for (i = 0; i < users.length; i = i + 1) {
		
		if (users[i] === user) {

			if (pwords[i] === password) {
				valid = true //The user exists in system
			}
		}


	} 


	if (valid === true) {
		login_nav.style.display = "none"
		logout_nav.style.display = "block" //display the logout_nav button
		learn_more_nav.style.display = "block"
		elements_nav.style.display = "block"

	}
	else {
		M.toast({html: 'Invalid User'})
	}
	




	//Cleared and closed modal
	//manually close modal
	//General
	const modal = document.querySelector('#login_modal'); 
	//M is the materialize tool box that I have access to since I loaded the resources
	//Modal is the set tools inside M for modals
	//getInstance is a special function that I pass the modal object to
	//close()
	M.Modal.getInstance(modal).close();
	//Clears the content in the modal
	login_form.reset()

});

logout_nav.addEventListener("click",(e) => {

	console.log(e)

	//changed display states of nav bar buttons
	login_nav.style.display = "block"
	logout_nav.style.display = "none" //display the logout_nav button
	learn_more_nav.style.display = "none"
	elements_nav.style.display = "none"
});








