var days = 60;
function whileYouWait(days) {
        if ( days > 29) {
          console.log(days, "days until my birthday, such a long time ...");
        }
        if ( days < 30 && days > 5) {
          console.log(days, "days until my birthday, getting closer...");
        }
        if ( days < 5 && days > 0 ) {
          console.log(days, " DAYS UNTIL MY BIRHTDAY!");
        }
        if (days == 0) {
          console.log("HAPPY BIRTHDAY TO ME");
        }
}
whileYouWait(8);
