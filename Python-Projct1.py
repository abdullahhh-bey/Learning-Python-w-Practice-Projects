firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
Id = int(input("Enter your Student Id: "))
math_score = float(input("Enter your Maths score: "))
english_score = float(input("Enter your English score: "))
science_score = float(input("Enter your Science score: "))
hasScholarship = bool(input("Are you on scholarship? ( If yes -> True & If no -> False)"))

student_info = {
    "firstName" : firstName,
    "lastName" : lastName,
    "Id" : Id,
    "Mathematics Score": math_score,
    "English Score" : english_score,
    "Science Score" : science_score,
    "HasScholarship" : hasScholarship
}

totalScore = math_score + english_score + science_score
average = (totalScore/3)

grade = ""

if average >= 90 and average <= 100:
    grade = "A"
    
if average >= 80 and average < 90:
    grade = "B"
    
if average >= 70 and average < 80:
    grade = "C"

if average >= 60 and average < 70:
    grade = "D"

if average >= 50 and average < 60:
    grade = "E"
    
if average < 50:
    grade = "F"

print(f"Total Score : {totalScore}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
