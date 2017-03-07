import random
def scoreGrades():
    count =0
    grade=""
    while count < 10:
        random_num = random.random()
        str = random.randint(60,100)
        if str >= 60 and str < 70:
            grade = 'D'
            print 'Score: ', str, 'Your grade is ', grade
            count += 1
        elif str >=70 and str <80:
            grade = 'C'
            print 'Score: ', str, 'Your grade is ', grade
            count += 1
        elif str >=80 and str < 90:
            grade = 'B'
            print 'Score: ', str, 'Your grade is ', grade
            count += 1
        elif str >=90 and str <=100:
            grade = 'A'
            print 'Score: ', str, 'Your grade is ', grade
            count += 1

scoreGrades()
