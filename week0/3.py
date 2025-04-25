import numpy as np

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

average_scores_students = np.mean(scores, axis=1)
print("Average score for each student:", average_scores_students)

average_scores_subjects = np.mean(scores, axis=0)
print("Average score for each subject:", average_scores_subjects)

total_scores_students = np.sum(scores, axis=1)
highest_score_student = np.argmax(total_scores_students)
print(f"Student with the highest total score is student {highest_score_student}.")

scores[:, 2] += 5  # Adding 5 points to all elements in the third column
print("Updated scores with bonus points for third subject:")
print(scores)
