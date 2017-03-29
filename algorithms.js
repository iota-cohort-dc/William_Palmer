/* Algorithms and how they work.*/
// Second to Last /*(how to find the second to last item in an array)*/
// BASIC THIRTEEN ALGORITHMS:
// /*-------------------------------------------*/
// /*Print 1-255. Print all intergers from 1 to 255*/
// function print1_255(){
//   for (var i=0;i<256;i++){
//     console.log(i);
//   }
// }
// print1_255();
//
//
// /*-------------------------------------------*/
// /*Return an array with all numbers from 1-255*/
// function print1_255(){
//   var arr=[];
//   for (var i=0;i<256;i++){
//     arr.push(i);
//   }
//   return arr;
// }
// print1_255();
//
//
// /*-------------------------------------------*/
// /*Print all odd integers from 1-255*/
// function printOdd(){
//   for( var i=0;i<256; i++){
//     if (i % 2 !==0){
//       console.log(i);
//     }
//   }
// }
// printOdd();
//
//
// /*-------------------------------------------*/
// /*Print all even integers from 1-255*/
// function printEven(){
//   for( var i=0;i<255; i++){
//     if (i % 2 ===0){
//       console.log(i);
//     }
//   }
// }
// printEven();
//
//
// /*-------------------------------------------*/
// /*Get the sum off all even integers from 1-255*/
// function sumEven(){
//   var sum=0;
//   for( var i=0;i<255; i++){
//     if (i % 2 ===0){
//       sum+=i;
//     }
//   }
//   return sum;
// }
// sumEven();
//
//
// /*-------------------------------------------*/
// /*Print intergers from 1-255 and the sum of the intergers*/
// function printSum0_255(){
//   var sum = 0;
//   for var(i=0;i<256>i++){
//     sum=sum+=i;
//   }
//   return sum;
// }
// printSum0_255();
//
//
// /*-------------------------------------------*/
// /*Iterate and array (Print all values of a given array.)*/
// function iterateArray(arr){
//   for(var i = 0; i<arr,length; i++){
//     sum+=arr[i];
//   }
//   return sum;
// }
// iterateArray();
//
//
// /*-------------------------------------------*/
// /*Print the largest value of a given array*/
// function printMax(){
//   var max=[0];
//   for(var i = 0: i < arr.length;i++){
//     if (arr[i]>max){
//       max=arr[i]
//     }
//   }
//   return max;
// }
// printMax();
//
//
// /*-------------------------------------------*/
// /*Get the average of an array and print it*/
// function getAvg(){                      function getAvg(){
//   var sum = 0;                            var sum = 0;
//   var avg = 0;                            for (var i = 0;i<arr.length); i++){
//   for (var i = 0;i<arr.length);i++){        sum = sum + arr[i];
//     sum=sum+arr[i];                         }
//   }                                        return sum/arr.length;
//   avg=sum / arr.length;                   }
//   /*can also use 'return sum/arr.length;'
//   and not include the return avg; code
//   on the next line below.*/
//   return avg;
// }
// getAvg();
//
//
// /*-------------------------------------------*/
// /*Create and array with off intergers from 1-255*/
// function arrayOdd(){
//   var arr=[];
//   for (var i=1;i<arr.length;i++){
//     /*if given a defined range, like 1-57, should use for(var i=1;i<58;i++)
//      if the range is 16-395, should use for(var i=17;1<396;i++)
//      if the range is 4-66, shold use (var i=5;i<66;i++)*/
//     if(i % 2 !== 0){/*is this modulus is = 0, the number is even*/
//       arr.push(i);
//     }
//   }
//   return arr;
// }
// arrayOdd();
//
//
// /*-------------------------------------------*/
// /*Square the values of an array*/
// function squreArray(){
//   for( var i=0;i<arr.length;i++){
//     arr[i]=arr[i]*arr[i];
//   }
//   return arr;
// }
// squareArray();
//
//
// /*-------------------------------------------*/
// /*count all the values in an Array that are greater than Y*/
// function greaterThanY(arr, Y){
//   var count=0;
//   for( var i=0;i<arr.length;i++){
//     if(arr[i]>y){
//       count++;
//     }
//   }
//   return count;
// }
// greaterThanY([3,7,2,5,3,7,9], 5);
//
//
// /*-------------------------------------------*/
// /*Zero out integers that are less than zero*/
// function lessThanZero(arr){
//   for (var i=0;i<arr.length;i++){
//     if (arr[i]<0){
//       arr[i]=0;
//     }
//   }
//   return arr;
// }
// lessThanZero();
//
//
// /*-------------------------------------------*/
// /*print the MIN, MAX, and AVG of a given array*/
// function minMaxAvg(arr){
//   var min=[0];
//   var max=[0];
//   var sum=[0];
//   for (vari=1;i<arr.length;i++){
//     /*set i=1 because setting because settting it to 0 will result
//     in comapring the first position of the array to the first position
//     since min, max and sum are all set to the first position of the given array.*/
//     if (arr[i]>max){
//       max=arr[i];
//     }
//     if (arr[i]<min;){
//       min=arr[i];
//     }
//     sum = sum + arr[i];
//   }
//   var avg=sum/arr.length;
//   var newarr=[,min,max,avg];
//   return newarr;
// }
// minMaxAvg();
//
//
// /*-------------------------------------------*/
// /*Swap the first and last values of a given array. Array length has the have
// a minimum of 2 to work.*/
// function swapFirstLast(arr){
//   var temp=arr[0];
//   arr[0] = arr[arr.length-1];
//   arr[arr.length-1]=temp;
//   return arr;
// }
// swapFirstLast();
//
//
// /*-------------------------------------------
// Replace any negative number in an array with a string, use the string "Mongo"*/
// function stringToNumber(arr){
//   for (var i=0;i<arr.length;i++){
//     if (arr[i]<0){
//       arr[i]="Mongo";
//     }
//   }
//   return arr;
// }
// stringToNumber();
// /*-------------------------------------------*/
// function secondToLast(arr, n){
//   if(arr.length < 2){
//     return null;
//   }
//   else {
//     return arr[arr.length -2];
//     }
// }
//  secondtoLast();
//
// /*-------------------------------------------*/
// /*Reverse the elements in an array*/
// function reverseArray(arr){
//   var temp;
//   for(var i=o;i<arr.length/2; i++){
//     temp = arr[i];
//     arr[i]=arr[arr.length -1];
//     arr[arr.length-1]=temp;
//   }
//   return arr;
// }
// reverseArray();
//
// /*-------------------------------------------*/
// /*Remove blacnkd from a string*/
// function removeBlanks(str){
//   var newstr="";
//   for (var i=0;i<str.length;i++){
//     if(str[i]!==""){
//       newstr += str[i];
//     }
//   }
//   return newstr;
// }
// removeBlanks("Th eFac tC  at");
// /*-------------------------------------------*/
// /*SLL remove Negatives*/
// function ListNode(val){
//   this.val=value;
//   this.next=null;
// }
// function SLL(){
//   this.head=null;
//   this.removeNeg = function(val){
//     if (!this.head){
//       return False;
//     }
//     var current=.this.head;
//     var temp = null;
//     while(this.head<0){
//       this.head = current.next;
//       current=this.head
//       if(current.val < 0){
//         temp = current.next;
//         current = null;
//         current = temp;
//       }
//       if (current.next == null){
//         if (current.next.val < 0){
//           current.next = null;
//         }
//       }
//       current = current.next;
//     }
//   }
// }
/*-------------------------------------------*/
/*SLL remove Negatives*/
// function ListNode(val){
//   this.val=val;
//   this.next=null;
// }
// function SLL(){
//   this.head=null;
//   this.addFront = function(val){
//     var Node = new ListNode(val);
//     currentNode = this.head;
//     if (!currentNode){
//       this.head = Node
//       // console.log(Node)
//       return Node;
//     }
//     while(currentNode.next){
//       currentNode=currentNode.next;
//     }
//     currentNode.next=Node;
//     var current = new ListNode(val);
//
//     return this.head;
//   }
//
// //   this.removeNeg = function(val){
// //     if (!this.head){
// //       return False;
// //     }
// //     var current= this.head;
// //     var temp = null;
// //     while(this.head<0){
// //       this.head = current.next;
// //       current=this.head
// //     }
// //     while(current.next){
// //       if(curent.next<0){
// //         temp=current.next.next;
// //         current.next.next=null;
// //         current.next=temp
// //       }
// //       current=current.next;
// //     }
// //
// //     console.log(SLL);
// //   }
// }
// var list=new SLL;
// // this.ListNode()
// list.addFront(10)
// list.addFront(3)
// list.addFront(8)
// list.addFront(10)
// console.log(list.head);

/*-------------------------------------------*/
/*SLL concatenate Slls*/
function ListNode(val){
  this.val=val;
  this.next=null;
}
function SLL(){
  this.head=null;
  this.addFront = function(val){
    var Node = new ListNode(val);
    currentNode = this.head;
    if (!currentNode){
      this.head = Node
      // console.log(Node)
      return Node;
    }
    while(currentNode.next){
      currentNode=currentNode.next;
    }
    currentNode.next=Node;
    var current = new ListNode(val);
  }
  //   return this.head;
  // }


// function ListNode(val){
//   this.val=value;
//   this.next=null;
// }
// function SLL(){
//   this.head=null;
  this.newList=function(val){
    if(!this.head)
    return False

    var current = this.head;

    var temp = SLL2.head
    while(SLL1.current.next){
      if (SLL1.current.next == null){
        temp2=SLL1.current.next
      }
      temp2.next=temp;
    }
    // newList=SLL1
  }
  return SLL1.head
}


var SLL1 = new SLL
var SLL2 = new SLL
SLL1.addFront(1)
SLL2.addFront(2)
console.log(SLL1.head)
