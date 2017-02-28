var arr = [1, "apple", -3, "orange", 0.5];

function numbersOnly(arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (typeof arr[i] === "number") {
            newArr.push(arr[i]);
        }
    }
    console.log(newArr);
    return newArr;
}

numbersOnly(arr);
