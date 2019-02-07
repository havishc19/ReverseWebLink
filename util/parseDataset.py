import sys
import random
iter = 0
file2 = open("graph.tsv","w")
batchWrite = []
with open("soc-LiveJournal1.txt") as file:
    for line in file:
        temp = line[:-2] + "\t" + str(random.randint(1,101)) + "\n"
        batchWrite.append(temp)
        iter += 1
        if(iter % 1000000 == 0):
            print(iter)
            file2.writelines(batchWrite)
            batchWrite = []

    # print(iter)


