# Compe #

### Overview ###

### Requirement ###
* Python 3.6.1 

### Getting Started ###
The program will actively look for file with the name “config.txt” which contain the relative and absolute tolerance set by user.  The same directory that contain the configuration files must also contain two data files, which must be named:

	“goldfile.txt”
	“test.txt”

### Using Compe ###
To run Compe, navigate to the directory where Compe is located and type:

    ./run_test


### Setup Compe ###
Set up config.txt

Create a txt file in the directory of your txt location, and follow the formate for the following:

```
Absolute_Tolerance: 1e-5”
Relative_Tolerance: 1e-5
Reference_Filepath: gold/rdg1d.output
Test_Filepath: rdg1d.output
```

Modlify values abd filepath to your configurations

Note: Make sure there is a space before each row
 
### Owner ###
* Owner: Miu Lun Lau
* Other community or team contact