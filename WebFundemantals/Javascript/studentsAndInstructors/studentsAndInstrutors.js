var Students = [
  {first_name: 'Michael', last_name: 'Jordan'},
  {first_name: 'John', last_name: 'Rosales'},
  {first_name: 'Mark', last_name: 'Guillen'},
  {first_name: 'KB', last_name: 'Tonel'},
]

function studentNames(Students){
  for (var i=0; i < Students.length; i++){
    console.log(Students[i].first_name + " " +Students[i].last_name);
  }
}
studentNames(Students);
