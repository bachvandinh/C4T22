var el = document.getElementById("btn_search");

console.log(el);

var rects = document.getElementsByClassName("rect");
for (var i = 0; i<rects.length; i++)
{
    console.log(rects[i]);
}

var divs = document.getElementsByTagName("div");
for (var t = 0; t < divs.length; t++)
{
    console.log(divs[t])
}