def calculate(weights, max_scores, scores):
    total = 0
    if not weights:
        weights100 = 100 / len(scores)
        weights = [weights100] * len(scores)
    for i in range(len(scores)):
        ratio = scores[i] / max_scores[i]
        weights_part = ratio * weights[i]
        total += weights_part
    return round(total, 2)
weights = list(map(int, input("weights: ").split()))
max_scores = list(map(int, input("max_scores: ").split()))
scores = list(map(int, input("scores: ").split()))
final_scores = calculate(weights, max_scores, scores)
print(f"Final weighted score is {final_scores}")
