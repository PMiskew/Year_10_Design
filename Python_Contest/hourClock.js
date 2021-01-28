val = "09:30"

//JS - Substring different
h = val.substring(0,2)


h = parseInt(h)

m = val.substring(3,5)	

timeOfDay = "AM" 

if (h >= 12 && h <= 23) {
	timeOfDay = "PM"
	h = h - 12
}
if (h == 0) {
	h = 12
}


console.log(h+":"+m+" "+timeOfDay)