'''
#---------------------------------------------------
# MCNPtoolboxf - Code by L. Heffern & C. Hardgrove (c) June 18, 2018
# Function library
# Most Recent Update: Dec 12, 2023
# Currently cleaning up code, will continue to release throughout December 2023
# Next update anticipated: Dec 17, 2023
#---------------------------------------------------
'''
import numpy as np
import os
from operator import is_not
from functools import partial
import scipy.optimize as optimization
import collections
'''
#---------------------------------------------------
# DEFINE COMPOSITION DICTIONARY
#---------------------------------------------------
'''

def dictcompositionfile(filename): # Reads in a composition file
    file = open(filename, 'r')
    # Read and ignore header line
    MATERIALCARD = file.readline()
    OxygenLine = file.readline()
    Oline=(str.strip(OxygenLine,'m7').split('  ')) #calls the material you're changing m7
    LINES=[]
    allnames=[]
    MCNPcode=((str(filter(None,Oline)[0])))
    amount=((str(filter(None,Oline)[1])))
    comment=((str(filter(None,Oline)[2])))
    elementnames=str.strip((str.strip(comment)),'$')
    allnames.append(elementnames)
    elementweights = {elementnames:float(amount)}
    elementMCNPcode = {elementnames:MCNPcode}
    for line in file: # Loop over lines and extract variables of interest
        line = line.split(',')
        LINES.append(line)
    for i in range(0,len(LINES)-1):
        LIST=(str.strip(LINES[i][0])).split('  ')
        MCNPcode=(str(filter(None,LIST)[0]))
        amount=(str(filter(None,LIST)[1]))
        comment=(str(filter(None,LIST)[2]))
        elementnames=str.strip((str.strip(comment)),'$')
        allnames.append(elementnames)
        elementweights.update({elementnames:float(amount)})
        elementMCNPcode.update({elementnames:MCNPcode})
    return elementweights,elementMCNPcode,allnames, MATERIALCARD

def updateWTbasic(elementweights,value,elementname='H'):
    if elementname in elementweights:
        elementweights.update({elementname:float(value)})
        return elementweights
    else:
        return 'Error: Element not in base composition add to MCNPtoolbox.'

def dictcrosssectionfile(filename): # Reads in a composition file
    file = open(filename, 'r')
    # Read and ignore header line
    HEADER1 = file.readline()
    HEADER2 = file.readline()
    FirstLine = file.readline()
    FLine=(str.strip(FirstLine,'\n').split('\t')) #calls the material you're changing m7
    LINES=[]
    allnames=[]
    MCNPcode=((str(filter(None,FLine)[0])))
    isotope=((str(filter(None,FLine)[1])))
    isotopenames = str.strip((str.strip(isotope)), '$')
    abundance=((str(filter(None,FLine)[2])))
    Scat_xsect=((str(filter(None,FLine)[3])))
    Abs_xsect=((str(filter(None,FLine)[4])))
    molar_mass=((str(filter(None,FLine)[5])))
    allnames.append(isotopenames)
    abundances = {isotopenames:float(abundance)}
    elementMCNPcode = {isotopenames:MCNPcode}
    Scat_xsects = {isotopenames:float(Scat_xsect)}
    Abs_xsects = {isotopenames:float(Abs_xsect)}
    molar_masses = {isotopenames:float(molar_mass)}
    for line in file: # Loop over lines and extract variables of interest
        line = line.split(' ')
        LINES.append(line)
    for i in range(0,len(LINES)-1):
        LIST=(str.strip(LINES[i][0],'\n')).split('\t')
        MCNPcode=(str(filter(None,LIST)[0]))
        isotope=(str(filter(None,LIST)[1]))
        abundance=(str(filter(None,LIST)[2]))
        Scat_xsect = ((str(filter(None, LIST)[3])))
        Abs_xsect = ((str(filter(None, LIST)[4])))
        molar_mass = ((str(filter(None, LIST)[5])))
        isotopenames=str.strip((str.strip(isotope)),'$')
        allnames.append(isotopenames)
        abundances.update({isotopenames:float(abundance)})
        elementMCNPcode.update({isotopenames:MCNPcode})
        Scat_xsects.update({isotopenames:float(Scat_xsect)})
        Abs_xsects.update({isotopenames:float(Abs_xsect)})
        molar_masses.update({isotopenames:float(molar_mass)})
    return abundances,elementMCNPcode,Scat_xsects, Abs_xsects, molar_masses, allnames


'''
#---------------------------------------------------
# FOR CROSS-SECTIONS FILES
#---------------------------------------------------
'''

CrosssectionFile='Compositions/Crosssections.txt'

def readxsectfile(filename=CrosssectionFile):
    file = open(filename, 'r')
    nameline = file.readline()
    LINES = []
    for line in file:  # Loop over lines and extract variables of interest
        line = line.split('\t')
        LINES.append(line)
    MacroAbs={}
    MicroAbs = {}
    MacroScat={}
    MicroScat = {}
    for i in range(0, len(LINES)):
        LIST = LINES[i]
        Targetname = LIST[0]
        MacroAbs.update({Targetname:float(LIST[1])})
        MacroScat.update({Targetname:float(LIST[2])})
        MicroAbs.update({Targetname:float(LIST[3])})
        MicroScat.update({Targetname:float(str.strip(LIST[4],'\t'))})
    return MacroAbs,MacroScat,MicroAbs,MicroScat,Targetname
