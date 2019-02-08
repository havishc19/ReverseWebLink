


f1 = open("output_webLink.tsv")
f2 = open("output_edgeFile.tsv", "w")
f2.write("Source\tTarget\n")
lines = f1.readlines()
for line in lines:
    temp = line.split("\t")
    source = temp[0]
    targets = temp[1][1:-2].split(";")
    print(targets)
    for target in targets:
        f2.write(source + "\t" + target + "\n")

