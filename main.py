print("This program will print the highest score")

student_scores = input("Input a list of student\n").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#checking the highest score using for loop

highest_score = 0 
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"the highest score in the class is : {highest_score}")

