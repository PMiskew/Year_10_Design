//Step 1: I going grab all the objects on the page I need for manipulation of page
const login_form = document.querySelector("#login_form")
const login_nav = document.getElementById("login_nav") //if this id does not exist it is set to null
const logout_nav = document.getElementById("logout_nav")
const learn_more_nav = document.getElementById("learn_more_nav")
const elements_nav = document.getElementById("elements_nav")

const homecontent = document.getElementById("home_content")
console.log(homecontent)


//set users to empty: We only need one collection since it will hold an object that has both user name and 
//password

var users =[]

//or
userNames = []
passwords = []

cuser = ""

/*
//ONCE: Does the pull once when called.  If you add a new user and change users you then need to run this
//call again to update the users data

database.ref('/users/').once('value').then((snapshot) => {
			
			//option 1: Make a list of objects that hold both username and password
			users = snapshot.val()
			///console.log(users)
		
	
			//option 2: create two parallel lists
			for (key in users) {
				userNames.push(users[key]["userName"])
				passwords.push(users[key]["password"])

			}		

			console.log(userNames)
			console.log(passwords)

			//RECOMMEND OPTION 1
});

//*/

//ON: Creates a connection with the page this will run once on the load of a page and then automatically
//		run again when the database changes
database.ref('/users/').on('value',(snapshot) => {
			users = snapshot.val()
			///console.log(users)
		
			//This is a for each loop that will loop through a collection
			//the same as C.hasNext()
			//This short hand loop form just automatically goes through all elements in 
			//the collection - it is designed to give me the key for every value as it passeses
			//it
			for (key in users) {
				userNames.push(users[key]["uname"])
				passwords.push(users[key]["pword"])

			}		

			console.log(userNames)
			console.log(passwords)
});


//*/

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
				cuser = users[i]
				if (cuser === "") {
						console.log("NO USER")
				}
				else {
					console.log(cuser)
				}

			}
		}


	} 


	if (valid === true) {
		login_nav.style.display = "none"
		logout_nav.style.display = "block" //display the logout_nav button
		learn_more_nav.style.display = "block"
		elements_nav.style.display = "block"

		homecontent.style.display = "block"


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
	cuser = ""
	homecontent.style.display = "none"
});








