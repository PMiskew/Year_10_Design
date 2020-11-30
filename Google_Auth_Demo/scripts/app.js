function toggleSignIn() {
            if (!firebase.auth().currentUser) {
        
                var provider = new firebase.auth.GoogleAuthProvider();
        
                provider.addScope('https://www.googleapis.com/auth/plus.login');
        
                firebase.auth().signInWithRedirect(provider);
            } 
            else 
            {
                firebase.auth().signOut();
            }

            document.getElementById('quickstart-sign-in').disabled = true;
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
            var displayName = user.displayName;
            var email = user.email;
            var emailVerified = user.emailVerified;
            var photoURL = user.photoURL;
            var isAnonymous = user.isAnonymous;
            var uid = user.uid;
            var providerData = user.providerData;
            document.getElementById('quickstart-sign-in-status').textContent = 'Signed in';
            document.getElementById('quickstart-sign-in').textContent = 'Sign out';
            document.getElementById('quickstart-account-details').textContent = JSON.stringify(user, null, '  ');
        } 
        else {
            document.getElementById('quickstart-sign-in-status').textContent = 'Signed out';
            document.getElementById('quickstart-sign-in').textContent = 'Sign in with Google';
            document.getElementById('quickstart-account-details').textContent = 'null';
            document.getElementById('quickstart-oauthtoken').textContent = 'null';
        }
            document.getElementById('quickstart-sign-in').disabled = false;
    });

    document.getElementById('quickstart-sign-in').addEventListener('click', toggleSignIn, false);
}
