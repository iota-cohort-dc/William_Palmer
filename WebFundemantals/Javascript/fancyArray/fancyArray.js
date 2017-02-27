var arr = ["James", "Jill","Jane","Jack"];
function fancyArray(sym, arr){
  for (var i = 0; i < arr.length; i++){
    console.log(sym + i, arr[i]);
  }
}
fancyArray("x---> ",arr);
