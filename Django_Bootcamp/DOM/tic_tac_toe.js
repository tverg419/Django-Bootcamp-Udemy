alert("Welcome to TTT")
// Restart Game
var restart = document.querySelector('#b');

// Grab all spaces
var spaces = document.querySelectorAll("td");

// Clear all spaces
function clearSpaces(){
  for (var i = 0; i < spaces.length; i++) {
    spaces[i].textContent = '';
  }
}
restart.addEventListener('click',clearSpaces)

// Change Marker
function changeSpace(){
  if(this.textContent === ''){
    this.textContent = 'X';
  } else if(this.textContent === 'X'){
    this.textContent = 'O';
  } else{
    this.textContent = '';
  }
};

// Assign each space an event
for (var i = 0; i < spaces.length; i++) {
  spaces[i].addEventListener('click', changeSpace);
}
