console.log("something")
function signOut() {

	auth.signOut();

}

function signIn() {
	console.log("Sigining IN")
	var provider = new auth.GoogleAuthProvider();
	
	auth.signInWithRedirect(provider).then(function(result) { 
		
	});
} // end signin 

