# -*- coding: utf-8 -*-  
from math import exp
from multiprocessing import Process
import os

'''def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
from multiprocessing import Pool, cpu_count
pool = Pool(processes=cpu_count())
'''
#import plotly.plotly as py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.stats
from scipy.stats import norm
import warnings
import matplotlib
warnings.filterwarnings('ignore')
import random, math
from matplotlib import cm
colvar_name='COLVARN_atoms'
colvar_file='{}'.format(colvar_name)
cs_file_name='{}'.format('cs-cs-100.dat')
chem_shifts_lab={'cb':3, 'ha':0, 'cb':4, 'co':5, 'hn':1, 'nh':2}
def empty_arrays(length):
    '''takes a number and makes number by number array
    Var:length:length of the array that needs to be generated
    Return: an empty nxn array'''
    index=0
    empty_NxN_array=[]#array that is 'length' long
    for i in range(length):
        empty_NxN_array.append([])
    return empty_NxN_array
def numbers(filename):
    '''takes the output file of the colvar file and prints the data points in an array
    filename:name of the COLVAR file
    returns an array of data points read from the output file'''
    f=open(filename, 'r')
    lines=f.readlines()                       #lines in the file
    lines=lines[1:]                           #gets rid of the first two lines from an array lines
    names_of_variables=lines[0].strip()       #reads the following line that has the names of the variables and gets rid of the newline syntax
    variables=names_of_variables.split()      #creates an array of variable names
    word_count=len(variables)                 #keeps the total number of variables
    number_array=empty_arrays(word_count)     #empty array that has number of variables long square array
    for i in lines:
        clean_line=i.strip()                  #cleans the lines
        array_of_words=clean_line.split()     #separates the string in the line whenever there is space
        index=0                               #index of numbers will be stored
        for i in array_of_words:        
            number_array[index].append(float(i))
            index=index+1
    return number_array[1:]

#an array will hold the data from the output of the COLVAR file

noe_results=numbers(colvar_file)         #output of the COLVAR file are actually stored here.

power=1/6.0#power
conversion_factor=10**(-3)
def variables(filename):
    '''takes in a file and returns an array of variable names from the first line of the output COLVAR_File'''
    f=open(filename, 'r')
    lines=f.readlines()                      #contains all the lines from the file
    line0=lines[0]                           #reads the first line and saves it
    line0_strip=line0.strip()                #gets rid of the newline comment
    line0_split=line0_strip.split()          #splits the line into strings whenever there is a space
    return line0_split[3:]                   #gets rid of the first 3 variables

def noe_f(results):
    '''Computes the noe by taking the array of noe and print the average noe and distance restraints
    Return: NOE intensity and NOE distance'''
    noe=0
    for n in results:
        noe+=n
    noe1=noe/len(results)
    return noe1,noe1**(-power)
def chemical_shifts(cs_file, shift_type):
    '''takes a file with chemical shifts, and the type of chemical shifts and returns the corresponding chemical shifts for the backbone 
    parameters: 
        cs_file-string that has chemical shifts filename
        shift_type-string that has chemical shift type e.g 'HA', 'CA', 'C', 'CB', 'N', 'H'
    returns:
        chem_shifts: array that has the chemical shifts
    '''
    cs_type=chem_shifts_lab[shift_type]
    f=open(cs_file, 'r')
    lines=f.readlines()
    chem_shifts=[]
    for data in lines:
        stripped_data=data.strip()#strips the newline symbol
        splitted_data=stripped_data.split()
        splitted_data=splitted_data[3:]

        index=cs_type*4
        chem_shifts.append(splitted_data[index])
    return chem_shifts
shiftss=chemical_shifts(cs_file_name, 'nh')
last_atom=len(shiftss)-1
shiftss[0]=105
shiftss[last_atom]=135
len(shiftss)
for i in range(len(shiftss)):
    shiftss[i]=float(shiftss[i])
def total_atom(variables_list):
    '''takes an array of variable names and counts the total number of atoms interacting to make noes
    args: variables_list-an array of variable names for interacting atoms
    returns an array that has all the interacting atoms labeled 
    '''
    total_number_atoms=0                   #total number of atoms interacting
    atom_labels=[]#array that keeps labels of atoms
    for i in range(len(variables_list)):   #index for the variables argument
        word=variables_list[i]                              #reads each label in the list
        atom1_2=word.split('_',2)                             #splits the labels whenever there is an underscore
        atom1_2=atom1_2[1:]                                    #removes the first part of the splitted word which supposed to be comb
        k=i+1                                                #keeps track of the index of next thing in the loop
        next_word=variables_list[k]        #reads the next word in the list
        atom1_2_next=next_word.split('_',2)#splits the labels whenever there is an underscore
        atom1_2_next=atom1_2_next[1:]      #removes the first part of the splitted word which supposed to be comb
        atom_identity=[] #an array that will keep track of atoms to be added
        atom_identity.append(int(atom1_2[1]))#the string that old atom number will be converted to a string
        atom_identity.append(shiftss[k])         #  the index that keeps track of the for loop will also be added as an actual atom number later
        atom_labels.append(atom_identity)  #both the old atom value and the new atom value will be added to the array that keeps track of labels
        if (atom1_2[0]!=atom1_2_next[0]):#check the atom values whether the next atom and previous atom are the same
            total_number_atoms=i           #updates the total number of atoms even when the consecutive atoms differ
            last_atom=[int(atom1_2[0])]    #if the if statement is true it will add the first pivot atom itself around which the all the other atoms were labeled 
            last_atom.append(shiftss[0])            #keep track of the atoms in the list
            atom_labels.append(last_atom)  #first atom and its new index are added
            break
    return atom_labels                     #returns the old and new label of all atoms involved
old_variables=variables(colvar_file)  #variables are retrieved from the file
def converted_variables(filename):
    '''takes in a file and returns an array of variable names from the first line of the output COLVAR_File'''
    f=open(filename, 'r')
    lines=f.readlines()                    #contains all the lines from the file
    line0=lines[0]                         #reads the first line and saves it
    line0_strip=line0.strip()              #gets rid of the newline comment
    length_line=len(line0_strip)/2
    line0_split=line0_strip.split()        #splits the line into strings whenever there is a space
    line0_split=line0_split[3:]
    chem_shifts_var=[]
    total_atoms=total_atom(old_variables)
    number_atoms=len(total_atoms)
    for atoms  in total_atom(old_variables):
        for i in range(len(line0_split)):
    
           
            if (('_{}'.format(atoms[0]) in line0_split[i])):
                if (atoms[0]<10):
                    break
                else:
                    old_atom='_{}'.format(atoms[0])
                    new_atom='_{}'.format(atoms[1])
                    word=line0_split[i]
                    line0_split[i]=word.replace(old_atom, new_atom)          
    for i in range(number_atoms):
        word=line0_split[i]
        line0_split[i]=word.replace('_{}_'.format(total_atoms[number_atoms-1][0]), '_{}_'.format(total_atoms[number_atoms-1][1]))
    print line0_split[0]
    return line0_split        
new_variables=converted_variables(colvar_file)
variable_averagenoe=[]                     #empty array that contains the atoms that will have strong intensities and show intensities and restraints
for  i in range(len(noe_results)):
    if (i==0):
        next
    else:
        variable_noe=[]                           #an array which will save a string of atoms interacting and the corresponding value of average NOE intensity and distance
        noe, dist=noe_f(noe_results[i])           #computes an noe and distance restraint from an array of noe measurements.
        variable_noe.append(new_variables[i])     #adds the corresponding new labels for the interacting atoms
        variable_noe.append(noe)                  #append the noe
        variable_noe.append(dist)                 #append the distance
        variable_averagenoe.append(variable_noe)  # for a given array of results noe_results[i] the corresponding atoms, noe intensity and noe distance will be saved

small_dist_atoms_1=[]#1st atoms of NOESY 
small_dist_atoms_2=[]#2nd atoms of NOESY
intensities=[]#intensities
def atoms_distances(array_of_comb_numb):
    #takes an array of interacting atoms, intensity, and distance as an array element and outputs intensities and interacting atoms that have a big enough intensity
    #array_of_comb_numb: nx3 array, 1st colomn is the interacting atoms (comb_1_2), 2nd column is noe intensity, and 3rd column is 
    #return:  three arrays will be returned that have the first atom, second atom and the corresponding NOE intensit
    for i in range(len(array_of_comb_numb)):
        if (array_of_comb_numb[i][2]>1):   # only atoms that are closer than 5.5 Angstroms will be considered
            next
        else:
        
            comb_word=array_of_comb_numb[i][0]  #saves the first element of the given array, which is a string that tells about info about interacting atoms 
            atoms=comb_word.split("_", 2)       #cuts the string wherever there is an underscore
            atoms=atoms[1:] #removes the string part of the label
            atom1=float(atoms[0])                 #reads and makes the first atom into an integer type
            atom2=float(atoms[1])                 #reads and makes the second atom into an integer type
            small_dist_atoms_1.append(atom1)    #puts different combinations of atoms
            small_dist_atoms_1.append(atom1)
            small_dist_atoms_2.append(atom2)
            small_dist_atoms_2.append(atom1)
            intensities.append(array_of_comb_numb[i][1]*conversion_factor)
            intensities.append(array_of_comb_numb[i][1]*conversion_factor)
            small_dist_atoms_1.append(atom2)
            small_dist_atoms_1.append(atom2)
            small_dist_atoms_2.append(atom1)
            small_dist_atoms_2.append(atom2)
            intensities.append(array_of_comb_numb[i][1]*conversion_factor)
            intensities.append(array_of_comb_numb[i][1]*conversion_factor)
    return small_dist_atoms_1, small_dist_atoms_2, intensities 
x_H,y_H, intense=atoms_distances(variable_averagenoe) #x atom, y atom, and corresponding interaction
XX_means=np.array(x_H)                                #atoms on x_axis
YY_means=np.array(y_H)                                #atoms on y_axis
intens=np.array(intense)                              #noe intensity
x_atoms=np.array(shiftss)                             #shift of atoms on x_axis
X_points=np.arange(min(shiftss),max(shiftss),1)       #gridpoints for axis
N_atoms=len(X_points)
sigma=0.0001
def gaus(x, y, intensity):
    ''' a function that takes in 3 arrays of atoms on x axis and atoms on y axis and the NOE intensity between corresponding atoms and returns a 2D array of gaussian corresponding to each point on the grid

    Arguments:

       x - an array of atom indeces that will be in x-axis of 2D NOESY spectrum
       y - an array of atom indeces that will be in y-axis of 2D NOESY spectrum
       intensity- an array of intensity for corresponding atom indeces
    Returns:
    
       ZZZ-2D array that should have the gaussian for each interacting pair of atoms
       
    '''
    ZZZ=np.zeros((len(X_points),len(X_points)))#N_atoms,N_atoms))                 #initialize 2d grid to zeros
    for i in range(len(X_points)):                  #iterates through X atoms
        for k in range(len(X_points)):              #iterates through Y atoms
            for l in range(len(x)):                 #iterates though all neighbors that have to add to the guassian with their respective intensities  
                ZZZ[i][k]+=intensity[l]*math.exp(-((x[i]-x[l])**2+(y[k]-y[l])**2)/(2*sigma**2))
    return ZZZ

ZZ=gaus(XX_means, YY_means, intense)                  #adds gaussian to two interacting atoms with high NOE intensity
ZZ=np.array(ZZ)                                       #converts to np array
fig, ax = plt.subplots()                              #start plotting
sc=ax.scatter(x_H, y_H,ZZ)# intense)                      #scatter plot of NOESY spectrum
ax.grid()
plt.xlabel('chemical shifts')
plt.ylabel('chemical shifts')
plt.title(r'Scaller plot of 2D NOESY Spectroscopy of N atoms')
plt.savefig('final_project_gaussian.png'.format(colvar_name)) 
fig1, ax1 = plt.subplots()                            #start plotting
sc=ax1.scatter(x_H, y_H,intense)                      #scatter plot of NOESY spectrum
ax1.grid()
plt.xlabel('chemical shifts')
plt.ylabel('chemical shifts')
plt.title(r'Gausian 2D NOESY Spectroscopy of N atoms')
plt.savefig('final_project_scatter_plot.png'.format(colvar_name)) 
plt.show()

plt.show()


