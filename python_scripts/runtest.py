""" Andy Lau, INL 2017 """

import os
import sys
import subprocess
import csv

Cur_dir=os.getcwd() # Find the current dir path

# Find all files that match the name of configuration files
i=0
j=0
y=[]
x=[]
for root, dirs, files in os.walk(Cur_dir, topdown=True):    # Find all files in the the dir
    for name in files:
        if name=='config.txt':                               # Look for config.py in filename
            j=j+1
            y.append([])
            y[j-1]=root
            #print(os.path.join(root, name))                 # Output path that fit the conditions
            i=i+1
            x.append([])
            x[i-1]=(os.path.join(root, name))               # Join path to and assign to valuable x  

# Delete config.py from the end of each name
File_name=[i.split('/config.txt',1)[0] for i in x] 

File_name2=[y.split(str(Cur_dir))[1] for y in File_name]


"""---------------------------------------------------------------------------------------------------------------------"""
# Class of colors
class bcolors:
    N='\033[0m'             #Normal
    BOLD = '\033[1m'        #Bold
    UNDERL = '\033[4m'      #Underline
    RED = '\033[91m'        #RED
    GREEN = '\033[42m'      #GREEN
    

# Importing Testing Comparision Program
def Comparision(Pathlength):
    import sys
    
    ## Import config.txt
    Pathtoconfig=os.path.join(Pathlength,'config.txt')

    with open(Pathtoconfig) as f:
        out3=[]
        for line in f:
            line = line.split()
            if line:
                line=[str(i) for i in line]  # convert to str
                out3.append(line)
    configD=[]
    for i in range(len(out3)):
        configD.append([])
        configD[i]=out3[i][1]

    Abs=float(configD[0])
    Rel=float(configD[1])
    GOLD=configD[2]
    TEST=configD[3]


    Test='Test: '
    Ref='Ref: '
    # Join the file pathlength
    print(bcolors.RED+'Comparision Test '+bcolors.N+'*'*60)
    Pathtotest=os.path.join(Pathlength,TEST)
    Pathtogold=os.path.join(Pathlength,GOLD)
    Pathtoout=os.path.join(Pathlength,'out.txt')

    #Import Testfile
    with open(Pathtotest) as csvfile:
        out=[]
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row:
                row=[str(i) for i in row]
                out.append(row)

    #Import Goldfile
    with open(Pathtogold) as csvfile:
        out2=[]
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row:
                row=[str(i) for i in row]
                out2.append(row)


    # Cleanup each file   
    top=out[0]
    
    
    # Delete the top row of each files
    del out[0]
    del out2[0]

    # Manulipte Files input as script
    NumRows=(len(out))                      # Number of Rows
    NumColumns=(len(out[0])-1)                # Number of Columns

    x=[]                                    # Initalize the x matrix
    numerror=0;
    
    for j in range(NumRows):
        x.append([])                        # Grow the row of x matrix
        for i in range(NumColumns):
            x[j].append(0)                  # Grow the column of x matrix
            x[j][i]=abs(float(out[j][i])-float(out2[j][i]))  #Find the tolerance value

    # Tolerance Comparision 
    for j in range(len(x)):
        for i in range(len(x[0])):
            if x[j][i]<Abs:                 # Compare to Absolute Tolerance
                continue
            else:
                print((bcolors.BOLD+'Row:')+ bcolors.N+str(j)+ bcolors.BOLD + ' Columns:',
                      bcolors.N + str(top[i])+bcolors.BOLD+' , Test: '+ bcolors.N+str(out2[j][i])+' , '+
                      bcolors.BOLD+str(Ref)+bcolors.N+str(out[j][i])+' , '+
                      bcolors.RED+str(x[j][i])+
                      bcolors.N+' exceed Absolute Tolerance')  # Print it
                numerror=numerror+1;
                
            if x[j][i]<Rel:                 # Compare to Relative Tolerance
                continue
            else:
                 print((bcolors.BOLD+'Row:')+ bcolors.N+str(j)+ bcolors.BOLD + ' Columns:',
                      bcolors.N + str(top[i])+bcolors.BOLD+' , Test: '+ bcolors.N+str(out2[j][i])+' , '+
                      bcolors.BOLD+Ref +bcolors.N+str(out[j][i])+' , '+
                      bcolors.RED+str(x[j][i])+
                      bcolors.N+' exceed Relative Tolerance')  # Print it

    # IF encounter no error, Output "OK"
    if numerror==0:
        print(bcolors.GREEN+" OK "+ bcolors.N)
        print('_'*75)
    else:
        print('_'*75)
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
s_name=[]
# Run the program
for i in range(len(File_name)):
    s_name.append([])
    s_name[i]=("cd;cd "+File_name[i]+";~/rdgflo1d/singlephase/src/rdg1d")
    
    output=subprocess.call(s_name[i],shell=True)

subprocess.call("clear",shell=True)

for i in range(len(File_name)):
    print(bcolors.BOLD+"\n"+"TEST:"+bcolors.N+bcolors.UNDERL+str(File_name2[i])+bcolors.N +"\n" )
    
    Comparision(File_name[i])    
    

print(bcolors.BOLD+"RESULT: " +bcolors.GREEN+"OK"+bcolors.N)
print(bcolors.BOLD+"NUMOFTESTS: "+str(len(y))+bcolors.N)



