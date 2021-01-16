print("This program will print the highest score")

student_scores = input("Input a list of student").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


