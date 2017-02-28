var quarters;
var slotPull;
function randomChance(quarters) {
    var win = Math.floor(Math.random()*100)+1;//this generates the random winning number
    for (var i = quarters; i > 0; i--) {
        console.log(quarters + "_______starting");
        if (i >= 0) {
            slotPull = Math.floor(Math.random() * 100) + 1; //random number per pull
            console.log(slotPull + "______number pulled on slots")
            if (win == slotPull) {
                var cash = Math.floor(Math.random() * 100) + 1;
                console.log("You won " + cash);
                quarters = (quarters + cash);
                quarters = quarters - 1;
                console.log(win);
                // console.log(cash);
                console.log(quarters);
                return quarters;
            }
            if (win !== slotPull) {
                console.log("You just lost a quarter");
                quarters = (quarters - 1);
                console.log(quarters + "________after loss");
            }
        }
        if (quarters == 0)
            console.log("Your game is over. No more quarters");
    }
    console.log(quarters + " quarters remaining");
}

randomChance(20);
// var cash=Math.floor(Math.random()*50)+51;
// console.log(cash);
