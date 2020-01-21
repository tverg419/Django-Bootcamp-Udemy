var firstName = prompt("What is your first name?")
var lastName = prompt("What is your last name?")
var age = prompt("How old are you?")
var height = prompt("How tall are you? Please answer in centimeters")
var pet = prompt("What is the name of your favorite pet?")
alert("Thank you for your information!")

if (firstName[0].lower == lastName[0].lower) {
  var cond1 = true;
}
if (age > 20 && age < 30) {
  var cond2 = true;
}
if (height >= 170) {
  var cond3 = true;
}
if (pet[pet.length-1] == "y") {
  var cond4 = true;
}

if (cond1 = cond2 = cond3 = cond4) {
  console.log("Hello Comrade!");
} else {
  console.log("Nothing to see here");
}
