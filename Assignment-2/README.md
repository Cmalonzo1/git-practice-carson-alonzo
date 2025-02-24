# <u>Work Documentation</u>

## What does this code do?
- This code grabs population density data from Natural World Data, extracts the information from the zip file, and visualizes 
the data through an interactive globe.

## Procedures
1. I created the project inside my personal GitHub repository and inserted the code into a python file.
2. I installed the necessary packages for this assignment, including Geopandas, pandas, pipdeptree, pipreqs, and plotly, 
through the VE
3. After installing the libraries, I ensured the program ran.
4. After running the program for the first time, I generated the requirements.txt file using pipreqs. I verified that an import error appeared after the libraries were removed
5. I removed the packages and reinstalled them using the requirements.txt file
6. I ensured the program worked after reinstalling using the requirements.txt file

## Problems Encountered
### My problems came down to creating the requirements.txt file and uninstalling from it.

- I created the directory within my personal GitHub repository. I believe the path caused issues creating
the file as I constantly encountered this issue: **UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 81: invalid start byte** 

    However, I experienced no issues generating the file in a different directory hosted outside of my GitHub repository.
- When I tried uninstalling the libraries through my txt file, I didn't notice I was using the wrong path, so the terminal
couldn't find my requirements.txt file
