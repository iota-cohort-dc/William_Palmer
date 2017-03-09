students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'},
]

def names(students):
    for value in students: # the word "value" is a variable. It is not a reserved word in Python
        print value['first_name'],value['last_name']

names(students)



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def bothPeople(users):

    for key, data in users.items():# the words "key" and "data" are variables. Not reserved words in Python
        count = 0
        print key
        for value in data:
            count +=1
            print count,'-',value['first_name'],value['last_name'],' - ',len(value['first_name'])+len(value['last_name'])

bothPeople(users)
