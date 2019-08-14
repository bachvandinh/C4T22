var btnDelete = document.getElementsByClassName("btn_del");
for (i = 0; i<btnDelete.length; i++)
{
    var Del = btnDelete[i];
    Del.addEventListener('click', function(e) {
        console.log(e.target);
        var btn = e.target;
        var div = btn.parentNode;
        console.log(div);
        div.remove();
    })
}