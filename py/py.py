f=open("data.txt","r")
linum=0
for line in f:
    if "python" in line.lower():
        print("present")
        print(linum)
    linum+=1
