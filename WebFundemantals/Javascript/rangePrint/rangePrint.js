function printRange(start, stop, step){
  // var

    if (step == undefined){
    step = 1;
    }
    if (stop == undefined){
      stop = start;
      start = 0;
    }
    for  (var i = start; i < stop; i+= step){
    console.log(i);
    }
  }
printRange(2, 27, 4);
