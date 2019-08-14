function startClick() { //callBack
    console.log("Clicked");
};

var btn = document.getElementById("btn");
btn.textContent = "Stop";
console.log(btn);
btn.addEventListener('click', function(e) {
    console.log(e)
});


var search = document.getElementById("search");
search.value = "";
console.log(search);
search.style.backgroundColor = "pink";

var menu = document.getElementById("menu");
var newItem = document.createElement("li");  // <li></li>
newItem.textContent = "sushi";
menu.appendChild(newItem);
var liList= document.getElementsByTagName("li");
var firstList = liList[0];
firstList.remove();
console.log(liList)