# SigmaNuPy
#-------------------------------------------------------------------------------------------------------------
Space Investigation Geoscience Mission Assessment of Nuclear instruments toolkit using Python
  ____  _                       _   _       ____
 / ___|(_) __ _ _ __ ___   __ _| \ | |_   _|  _ \ _   _
 \___ \| |/ _` | '_ ` _ \ / _` |  \| | | | | |_) | | | |
  ___) | | (_| | | | | | | (_| | |\  | |_| |  __/| |_| |
 |____/|_|\__, |_| |_| |_|\__,_|_| \_|\__,_|_|    \__, |
          |___/                                   |___/

                                            Beta Version 1.0
A Semi-Open-Source Python Toolkit for Planetary Nuclear Instrument Sensitivity Assessment using MCNP

#-------------------------------------------------------------------------------------------------------------
Created by:
Lena Heffern - Lheffern@asu.edu; Lena.Heffern@lasp.colorado.edu
Craig Hardgrove - chardgro@asu.edu
(c) June 18, 2018 - Dec 6, 2023
#-------------------------------------------------------------------------------------------------------------
Citations:
The GitHub repository of the Software: https://github.com/lheffern/SigmaNuPy
The AGU presentation related to the Software: 
Heffern, L. E, Hardgrove, C.J., & Landis, M.E., (2023, December 11-14). "SigmaNuPy: A Semi-Open-Source Python Toolkit 
for Planetary Nuclear Instrument Sensitivity Assessment Using MCNP," [Poster Presentation P11C-2743]. 2023 American 
Geophysical Union Conference, San Francisco, CA, United States. 
#-------------------------------------------------------------------------------------------------------------
PLEASE READ THE LICENSING INFORMATION BEFORE UTILIZING THIS SOFTWARE. BY USING THIS SOFTWARE YOU AGREE TO THE LICENSE.
#-------------------------------------------------------------------------------------------------------------
  ___ _   _ _____ ____   ___  ____  _   _  ____ _____ ___ ___  _   _ 
 |_ _| \ | |_   _|  _ \ / _ \|  _ \| | | |/ ___|_   _|_ _/ _ \| \ | |
  | ||  \| | | | | |_) | | | | | | | | | | |     | |  | | | | |  \| |
  | || |\  | | | |  _ <| |_| | |_| | |_| | |___  | |  | | |_| | |\  |
 |___|_| \_| |_| |_| \_\\___/|____/ \___/ \____| |_| |___\___/|_| \_|
                                                                     
#-------------------------------------------------------------------------------------------------------------
The interpretation of planetary nuclear data (acquired from orbit or the surface) requires knowledge that includes nuclear physics, engineering, and planetary geosciences. One barrier to mission planning using nuclear instrumentation comes from complexity of modeling codes and lack of publicly released tools to assist in modeling. The Space Investigation Geoscience Mission Assessment of Nuclear instruments toolkit using Python (SigmaNuPy) is a semi-open-source toolkit built in Python3.8+ and is designed to assist in the generation of model simulations (i.e., detectors, geometry, composition) and analyses of simulation outputs for use in planetary nuclear science instrument development and data analysis. The current status of SigmaNuPy is in Beta version, it is being developed for initial use with gamma-ray and neutron spectrometers (GRNS). We used the Monte Carlo N-Particle (MCNP6.1+) simulation code from Los Alamos National labs to create a set of basic planetary scenario files and GRNS instrument files that can be adjusted based on the user’s desired study. We consider our toolkit to be “semi-open-source” as the MCNP source code is controlled by the Radiation Safety Information Computational Center (RSICC) and requires approvals to obtain. We currently operate our code on the Arizona State University Agave Research Computing Cluster which has a designated and secure partition for running MCNP input files.
SigmaNuPy’s toolkit user input options include but are not limited to: 1) a suite of planetary compositions (e.g., materials including lunar, Mars, terrestrial, and etc. compositions); 2) ability to specify a range of elemental change within a material; 3) desired scenarios such as buried material; 4) desired source (e.g., passive GCR flux, active neutron generator, etc.); 5) orbital or landed scenarios; 6) and different levels of fidelity (e.g., level 0 particle tallys to a plane, level 1 particle tallys into instrument, etc.), with the current Beta version considered at level 1. Our Figure shows an example of a level 0 landed scenario.

The SigmaNuPy toolkit can be used for mission instrument planning and has the potential to assist in analysis of flight data. Here we present on the toolkit’s development and use in landed lunar mission planning and in ground-truth verification of active neutron measurements.

From: https://agu.confex.com/agu/fm23/meetingapp.cgi/Paper/1399696

#-------------------------------------------------------------------------------------------------------------
   ____ ___  _   _ _____ _____ _   _ _____ ____  
  / ___/ _ \| \ | |_   _| ____| \ | |_   _/ ___| 
 | |  | | | |  \| | | | |  _| |  \| | | | \___ \ 
 | |__| |_| | |\  | | | | |___| |\  | | |  ___) |
  \____\___/|_| \_| |_| |_____|_| \_| |_| |____/ 
                                                 
#-------------------------------------------------------------------------------------------------------------
==============================================================================================================
Filename                        Description                     Dependent Files/Folders/Libraries
==============================================================================================================
MCNPtoolbox.py                  The heart of the program        numpy, OS, scipy, functools, operator


==============================================================================================================
Generate.py                     Currently empty, TBR            MCNPtoolbox, numpy, OS, scipy, functools, operator

==============================================================================================================
GenerateMCNPElementGrid.py      Creates input grids of          MCNPtoolbox, numpy, OS, time
                                MCNP files, along with
                                copy/paste .txt files for
                                easy use with SLURM-based
                                computing clusters; this
                                code can either generate
                                grid files for use with
                                GenerateDetectorFile or
                                it can just make first
                                principles surface tally
                                grid files (see Intro
                                Document)
==============================================================================================================
GenerateDetectorFile.py         Creates detector grid          MCNPtoolbox, numpy, OS, time
                                MCNP input files to do
                                sensitivity analyses for
                                gamma-rays (see Intro
                                Document)
==============================================================================================================
MCNPtoCSV_gammas.py             Converts MCNP output to       extra_MCNPfunctions, os, time
                                a more readable file
==============================================================================================================
MCNPtoCSV_neutrons.py           TBR                           extra_MCNPfunctions, os, time, umpy, matplotlib
==============================================================================================================
MiscPrograms folder             TBR
==============================================================================================================
BaseMx folder                   MCNP base files; these should be raw MCNP.mx files that can be used as inputs
                                into the GenerateMCNPElementGrid file; active files are labeled, if not labeled
                                as active assume it is a passive file, but check the MCNP cards - it is active
                                if there is an obvious Time Card! SPECIFIC FORMAT IN USE PLEASE FOLLOW IT!
==============================================================================================================
DetectorFiles folder            Files here are literally detector in an empty vacuum bubble; you should be 
                                using these files as an input into the GenerateDetectorFile program; the 
                                DetectorFile.mx file gets the output from the GenerateMCNPElementGrid 
                                basefile_composition.outputo file shoved into it; the output from the 
                                basefile_composition.outputo is the gamma-ray leakage from the planetary 
                                surface at whatever height you specify the tally height (TBR feature); this 
                                tally leakage is then projected as a disk source onto the detector you choose; 
                                the resulting output is the gamma-ray pulse-height spectrum of the detector; 
                                TBR on adding. SPECIFIC FORMAT IN USE PLEASE FOLLOW IT!
==============================================================================================================
Compositions folder             Pretty self-explanatory, but these have a VERY SPECIFIC FORMAT PLEASE USE IT
                                IF YOU INTEND TO MAKE YOUR OWN COMPOSITIONS!!!
==============================================================================================================
Examples folder                 Old examples.
==============================================================================================================
Sources folder                  Different GCR and PNG sources that can be put into the BaseMX.mx files.
==============================================================================================================

This space intentionally left blank.



==============================================================================================================

#-------------------------------------------------------------------------------------------------------------
  _____ _   _ _____ _   _ ____  _____   _____ ____  ____     _______ ____  ____
 |  ___| | | |_   _| | | |  _ \| ____| |_   _| __ )|  _ \   / |_   _| __ )|  _ \ ___
 | |_  | | | | | | | | | | |_) |  _|     | | |  _ \| |_) | / /  | | |  _ \| | | / __|
 |  _| | |_| | | | | |_| |  _ <| |___    | | | |_) |  _ < / /   | | | |_) | |_| \__ \
 |_|    \___/  |_|  \___/|_| \_|_____|   |_| |____/|_| \_/_/    |_| |____/|____/|___/

#-------------------------------------------------------------------------------------------------------------
1. Organize and combine function libraries to be more consistent
2. Clean up plotting program (in dev)
3. Clean up CSV converter files (in dev)
4. Clean up depth/layering generator program (in dev)
5. Add new detector types (CsI, HPGe, CLLBC, BGO, etc.)
6. Add new user input capabilities for detector size and selection
7. Figure out Java applet to combine literally everything together
8. Add in new BaseMx.mx files that include higher fidelity levels, e.g., Rovers, S/C, and Orbital options

#-------------------------------------------------------------------------------------------------------------
  ____  _____ _____ _____ ____  _____ _   _  ____ _____ ____
 |  _ \| ____|  ___| ____|  _ \| ____| \ | |/ ___| ____/ ___|
 | |_) |  _| | |_  |  _| | |_) |  _| |  \| | |   |  _| \___ \
 |  _ <| |___|  _| | |___|  _ <| |___| |\  | |___| |___ ___) |
 |_| \_|_____|_|   |_____|_| \_|_____|_| \_|\____|_____|____/

#-------------------------------------------------------------------------------------------------------------
Publications that have used this Code:

[1] L.E. Heffern. "Strange New Worlds: Development of Active Nuclear Technologies and Techniques for Planetary
Science Applications" Arizona State University ProQuest Dissertations Publishing,  2022. 29255531.
https://keep.lib.asu.edu/items/171826
https://keep.lib.asu.edu/_flysystem/fedora/c7/Heffern_asu_0010E_22076.pdf

[2] L.E. Heffern, C.J. Hardgrove, A. Parsons, et al., "Active neutron interrogation experiments and simulation
verification using the SIngle-scintillator Neutron and Gamma-Ray spectrometer (SINGR) for geosciences,"Nuclear 
Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated 
Equipment, Volume 1020, 2021, 165883, ISSN 0168-9002, https://doi.org/10.1016/j.nima.2021.165883.
https://www.sciencedirect.com/science/article/pii/S0168900221008664


Materials used in this library:

[1] Prettyman, T. H., Hagerty, J. J., Elphic, R. C., Feldman, W. C., Lawrence, D. J., McKinney, G. W., and 
Vaniman, D. T. (2006), Elemental composition of the lunar surface: Analysis of gamma ray spectroscopy data 
from Lunar Prospector, J. Geophys. Res., 111, E12007, doi:10.1029/2005JE002656.

[2] Nowicki, S. F., Evans, L. G., Starr, R. D., Schweitzer, J. S., Karunatillake, S., McClanahan, T. P., 
Moersch, J. E., Parsons, A. M., and Tate, C. G. (2017), Modeled Martian subsurface elemental composition 
measurements with the Probing In situ with Neutron and Gamma ray instrument, Earth and Space Science, 4, 
76–90, doi:10.1002/2016EA000162.

[3] Personal communication with S. Czarnecki 2018

[4] Kevin W. Lewis et al. ,A surface gravity traverse on Mars indicates low bedrock density at Gale crater.
Science363,535-537(2019).DOI:10.1126/science.aat0738

[5] Lawrence, D. J., Feldman, W. C., Elphic, R. C., Hagerty, J. J., Maurice, S., McKinney, G. W., and 
Prettyman, T. H. (2006), Improved modeling of Lunar Prospector neutron spectrometer data: Implications 
for hydrogen deposits at the lunar poles, J. Geophys. Res., 111, E08001, doi:10.1029/2005JE002637.

[6] Morgan L. Cable, Sarah M. Hörst, Robert Hodyss, Patricia M. Beauchamp, Mark A. Smith, and Peter A. 
Willis (2012), Titan Tholins: Simulating Titan Organic Chemistry in the Cassini-Huygens Era, Chemical 
Reviews 112 (3), 1882-1909. DOI: 10.1021/cr200221x

[7] Asteroid materials, personal communication with AstroForge 2022.

[8] Meteorite compositions based on averaging of compositional information from MetBase, 
https://www.metbase.org/sites/Metbase_GUI_new/


MCNP Code & Information:

[1] D. B. Pelowitz (Ed.) (2005), MCNPX User's Manual Version 2.5.0, Los Alamos Natl. Lab. Doc. 
LA-CP-05–0369, Los Alamos Natl. Lab., Los Alamos, N. M.

[2] Personal communication Christopher Tate, Oak Ridge National Laboratory

[3] Personal communication Richard Starr, Catholic Univerisities of America

[4] Personal communication Tom Prettyman, Planetary Science Institute

[5] Personal communication Ann Parsons, NASA Goddard

#-------------------------------------------------------------------------------------------------------------

 ______                 
 \  ___)                
  \ \     _  __  ______ 
   > >   | |/ / (  __  )
  / /__  | / /   | || | 
 /_____) |__/    |_||_| 
                        
                        
