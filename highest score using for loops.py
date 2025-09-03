student_scores= (input("enter a list of students scores, sperated by a comma and a space"))
student_scores=(int(score)for score in student_scores)
highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f"the highest score is {highest_score}")
   