def count(items, target):
    count = 0
    for i in range(len(items)):
        if items[i] == target:
            count = count + 1
    return count
    
vote = []
entry = input("Vote (done to stop): ")

while entry != "done":
    vote.append(entry)
    entry = input("Vote (done to stop): ")
    
name = input("Candidate: ")
index = count(vote, name)

print(name, "got", index, "vote(s)")