with open("rdg1d.output") as f:
        out=[]
        for line in f:
            line = line.split()
            if line:
                line=[str(i) for i in line]  # convert to str
                out.append(line)


z=out[0]

del out[0]
print(out)
