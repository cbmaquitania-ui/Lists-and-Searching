scores = []

for i in range(5):
    p = int(input("Give me a score: "))
    scores.append(p)

highest = scores[0]

for f in scores:
    if f > highest:
        highest = f

print("Highest:", highest)