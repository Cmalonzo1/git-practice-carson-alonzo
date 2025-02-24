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

<details>
geopandas==1.0.1
  - numpy [required: >=1.22, installed: 2.2.3]
  - packaging [required: Any, installed: 24.2]
  - pandas [required: >=1.4.0, installed: 2.2.3]
    - numpy [required: >=1.26.0, installed: 2.2.3]
    - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
      - six [required: >=1.5, installed: 1.17.0]
    - pytz [required: >=2020.1, installed: 2025.1]
    - tzdata [required: >=2022.7, installed: 2025.1]
  - pyogrio [required: >=0.7.2, installed: 0.10.0]
    - certifi [required: Any, installed: 2025.1.31]
    - numpy [required: Any, installed: 2.2.3]
    - packaging [required: Any, installed: 24.2]
  - pyproj [required: >=3.3.0, installed: 3.7.1]
    - certifi [required: Any, installed: 2025.1.31]
  - shapely [required: >=2.0.0, installed: 2.0.7]
    - numpy [required: >=1.14,<3, installed: 2.2.3]
pipdeptree==2.25.0
  - packaging [required: >=24.1, installed: 24.2]
  - pip [required: >=24.2, installed: 25.0.1]
pipreqs==0.5.0
  - docopt [required: ==0.6.2, installed: 0.6.2]
  - ipython [required: ==8.12.3, installed: 8.12.3]
    - backcall [required: Any, installed: 0.2.0]
    - colorama [required: Any, installed: 0.4.6]
    - decorator [required: Any, installed: 5.2.0]
    - jedi [required: >=0.16, installed: 0.19.2]
      - parso [required: >=0.8.4,<0.9.0, installed: 0.8.4]
    - matplotlib-inline [required: Any, installed: 0.1.7]
      - traitlets [required: Any, installed: 5.14.3]
    - pickleshare [required: Any, installed: 0.7.5]
    - prompt_toolkit [required: >=3.0.30,<3.1.0,!=3.0.37, installed: 3.0.50]
      - wcwidth [required: Any, installed: 0.2.13]
    - Pygments [required: >=2.4.0, installed: 2.19.1]
    - stack-data [required: Any, installed: 0.6.3]
      - asttokens [required: >=2.1.0, installed: 3.0.0]
      - executing [required: >=1.2.0, installed: 2.2.0]
      - pure_eval [required: Any, installed: 0.2.3]
    - traitlets [required: >=5, installed: 5.14.3]
  - nbconvert [required: >=7.11.0,<8.0.0, installed: 7.16.6]
    - beautifulsoup4 [required: Any, installed: 4.13.3]
      - soupsieve [required: >1.2, installed: 2.6]
      - typing_extensions [required: >=4.0.0, installed: 4.12.2]
    - bleach [required: !=5.0.0, installed: 6.2.0]
      - webencodings [required: Any, installed: 0.5.1]
    - defusedxml [required: Any, installed: 0.7.1]
    - Jinja2 [required: >=3.0, installed: 3.1.5]
      - MarkupSafe [required: >=2.0, installed: 3.0.2]
    - jupyter_core [required: >=4.7, installed: 5.7.2]
      - platformdirs [required: >=2.5, installed: 4.3.6]
      - pywin32 [required: >=300, installed: 308]
      - traitlets [required: >=5.3, installed: 5.14.3]
    - jupyterlab_pygments [required: Any, installed: 0.3.0]
    - MarkupSafe [required: >=2.0, installed: 3.0.2]
    - mistune [required: >=2.0.3,<4, installed: 3.1.2]
    - nbclient [required: >=0.5.0, installed: 0.10.2]
      - jupyter_client [required: >=6.1.12, installed: 8.6.3]
        - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
          - platformdirs [required: >=2.5, installed: 4.3.6]
          - pywin32 [required: >=300, installed: 308]
          - traitlets [required: >=5.3, installed: 5.14.3]
        - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
          - six [required: >=1.5, installed: 1.17.0]
        - pyzmq [required: >=23.0, installed: 26.2.1]
        - tornado [required: >=6.2, installed: 6.4.2]
        - traitlets [required: >=5.3, installed: 5.14.3]
      - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
        - platformdirs [required: >=2.5, installed: 4.3.6]
        - pywin32 [required: >=300, installed: 308]
        - traitlets [required: >=5.3, installed: 5.14.3]
      - nbformat [required: >=5.1, installed: 5.10.4]
        - fastjsonschema [required: >=2.15, installed: 2.21.1]
        - jsonschema [required: >=2.6, installed: 4.23.0]
          - attrs [required: >=22.2.0, installed: 25.1.0]
          - jsonschema-specifications [required: >=2023.03.6, installed: 2024.10.1]
            - referencing [required: >=0.31.0, installed: 0.36.2]
              - attrs [required: >=22.2.0, installed: 25.1.0]
              - rpds-py [required: >=0.7.0, installed: 0.23.1]
              - typing_extensions [required: >=4.4.0, installed: 4.12.2]
          - referencing [required: >=0.28.4, installed: 0.36.2]
            - attrs [required: >=22.2.0, installed: 25.1.0]
            - rpds-py [required: >=0.7.0, installed: 0.23.1]
            - typing_extensions [required: >=4.4.0, installed: 4.12.2]
          - rpds-py [required: >=0.7.1, installed: 0.23.1]
        - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
          - platformdirs [required: >=2.5, installed: 4.3.6]
          - pywin32 [required: >=300, installed: 308]
          - traitlets [required: >=5.3, installed: 5.14.3]
        - traitlets [required: >=5.1, installed: 5.14.3]
      - traitlets [required: >=5.4, installed: 5.14.3]
    - nbformat [required: >=5.7, installed: 5.10.4]
      - fastjsonschema [required: >=2.15, installed: 2.21.1]
      - jsonschema [required: >=2.6, installed: 4.23.0]
        - attrs [required: >=22.2.0, installed: 25.1.0]
        - jsonschema-specifications [required: >=2023.03.6, installed: 2024.10.1]
          - referencing [required: >=0.31.0, installed: 0.36.2]
            - attrs [required: >=22.2.0, installed: 25.1.0]
            - rpds-py [required: >=0.7.0, installed: 0.23.1]
            - typing_extensions [required: >=4.4.0, installed: 4.12.2]
        - referencing [required: >=0.28.4, installed: 0.36.2]
          - attrs [required: >=22.2.0, installed: 25.1.0]
          - rpds-py [required: >=0.7.0, installed: 0.23.1]
          - typing_extensions [required: >=4.4.0, installed: 4.12.2]
        - rpds-py [required: >=0.7.1, installed: 0.23.1]
      - jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
        - platformdirs [required: >=2.5, installed: 4.3.6]
        - pywin32 [required: >=300, installed: 308]
        - traitlets [required: >=5.3, installed: 5.14.3]
      - traitlets [required: >=5.1, installed: 5.14.3]
    - packaging [required: Any, installed: 24.2]
    - pandocfilters [required: >=1.4.1, installed: 1.5.1]
    - Pygments [required: >=2.4.1, installed: 2.19.1]
    - traitlets [required: >=5.1, installed: 5.14.3]
  - yarg [required: ==0.1.9, installed: 0.1.9]
    - requests [required: Any, installed: 2.32.3]
      - certifi [required: >=2017.4.17, installed: 2025.1.31]
      - charset-normalizer [required: >=2,<4, installed: 3.4.1]
      - idna [required: >=2.5,<4, installed: 3.10]
      - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]
plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.27.1]
  - packaging [required: Any, installed: 24.2]
tinycss2==1.4.0
  - webencodings [required: >=0.4, installed: 0.5.1]

<summary>
pipdeptree output
</summary>
</details>
