
test1 = float(input("Enter score for Test 1: "))
test2 = float(input("Enter score for Test 2: "))
test3 = float(input("Enter score for Test 3: "))
average_score = (test1 + test2 + test3) / 3

if average_score >= 90:
 grade = "A"
elif 80 <= average_score < 90:
 grade = "B"
elif 70 <= average_score < 80:
 grade = "C"
elif 60 <= average_score < 70:
 grade = "D"
else:
 grade = "F"

print("Average score: ", average_score)
print("Letter grade: ", grade)