
//Faking It:
//This means storing all the data and user information
//in lists so it is there when the program starts. 

var uNames = ["user1@test.com","user2@test.com"];
var pWords = ["pword1","pword2"];

//Write a function call checkCred that takes two parametetesr
//
// u a string representing user name
// p a string representing password
//
// checkCred will check to see that u is contained in uNames
// and if u exists check that p matches the correct password
// returns true if the user name and password are valid, false
// otherwise. 

function checkCred(u, p) {
	
	//Loops through each element in uNames 
	for (i = 0; i < uNames.length; i = i + 1) {
		
		//Checks if the user name u exists
		if (uNames[i] === u) {

			if (pWords[i] == p) {
				return true; //Found it I am done!
			}


		}
	}

	return false; //user name not in system. 

}

result = checkCred("user1@test.com","pword1")
console.log(result)