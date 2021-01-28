
/*
With JS we declare variables by writing them down with nothing infront
or use var or let.  This affects the scope. 
/*/
x1 = 2
y1 = 4
x2 = 4
y2 = 8

r = Math.pow(((y2 - y1)*(y2 - y1) + (x2 - x1)*(x2 - x1)),0.5)
a = 3.1519 * r * r
//ROUNDING A LITTLE 
a = a * 1000 //moves deciaml over
a = Math.round(a)
a = a /1000
console.log(a)

/*
var num = 5.56789;
var n = num.toFixed(2);
*/