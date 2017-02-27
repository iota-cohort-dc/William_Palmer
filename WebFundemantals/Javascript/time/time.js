function timeOfDay(hour, minute, period) {
    // var hour = 12;
    // var minute = 0;
    // var period = "AM";
    var estimate = "";
    var tod = "";
    if (minute < 60 && minute > 50) {
        estimate = "5 til";
        hour = (hour + 1);
    } else if (minute > 0 && minute < 10) {
        estimate = "5 after";
    }
    if (minute >= 10 && minute <= 20) {
        estimate = "a quarter after";
    }
    if (minute >= 40 && minute <= 50) {
        estimate = "a quarter til";
        hour = (hour + 1);
    }
    if (minute > 20 & minute < 40) {
        estimate = "half past";
    }
    if (period == "AM") {
        tod = "in the morning";
    } else {
        tod = "in the evening";
    }
    if (hour === 12 && minute === 0 && period === "PM") {
        estimate = "";
        hour = "";
        tod = "noon";
    }
    if (hour === 12 && minute === 0 && period === "AM") {
        estimate = "";
        hour = "";
        tod = "midnight";
    }
    if (hour < 5 && hour > 1 && period == "PM") {
        tod = "in the afternoon";
    } else if (hour >= 1 && hour < 12 && period == "AM") {
        tod = "in the morning";
    }

    console.log("It is", estimate, hour, tod);
}
timeOfDay(2, 0, "PM");
