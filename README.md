# Physics_and_We

This project involves processing and analyzing spectrometric data using Python. The primary tasks include visualizing data, converting intensity measurements into vectors, simplifying those vectors, and identifying unknown materials based on their spectral data.

## Table of Contents

1. [Introduction to Physics and We](#introduction-to-physics-and-we)
2. [Introduction to this project](#introduction-to-this-project)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Data Input](#data-input)
    - [Data Visualization](#data-visualization)
    - [Vector Conversion and Subspace Creation](#vector-conversion-and-subspace-creation)
    - [Material Identification](#material-identification)


## Introduction to Physics and We

Welcome to **Physics and We**. 
Physics and We is an  educational camp․ Within the framework of the camp, a digital spectrometer will be designed and prepared, which will make it possible to study the composition of different liquids.


## Introduction to this project

This project provides tools for analyzing spectrometric data, including:

- Reading and visualizing spectral data.
- Converting spectral intensities into vectors and making them orthogonal.
- Projecting the intensity vector of the unknown material onto the vector subspace of the orthogonal vectors.
- Reversing orthogonal vectors to determine the ratio of mixed substances.

## Installation

To get started with this project, clone the repository and install the required Python packages:

```bash
git clone git@github.com:Chalyan/Physics_and_We.git
cd Physics_and_We/
python -m pip install -r requirements.txt
python main_loop.py
```

## Usage

### Data Input

Spectrometric data should be provided in files containing wavelength and intensity information. The data files should be in a format readable by Python (e.g., CSV).

### Data Visualization

By plotting the CSV file in Python, you can create graphs for individual measurements or for all the measurements combined, as shown below:

<insert pictures>

### Vector Conversion and Subspace Creation

This code can convert intensity measurements into vectors, simplify them using orthogonalization and create vector subspace using the orthogonal vectors

### Material Identification

To identify an unknown material code projects the given intensity vector onto the vector subspace: