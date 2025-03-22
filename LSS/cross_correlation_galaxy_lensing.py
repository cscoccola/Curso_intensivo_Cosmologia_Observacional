#Exercise: Cross-Correlation Between Galaxy Surveys and CMB Lensing Maps

#Objective
#Analyze the correlation between the distribution of galaxies in a survey and the CMB lensing convergence map, which traces the large-scale matter distribution.



# Data Requirements
# Galaxy Survey Data

# Data Source: SDSS DR12 (Sloan Digital Sky Survey, Data Release 12).
# Dataset: The BOSS (Baryon Oscillation Spectroscopic Survey) galaxy catalog.
# Access:
# Visit the SDSS DR12 Science Archive Server.
# Download the BOSS LSS catalogs from here.
# Use the "randoms" and "galaxy" files to construct density fields.
# CMB Lensing Map

# Data Source: Planck Collaboration.
# Dataset: CMB lensing convergence map (Planck 2018).
# Access:
# Visit the Planck Legacy Archive.
# Navigate to "CMB lensing products" under "Planck 2018 results."


# Steps to Follow
# 1. Prepare the Galaxy Data

# Load the galaxy catalog from SDSS.
# Apply cuts for redshift (e.g.,  0.1 < 𝑧 < 0.6 0.1<z<0.6) to ensure overlap with the CMB lensing map's sensitivity.
# Bin the galaxies into a Healpix map using the Python package healpy.


import healpy as hp
import numpy as np
from astropy.io import fits

# Example: Load galaxy RA/Dec and create a Healpix map
galaxy_data = fits.open('galaxy_catalog.fits')[1].data
nside = 512  # Healpix resolution
pixels = hp.ang2pix(nside, galaxy_data['RA'], galaxy_data['DEC'], lonlat=True)
galaxy_map = np.zeros(hp.nside2npix(nside))
for pix in pixels:
    galaxy_map[pix] += 1



# 2. Prepare the CMB Lensing Data

# Load the Planck lensing map (in Healpix format).
# Smooth or rebin the map to match the resolution of the galaxy map.


# Load Planck lensing map
lensing_map = hp.read_map('COM_Lensing_Convergence_2048_R3.00.fits')
lensing_map = hp.ud_grade(lensing_map, nside_out=512)  # Match resolution




#3. Compute the Cross-Power Spectrum

#Use healpy to compute the angular cross-power spectrum  C_\ell  between the two maps.


cl_cross = hp.anafast(galaxy_map, lensing_map)
ell = np.arange(len(cl_cross))

import matplotlib.pyplot as plt
plt.plot(ell, cl_cross)
plt.xlabel(r'Multipole $\ell$')
plt.ylabel(r'$C_\ell^{\kappa g}$')
plt.title('Cross-Power Spectrum: Galaxy Density & CMB Lensing')
plt.show()



# Interpret Results

# The cross-power spectrum reflects the correlation between the galaxy distribution and the matter distribution traced by the CMB lensing map.

#Discuss consistency with ΛCDM predictions or potential deviations.


# Extensions
# Compare results with theoretical predictions from CAMB or CLASS, including modeling galaxy bias.
# Investigate redshift bins to study the evolution of the cross-correlation.
# This exercise provides hands-on experience with observational data and insights into the connection between large-scale structure and the CMB.






