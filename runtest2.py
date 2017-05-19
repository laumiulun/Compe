""" Andy Lau, INL 2017 """

import os

Cur_dir=os.getcwd() # Find the current dir path
name='config.py'    # Name of configuration files


# Find all files that match the name of configuration files
i=0
x=[]
for root, dirs, files in os.walk(Cur_dir, topdown=True):    # Find all files in the the dir
    for name in files:
        if name=='config.py':                               # Look for config.py in filename
            print(os.path.join(root, name))                 # Output path that fit the conditions
            i=i+1
            x.append([])
            x[i-1]=(os.path.join(root, name))               # Join path to and assign to valuable x  

# Delete config.py from the end of each name
File_name=[i.split('/config.py',1)[0] for i in x] 


"""---------------------------------------------------------------------------------------------------------------------"""

# Importing Testing Comparision Program
def Comparision(Pathlength):
    import sys
    
    # Join the file pathlength
    print('Comparision Test','*'*60)
    Pathtotest=os.path.join(Pathlength,'test.txt')
    Pathtogold=os.path.join(Pathlength,'goldfile.txt')
    Pathtoout=os.path.join(Pathlength,'out.txt')
    
    #Import Testfile
    with open(Pathtotest) as f:
        out=[]
        for line in f:
            line = line.split()
            if line:
                line=[str(i) for i in line]  # convert to str
                out.append(line)

    #print('test.txt \n',out, '\n'*2)

    #Import Goldfile
    with open(Pathtogold) as f:
        out2=[]
        for line in f:
            line = line.split()
            if line:
                line=[str(i) for i in line]  # convert to str
                out2.append(line)

    #print('goldtest.txt \n',out2, '\n'*2)

    sys.path.append(Pathlength)
    import config
    Abs=float((config.Tolerance['Abs']))
    Rel=float((config.Tolerance['Rel']))


    # Manulipte Files input as script
    NumRows=(len(out))                      # Number of Rows
    NumColumns=(len(out[0]))                # Number of Columns

    x=[]                                    # Initalize the x matrix
    for j in range(len(out)):
        x.append([])                        # Grow the row of x matrix
        for i in range(len(out[0])):
            x[j].append(0)                  # Grow the column of x matrix
            x[j][i]=abs(float(out[j][i])-float(out2[j][i]))  #Find the tolerance value

    #print('X data \n')                      
    #print(x,'\n', 'Result','\n','-'*50)

    # Tolerance Comparision 
    for j in range(len(x)):
        for i in range(len(x[0])):
            if x[j][i]<Abs:
                continue
            else:
                print('Row:',j,'Columns:',i,',',x[j][i],'exceed Absolute Tolerance')  # Print it is greater than

            if x[j][i]<Rel:
                continue
            else:
                print('Row:',j,'Columns:',i,',',x[j][i],'exceed Relative Tolerance')
    print('\n', '-'*100)
    
    # Output files to a txt to the corrospondig dir.
    with open(Pathtoout, "w+") as f:
        f.write('Result:\n')
        for j in range(len(x)):
            for i in range(len(x[0])):
                if x[j][i]<Abs:
                    continue
                else:
                    L=('Row:',j,'Columns:',i,',',x[j][i],'exceed Absolute Tolerance')
                    f.write('\n')
                    f.write(str(L))
                    
                if x[j][i]<Rel:
                    continue
                else:
                    M=('Row:',j,'Columns:',i,',',x[j][i],'exceed Relative Tolerance')
                    f.write('\n')
                    f.write(str(M))
"""-------------------------------------------------------------------------------------------------------------"""

# Run the program 

for i in range(len(File_name)):
    print("\n",File_name[i], "\n")
    
    Comparision(File_name[i])    


