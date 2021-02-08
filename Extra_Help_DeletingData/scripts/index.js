//********************* AUTHENTICATION AND PAGE NAVIGATION ******************/

var uNames = ["edwin.kim@ucc.on.ca"] //stores user names
var pWords = ["1234"] //stores passwords
var uName = null
var pWord = null

var landing_content = document.getElementById("landing")
var home_content = document.getElementById("home")
var drills_content = document.getElementById("drills")
var discussionboard_content = document.getElementById("discussionboard")

home_content.style.display = "none";
drills_content.style.display = "none";
discussionboard_content.style.display = "none";


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
	return false;
}

function login(e) {

    e.preventDefault() //stops page from reloading
    const email =  loginForm["login-email"].value;
    const password = loginForm["login-password"].value;
    loginForm.reset();

    if (checkCred(email,password) === true) {
        uName = email //sets variable uName to email
        pWord = password //sets variable pWord to password
        e.preventDefault() //stops page from reloading
        home_content.style.display = "block";
        landing_content.style.display = "none";
        drills_content.style.display = "none";
        discussionboard_content.style.display = "none";
        console.log(uName)
    }
    else {
        M.toast({html: "Incorrect Email or Password"})
    }
   
    const modal = document.querySelector("#modal-login");
    M.Modal.getInstance(modal).close();
    
}

function logout() {
    uName = null
    pWord = null
    landing_content.style.display = "block";
    home_content.style.display = "none";
    drills_content.style.display = "none";
    discussionboard_content.style.display = "none";
}

function teamInfo() {
    landing_content.style.display = "none";
    home_content.style.display = "block";
    drills_content.style.display = "none";
    discussionboard_content.style.display = "none";
}

function drills() {
    landing_content.style.display = "none";
    home_content.style.display = "none";
    drills_content.style.display = "block";
    discussionboard_content.style.display = "none";
}

function discussionBoard() {
    landing_content.style.display = "none";
    home_content.style.display = "none";
    drills_content.style.display = "none";
    discussionboard_content.style.display = "block";
}

const loginForm = document.querySelector("#login-form")
loginForm.addEventListener("submit",login);

const logout_BTN = document.getElementById("logout_btn")
logout_BTN.addEventListener("click",logout);

const drillsBTN = document.getElementById("drills_btn")
drillsBTN.addEventListener("click",drills);

const teaminfoBTN = document.getElementById("teaminfo_btn")
teaminfoBTN.addEventListener("click",teamInfo);

const discussionboardBTN = document.getElementById("discussionboard_btn")
discussionboardBTN.addEventListener("click",discussionBoard);

//********************* TEAM INFO COLLAPSIBLE FUNCTION (REPETITVE HTML) ******************/

function createCollapsible(teamname) {

    const collapsible =

    `<li>
        <div class="collapsible-header orange darken-4"><b style="color:white;">${teamname}</b></div>
          <div class="collapsible-body">

            <h5>Coaches</h5>

                <div class="row">
                    <div class="col s12 m6">

                        <img src="images/Placeholder.jpg" height="150" width="150">
                        <p>Email: coach1@ucc.on.ca</p>
                        <p>Phone Number: XXX-XXX-XXXX</p>

                    </div>

                    <div class="col s12 m6">

                        <img src="images/Placeholder.jpg" width="150">
                        <p>Email: coach2@ucc.on.ca</p>
                        <p>Phone Number: XXX-XXX-XXXX</p>

                    </div>

                </div>

                <div class="divider"></div>

                <h5>Schedule</h5>

                <table class="highlight">
                    <thead>
                        <tr>
                            <th>Home</th>
                            <th>Away</th>
                            <th>Directions</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>Upper Canada College</td>
                            <td>Royal St. George's College</td>
                            <td><a class="waves-effect waves-light btn orange darken-4">Route</a></td>
                        </tr>
                        <tr>
                            <td>Upper Canada College</td>
                            <td>St. Michael's College School</td>
                            <td><a class="waves-effect waves-light btn orange darken-4">Route</a></td>
                        </tr>
                        <tr>
                            <td>Crescent School</td>
                            <td>Upper Canada College</td>
                            <td><a class="waves-effect waves-light btn orange darken-4">Route</a></td>
                        </tr>
                    </tbody>
                </table>

                <div class="divider"></div>

                <h5>W-L Record</h5>

                <table class="highlight">
                    <thead>
                        <tr>
                            <th>Wins</th>
                            <th>Losses</th>
                            <th>Pct%</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>X</td>
                            <td>X</td>
                            <td>.XXX%</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </li>`

return collapsible

}

const teamInfoDropdown = document.getElementById("collapsibleConstant")

var teams = {

    "collapsibles": [

        {
            "teamname": "U14"
        },

        {
            "teamname": "U16B"
        },

        {
            "teamname": "U16A"
        },

        {
            "teamname": "Varsity"
        }

    ]

}

for (i = 0; i < 4; i = i + 1) {

    teamInfoDropdown.innerHTML += createCollapsible(teams["collapsibles"][i]["teamname"])

}

//********************* FIREBASE PULL ******************/


var firebaseConfig = {

    apiKey: "AIzaSyCYZSqZmt_RTMPqCVHCUhngnESlGAk_f4o",
    authDomain: "extra-help-deletingdata.firebaseapp.com",
    databaseURL: "https://extra-help-deletingdata-default-rtdb.firebaseio.com",
    projectId: "extra-help-deletingdata",
    storageBucket: "extra-help-deletingdata.appspot.com",
    messagingSenderId: "138003468209",
    appId: "1:138003468209:web:b31c08a9358fe2f7b8b790"
        
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

//********************* GENERAL ELEMENTS ******************/

var database = firebase.database();
        
var display = document.getElementById("live")

var submitBTN = document.getElementById("enter_dataBTN")

var postsUpdate = database.ref('posts')

    

/********************** GENERAL FUNCTIONS *****************/

function createCard(username,teamname,message,newPostKey) {


    const card = `<div class="col s12">
                        <div class="card small orange darken-4">
                            <div class="card-content white-text">
                                <span class="card-title"><h4>${username}</h4></span>
                                <h5>${teamname}</h5>
                                <p>Message: ${message}</p>
                                <br>
                                <a class="waves-effect waves-light btn white" id = ${newPostKey} name = ${newPostKey} style="color:black;" onclick = "deleteData()">Delete</a>
                            </div>
                        </div>
                    </div>`
            
    return card
}
            
/********************* WRITING DATA **********************/

function writePostData(userId, username, teamname, message) {

    data = {

        username: username,
        teamname: teamname,
        message: message,

    }

    database.ref('posts/' + userId).set(data);

}

   
var discussionOBJ = []   
function enterData() {

    username = uName

    if (document.getElementById("opbox").value === "") {

        M.toast({html: "Error: You Must Select a Team"}) //error checking: ensures no posts with no teamname label


    } else {

        teamname = document.getElementById("opbox").value
    }

    if (document.getElementById("message").value === "") {

        M.toast({html: "Error: Message Body Must Be Filled"}) //error checking: ensures no posts with empty message body

    } else {

        message = document.getElementById("message").value

        // Get a key for a new post
        var newPostKey = database.ref().child('posts').push().key;
        console.log(newPostKey)

        discussionOBJ.push(newPostKey)
        writePostData(newPostKey,username,teamname,message,newPostKey)
        console.log(discussionOBJ)
    }
            
}
        
submitBTN.addEventListener("click",enterData)


/******************* ON COMMAND *******************/
  
function onChange(snapshot) {

    const data = snapshot.val();
    console.log(snapshot.key)
    d = document.createElement("div")
    d.innerHTML = createCard(data["username"],data["teamname"],data["message"],snapshot.key)
    display.appendChild(d)
    
            
}

postsUpdate.on("child_added", onChange)


function deleteData(e) {

    console.log(e)

   database.ref(`/posts/`).remove()

}