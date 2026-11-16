scores = []
total = 0

for i in range(5):
    p = int(input("Give me a score: "))
    scores.append(p)

for i in scores:
    total = total + i
    
print("Total:", total)
print("Average:", total / len(scores))