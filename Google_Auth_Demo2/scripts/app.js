function toggleSignIn() {

    if (!firebase.auth().currentUser) {

        var provider = new firebase.auth.GoogleAuthProvider();

        provider.addScope('https://www.googleapis.com/auth/plus.login');

        firebase.auth().signInWithRedirect(provider);
    } 
    else {
        firebase.auth().signOut();
    }

}


function initApp() {

    var firebaseConfig = {
        apiKey: "AIzaSyBHb_A01mFDUD5UsynaPa2t0XdJ6-N_r3c",
        authDomain: "fir-project-elements.firebaseapp.com",
        databaseURL: "https://fir-project-elements.firebaseio.com",
        projectId: "fir-project-elements",
        storageBucket: "fir-project-elements.appspot.com",
        messagingSenderId: "223980177694",
        appId: "1:223980177694:web:24c0031231e40f851ba10f",
        measurementId: "G-VTR86DL857"
    };

    firebase.initializeApp(firebaseConfig);
   
    firebase.auth().getRedirectResult().then(function(result) {
            
            if (result.credential) 
            {
                var token = result.credential.accessToken;
                document.getElementById('quickstart-oauthtoken').textContent = token;
            } 
            else 
            {
                document.getElementById('quickstart-oauthtoken').textContent = 'null';
            }

            var user = result.user;
    
    }).catch(function(error) {
       
        var errorCode = error.code;
        var errorMessage = error.message;
        var email = error.email;
        var credential = error.credential;

        if (errorCode === 'auth/account-exists-with-different-credential') {
            alert('You have already signed up with a different authorization provider for this email.');
        } 
        else {
            console.error(error);
        }
    });

    firebase.auth().onAuthStateChanged(function(user) {
    
        if (user) {
            console.log("IN")
        } 
        else {
            console.log("OUT")
        }
    });

    document.getElementById('quickstart-sign-in').addEventListener('click', toggleSignIn, false);
}
