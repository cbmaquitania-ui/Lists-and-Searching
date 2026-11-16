scores = []
passed = 0

for i in range(5):
    p = int(input("Give me a score: "))
    scores.append(p)

for f in scores:
    if f >= 75:
        passed = passed + 1
        
print(passed, "of 5 passed")