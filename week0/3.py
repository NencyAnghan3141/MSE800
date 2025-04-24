import numpy as np

# Given 2D array of scores (5 students, 3 subjects)
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# Task 1: Calculate and print the average score for each student (row-wise)
average_scores_students = np.mean(scores, axis=1)
print("Average score for each student:", average_scores_students)

# Task 2: Calculate and print the average score for each subject (column-wise)
average_scores_subjects = np.mean(scores, axis=0)
print("Average score for each subject:", average_scores_subjects)

# Task 3: Identify the student (row index) with the highest total score
total_scores_students = np.sum(scores, axis=1)
highest_score_student = np.argmax(total_scores_students)
print(f"Student with the highest total score is student {highest_score_student}.")

# Task 4: Add 5 bonus points to the third subject (index 2) for all students
scores[:, 2] += 5  # Adding 5 points to all elements in the third column
print("Updated scores with bonus points for third subject:")
print(scores)
