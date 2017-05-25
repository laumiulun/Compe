# Compe #

### Overview ###

* Python 3.6.1 

### Getting Started ###
The program will actively look for file with the name “config.py” which contain the relative and absolute tolerance set by user.  The same directory that contain the configuration files must also contain two data files, which must be named:

	“goldfile.txt”
	“test.txt”

The program will compare the two data sets and output locations of which it exceed the tolerances set up by “config.py”

### Using Compe ###
In order to use Compe, make sure your data sets are named goldfile.txt(Reference Data) and test.txt(Testing Data). Additionally, modlify the absolute and relative tolerence to yoyr desire by change the values in config.py 

To run Compe, navigate to the directory where Compe is located and type:

    ./run_test


### Set up Compe ###

* Set up config.txt
Create a txt file in the directory of your txt location, and follow the formate for the following:

   "Absolute_Tolerance: 1e-5
    Relative_Tolerance: 1e-5
    Reference_Filepath: gold/rdg1d.output
    Test_Filepath: rdg1d.output"

Modlify values abd filepath to your configurations

Note: Make sure there is a space before each row
 

### Owner ###

* Owner: Miu Lun Lau
* Other community or team contact