def search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return True
    return False
    
members = []
entry = input("Member (done to stop): ")

while entry != "done":
    members.append(entry)
    entry = input("Member (done to stop): ")
    
searched = 0
found = 0

name = input("Search (done to stop): ")

while name != "done":
    searched = searched + 1
    
    if search(members, name):
        print(" found")
        found = found + 1
        
    else:
        print(" not found")
        
    name = input("Search (done to stop): ")
    
print(found, "of", searched, "names found")