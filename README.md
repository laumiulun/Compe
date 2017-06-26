# Compe #

### Overview ###

Compe is a python script specific developed to perform regression test by compare two test instances . These two instances will be tested against two tolerances values that are set by users and alerts user if any values exceed the tolerances. The program will actively look for configuration files to determine if any configuration files exist.

Compe is publically hosted on Github as a repository. To clone Compe, please visit [Compe Website](https://github.com/laumiulun/Compe)


### Requirement ###

Compe is developed using **Python 3.6.1**, please make sure the correct python version is used in-order for it to work properly. 

### Getting Started ###
The program will actively look for file with the name “config.txt” which contains the relative and absolute tolerance set by user.  The same directory that contain the configuration files must also contain two data files. 


### Using Compe ###
To run Compe, navigate to the directory where Compe is located and type:

    ./run_test

### Setup Compe ###
Set up config.txt

Create a txt file in the directory of your txt location, and follow the formate for the following:

```
Absolute_Tolerance: 1e-5   
Relative_Tolerance: 1e-5   
Reference_Filepath: gold/rdg1d.output
Test_Filepath: rdg1d.output
```

Modlify values abd filepath to your configurations

Note: 
* Make sure there is a space before each rows
* The reference/test Filepath are relative filepath from where config.txt is located
 

### For owner and developers ###
The logic process of Compe is as follows:
1. Located all subdirectory folders under Compe folder, and located if any configuration files exist 
2. Read configurations, references and test data inside the test folders
3. Compare the test data against the reference data according to tolerances set by configuration file
4. Output result in console and text document 
### Contact ###
* Developer: MIU LUN LAU


