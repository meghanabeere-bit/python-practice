import fileinput

with fileinput.input(files=('sample.txt','no.txt'))as f:
    for line in f:
        print(line, end='')
