def sed(pattern, replacement, file1, file2):
    fout = open(file2, "w+")
    with open(file1, 'r') as fin:
        for line in fin:
            fout.write(str(line).replace(pattern, replacement))
    fout.close()

sed("sipe", 'spencer', 'file1.txt', 'spencer.txt')