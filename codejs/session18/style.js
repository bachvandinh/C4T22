var rightColorInd;
var score;
function generateColor() {
    var r = Math.floor(Math.random()*255);
    var g = Math.floor(Math.random()*255);
    var b = Math.floor(Math.random()*255);
    console.log(r,g,b); //random chon mau bong

    var colorString = `rgb(${r},${g},${b})`;
    console.log(colorString);
    var colorStringEl = document.getElementById("colorString").textContent;
    var ballEl = document.getElementById("ballContainer");
    var ballEls = ballEl.getElementsByClassName("ball");
    // console.log(ballEls);

    var rightColorInd = Math.floor(Math.random()*3);
    ballEls[rightColorInd].style.backgroundColor = colorString;

    for (var i = 0; i<ballEls.length; i++)
    {
        if (i != rightColorInd) 
        {
            var error1 = Math.random()* 100 - 25;
            var x = Math.random();
            if (x > 0,5)
            {
                error1 = -error1;
            }
            var error2 = Math.random()* 100 - 25;
            var x = Math.random();
            if (x > 0,5)
            {
                error2 = -error2;
            }
            var error3 = Math.random()* 100 - 25;
            var x = Math.random();
            if (x > 0,5)
            {
                error3 = -error3;
        }
        var wrongColor = `rgb(${r+error1},${g+error2},${b+error3})`
        ballEls[i].style.backgroundColor = wrongColor;
        }
    }
}
generateColor();

var ballEl = document.getElementById("ballContainer");
var ballEls = ballEl.getElementsByClassName("ball");
for (var i = 0; i<ballEls.length; i++){
    ballEls[i].addEventListener('click', function(e){
        var ball = e.target;
        // console.log(ball);
        var ballIndex = ball.getAttribute("index");
        if (ballIndex == rightColorInd)
        {
            console.log("Correct");
            // score = score +1;
            // console.log(score);
        }
        else{
            console.log("Wrong");
            // score = 0;
            // console.log(score);
        }
    })
}