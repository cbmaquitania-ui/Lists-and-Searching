def find(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
    
members = []
entry = input("Member (done to stop): ")

while entry != done:
    members.append(entry)
    
print(find(members, ))
    