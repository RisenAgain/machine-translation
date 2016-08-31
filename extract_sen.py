# separate sentence from file

#file where alignment is present
directory = "hi-en.A3.final"
# for hindi
f1 = open("hindisent.txt", 'w')

# for english
# f1 = open("eng.txt", 'w')
with open(directory, 'r') as flp:
    data = flp.read()

i = 1
while True:
    lines = data.splitlines()[i]
    print lines
    i += 3
    print i
# write hindi sentences in the file 
    f1.write(lines)
    f1.write("\n")

flp.close()
f1.close()
