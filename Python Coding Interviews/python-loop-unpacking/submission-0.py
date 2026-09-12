from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest = 0
    high_score_student = ""
    for name, score in scores:
        if score > highest:
            high_score_student = name
            highest = score
    return high_score_student



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
