//Big Take Away
// Two ways to run your javascript. 
// 
//	1. 	For quick testing you can run script right inside a browser
//	2. 	We typically link script files to web pages.  When a script is 
//		linked it automatically runs. 
console.log("Running Script")

var uNames = ["user1@test.com","user2@test.com","user3@test"];
var pWords = ["pword1","pword2","pword3"];

//Task: 	Write a function that takes a user name u and a password p
//			return true if u is in uNames and p matches the password
//			uNames[n] has password pWords[n]

function checkCred(u, p) {

	//Step 1: Loop through uNames and search for u
	for (i = 0; i < uNames.length; i = i + 1) {

		//Step 2: Check each element against passed user name
		if (uNames[i] === u) {
			//Step 3: Check if the password matches
			if (pWords[i] == p) {
				return true
			}
		}


	}

	return false
}

//I need to access hte information from the webpage and then 
//pass it to the function.  If true I update display for a valid
//user, if it is false I don't anything (send an error message)

//x = checkCred("user5@test.com","pword1")
//console.log(x)
//x = checkCred("user1@test.com","pword2")
//console.log(x)
//x = checkCred("user1@test.com","pword1")
//console.log(x)







