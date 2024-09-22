i = 1
while i in range(11):
    if i == 8: break
    print(i)
    i +=1 
    
word = "CIS103Lab3"
for i in range(len(word)):
    print(word[i] + " Index: " + str(i))
    
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()