import time

names = []
for x in range(1,6,1):
    names.append(str(x)+".txt")
#print(names)

for y in names:
    f = open(y,"w+")
    for line in range(6):
        f.write("This is sample line 1.\n")
        time.sleep(5)
    f.close()
