
// var so = document.getElementsByClassName("song");
// console.log(so);
// var title = document.getElementsByClassName("title");
// console.log(title);
// var ar = document.getElementsByClassName("artist");
// console.log(ar);

var so = document.getElementById("song_container");
var sr = so.getElementsByClassName("song");
console.log(sr);
var ti = so.getElementsByClassName("title");
console.log(ti);

var btnDelete = document.getElementsByClassName("del");
for (i = 0; i<btnDelete.length; i++)
{
    var Delete = btnDelete[i];
    Delete.addEventListener('click', function(e){
        console.log(e.target);
        var btn = e.target;
        var div = btn.parentNode;
        console.log(div);
        div.remove();
    });


}

var btnEdit = document.getElementsByTagName("div")
for (i = 0; i<btnEdit.length; i++)
{
    var Edit = btnEdit[i];
    Edit.addEventListener('click', function(e){
        console.log(e.target);
        var btn = e.target;
        var div = btn.parentNode;
        console.log(div.song_id)

    })
}

var btnMore = document.getElementsByTagName("div");
for (k=0; k<btnMore.length; k++)
{
    var More = btnMore[k];
    More.addEventListener('click', function(e){
        console.log(e.target);
        var btn = e.target;
        var div = btn.parentNode;
        console.log(div.textContent);
        })
}