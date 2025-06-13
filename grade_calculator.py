# Calculate average and letter grade

scores = list(map(float, input("Enter marks (space-separated): ").split()))
average = sum(scores) / len(scores)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
