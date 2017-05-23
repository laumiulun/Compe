""" Andy Lau, INL 2017 """

import os

Cur_dir=os.getcwd() # Find the current dir path
name='config.py'    # Name of configuration files


# Find all files that match the name of configuration files
i=0
j=0
y=[]
x=[]
for root, dirs, files in os.walk(Cur_dir, topdown=True):    # Find all files in the the dir
    for name in files:
        if name=='config.py':                               # Look for config.py in filename
            j=j+1
            y.append([])
            y[j-1]=root
            #print(os.path.join(root, name))                 # Output path that fit the conditions
            i=i+1
            x.append([])
            x[i-1]=(os.path.join(root, name))               # Join path to and assign to valuable x  

# Delete config.py from the end of each name
File_name=[i.split('/config.py',1)[0] for i in x] 

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

    Test='Test: '
    Ref='Ref: '
    # Join the file pathlength
    print(bcolors.RED+'Comparision Test '+bcolors.N+'*'*60)
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

    #Import Goldfile
    with open(Pathtogold) as f:
        out2=[]
        for line in f:
            line = line.split()
            if line:
                line=[str(i) for i in line]  # convert to str
                out2.append(line)

    # Cleanup each file   
    z=out[0]
    top=[i.split('|')[1] for i in z]
    
    # Delete the top row of each files
    del out[0]
    del out2[0]

    # Capture config value
    sys.path.append(Pathlength)
    import config
    Abs=float((config.Tolerance['Abs']))
    Rel=float((config.Tolerance['Rel']))


    # Manulipte Files input as script
    NumRows=(len(out))                      # Number of Rows
    NumColumns=(len(out[0]))                # Number of Columns

    x=[]                                    # Initalize the x matrix
    numerror=0;
    
    for j in range(len(out)):
        x.append([])                        # Grow the row of x matrix
        for i in range(len(out[0])):
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

# Run the program 
for i in range(len(File_name)):
    print(bcolors.BOLD+"\n"+"TEST:"+bcolors.N+bcolors.UNDERL+str(File_name2[i])+bcolors.N +"\n" )
        
    Comparision(File_name[i])    


print(bcolors.BOLD+"RESULT: " +bcolors.GREEN+"OK"+bcolors.N)
print(bcolors.BOLD+"NUMOFTESTS: "+str(len(y))+bcolors.N)


