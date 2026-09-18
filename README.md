# Session 3 — Intro to Data Course

This repository contains the materials for **Session 3** of *Intro to Data*.  
- Slides: see [`slides/`](./slides/) folder  
- Notebooks: see [`notebooks/`](./notebooks/) folder 
---

## 📑 Session Outline

1. **Python basics**
	- Run Python in notebook cells
	- Read basic syntax, variables, data types, operators, and control flow
	- Work with functions and built-in collections
	- Import modules and use standard-library tools
	- [Open `00_python_basics.ipynb`](./notebooks/00_python_basics.ipynb)

2. **Choosing the right plot**
	- Understand distribution, comparison, relationship, time, and part-to-whole plots
	- See why visualising data can reveal patterns hidden by summary statistics
	- Compare raw observations with summaries
	- Practise choosing axes, plot families, and appropriate visual encodings
	- [Open `01_week3_plot_families.ipynb`](./notebooks/01_week3_plot_families.ipynb)

3. **The first look at a dataset**
	- Load data from common file formats with pandas
	- Inspect dataset size, rows, column types, missing values, and duplicates
	- Summarise numeric variables and examine distributions
	- Explore relationships with a correlation matrix
	- [Open `02_week3_first_look.ipynb`](./notebooks/02_week3_first_look.ipynb)


---
## 🚀 Environment Setup

Before starting, **fork this repository** and create a fresh Python virtual environment.  
All required libraries are listed in `requirements.txt`.

> ⚠️ If you encounter errors during `pip install`, try removing the version pinning for the failing package(s) in `requirements.txt`.  
> On Apple M1/M2 systems you may also need to install additional system packages (the “M1 shizzle”).

---

### macOS / Linux (bash/zsh)

```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (PowerShell)
```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (Git Bash)
```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

You’re now ready to run the session notebooks!

Deactivate the environment when you’re done:
```bash
deactivate
```
