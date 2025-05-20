# Lesson 38 - for loop with  lists
# lesson 39 - High Score
# Use basic for loop, conditionals, etc to replicate the mas() function

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(max(student_scores))

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

print(high_score)

# Lesson 40 - for with range()
# Gauss challenge - sum all the numbers from 1 - 100

total = 0

for number in range(1, 101):
    total += number

print(total)
