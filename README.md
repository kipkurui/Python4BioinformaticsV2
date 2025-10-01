# Python For Bioinformatics

Introduction to Python for Bioinformatics - available at https://github.com/kipkurui/Python4BioinformaticsV2.

**Python Version: 3.13** (Latest stable release)

<small><small><i>

## Attribution
These tutorials are an adaptation of the Introduction to Python for Maths by [Andreas Ernst](http://users.monash.edu.au/~andreas), available from https://gitlab.erc.monash.edu.au/andrease/Python4Maths.git. The original version was written by Rajath Kumar and is available at https://github.com/rajathkumarmp/Python-Lectures.

These notes have been greatly amended and updated for the MSC Bioinformatics and Molecular Biology at Pwani university, sponsored by EANBiT by [Caleb Kibet](https://twitter.com/calkibet)
</small></small></i>

# Quick Introduction to Jupyter Notebooks

Throughout this course, we will be using Jupyter Notebooks.These notes are provided for you want to set it up in your Computer. 

## Introduction
The Jupyter Notebook is an interactive computing environment that enables users to author notebooks, which contain a complete and self-contained record of a computation. These notebooks can be shared more efficiently. The notebooks may contain:
* Live code
* Interactive widgets
* Plots
* Narrative text
* Equations
* Images
* Video

It is good to note that "Jupyter" is a loose acronym meaning Julia, Python, and R; the primary languages supported by Jupyter. 

The notebook can allow a computational researcher to create reproducible documentation of their research. As Bioinformatics is datacentric, use of Jupyter Notebooks increases research transparency, hence promoting open science. 

## First Steps

### Installation

#### Option 1: Using Conda Environment (Recommended)

1. [Download Miniconda](https://www.anaconda.com/download/) or Anaconda for your specific OS
    - Linux: `wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`
    - Mac: `curl https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`
    - Windows: [Download installer](https://docs.anaconda.com/anaconda/install/windows/)

2. Install Miniconda:
    - Linux/Mac: `bash Miniconda3-latest-*.sh`
    - Windows: Run the downloaded .exe installer
    - Follow all prompts (accept defaults if unsure)

3. Close and re-open your terminal

4. Verify installation:
    ```bash
    conda --version
    ```

5. Create the conda environment using the provided `environment.yml` file:
    ```bash
    conda env create -f environment.yml
    ```

6. Activate the environment:
    ```bash
    conda activate python4bioinformatics
    ```

#### Option 2: Manual Environment Setup

If you prefer to create the environment manually:

```bash
conda create --name python4bioinformatics python=3.13
conda activate python4bioinformatics
conda install -c conda-forge jupyterlab numpy pandas matplotlib seaborn scipy biopython
```

## How to learn from this resource?

1. Clone the repository:
    ```bash
    git clone https://github.com/kipkurui/Python4BioinformaticsV2.git
    cd Python4BioinformaticsV2
    ```

    Or download as ZIP:
    ```bash
    wget https://github.com/kipkurui/Python4BioinformaticsV2/archive/master.zip
    unzip master.zip
    rm master.zip
    cd Python4BioinformaticsV2-master
    ```

2. Create and activate the conda environment:
    ```bash
    conda env create -f environment.yml
    conda activate python4bioinformatics
    ```

3. Launch Jupyter Lab:
    ```bash
    jupyter lab
    ```

**Using Jupyter Notebooks:**
- Each notebook contains cells with Python code or text
- Execute a cell: Press `Shift-Enter` (run and move to next) or `Ctrl-Enter` (run without moving)
- We recommend using Jupyter Lab for the best experience 

## For Windows
Follow the instructions available [here](https://docs.anaconda.com/anaconda/install/windows/)
### Further help

To learn more about Jupyter notebooks, check [the official introduction](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb) and [some useful Jupyter Tricks](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/). 

Book: http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf

# Python for Bioinformatics

## Introduction

Python is a modern, robust, high-level programming language. It is straightforward to pick up even if you are entirely new to programming. 

Python, similar to other languages like Matlab or R, is interpreted hence runs slowly compared to C++, Fortran or Java. However, writing programs in Python is very quick. Python has an extensive collection of libraries for everything from scientific computing to web services. It caters for object-oriented and functional programming with a module system that allows large and complex applications to be developed in Python. 

These lectures are using Jupyter notebooks which mix Python code with documentation. The python notebooks can be run on a web server or stand-alone on a computer.


## Contents

This course is broken up into a number of notebooks (lectures).
### Session 1
* [00](Notebooks/00.ipynb) This introduction with additional information below on how to get started in running python
* [01](Notebooks/01.ipynb) Basic data types and operations (numbers, strings) 
* [02](Notebooks/02.ipynb) String manipulation 

### Session 2
* [03](Notebooks/03.ipynb) Data structures: Lists and Tuples
* [04](Notebooks/04.ipynb) Data structures (continued): dictionaries

### Session 3
* [05](Notebooks/05.ipynb) Control statements: if, for, while, try statements
* [06](Notebooks/06.ipynb) Functions
* [07](Notebooks/07.ipynb) Scripting with python

### Session 4
* [08](Notebooks/08.ipynb) Data Analysis and plotting with Pandas
* [09](Notebooks/09.ipynb) Reproducible Bioinformatics Research
* [10](Notebooks/10.ipynb) Reproducible Bioinformatics Research

This is a tutorial style introduction to Python. For a quick reminder/summary of Python syntax, the following [Quick Reference Card](http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html) may be useful. A longer and more detailed tutorial style introduction to python is available from the python site at: https://docs.python.org/3/tutorial/.



    

## How to Contribute

To contribute, fork the repository, make some updates and send me a pull request. 

Alternatively, you can open an issue. 

## License
This work is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/.
