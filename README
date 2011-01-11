pyhnn3 - Heterogeneous Neuronal Networks 3
==========================================

Dependencies
------------

 * MLPY (https://mlpy.fbk.eu/) >= 2.2.0
 * SciPy (http://www.scipy.org/) >= 0.7.2
 * NumPy >= 1.3.0

Data Set Header
-----------------

You have to add the following lines to the beginning of the data set file to 
can be used with pyhnn3.

 * Line 1: Type of problem, "cls" for classification problems, "rgs" for 
 regression problems.
 * Line 2: Number of attributes.
 * Line 3: Character for missing values.

To define the type of each attribute you have to put:

 * "int" for integer attributes.
 * "real" for real attributes.
 * "set" following of the possible values for nominal attributes.
 * "ord" following of the possible values for ordinal attributes with "<" order.
 * "bin" for binary attributes.
 * "class" for class attributes.

For classification problems, class attributes have to be coded as 0-1 sequences.

Example: 

Hepatitis data set:

cls
16
?
int
set 0 1
set 1 2 3 4
real
real
set 0 1
set 0 1 2
real
set 0 1
real
set 1 2 3
real
set 3 6 7
class
class
class

How to use
----------

$ python pyhnn3 -n {initial population} {dataset}

