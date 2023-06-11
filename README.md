# Cosmic_Ray_Removal

A web app that provides an approachable method or removing cosmic rays from Raman spectra saved in CSV format.
This is an early version, I want to look into speeding it up.

The spectra need saving in a matrix where every row is a spectrum (no labels, spectral ranges, etc. in the same CSV)

How to use:
- Pull/download the file (dependencies: streamlit, pandas, and numpy)
- Run the program in python and navigate to page 1
- Select the CSV. file of Raman spectra you want cosmic rays removing from
- Wait... and save the csv file, then wait again... 
- The cosmic ray removed (crr) CSV should be in the same folder as Cosmic_Ray_Removed.py, called 'data_crr.csv'
