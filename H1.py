def find(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
    
members = []
entry = input("Member (done to stop): ")

while entry != "done":
    members.append(entry)
    entry = input("Member (done to stop): ")
    
name = input("Look for: ")
index = find(members, name)

if index == -1:
    print(name, "is not a member.")
    
else:
    print(name, "is member number", index + 1)