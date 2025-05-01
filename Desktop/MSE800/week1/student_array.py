import numpy as np

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

print("Average score per student:", np.mean(scores, axis=1))

print("Average score per subject:", np.mean(scores, axis=0))

total_scores = np.sum(scores, axis=1)
print("Student with highest total score (row index):", np.argmax(total_scores))

scores[:, 2] += 5
print("Updated scores:\n", scores)
