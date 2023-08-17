# Git Commands

- clone: Download the file from the website to the local machine
- add: Track files and save changes in Git
- commit: Save your files in Git
- push: Upload Git commands to a remote repo
- pull: When there is a code change and you want to bring it to the local machine
- ls: List files
- git init: Initializes a new Git repository in the current directory

# Jupyter Notebook Shortcuts

- To scroll down fast: Space
- To scroll to the top fast: Shift + Space
- To merge cells: Shift + m
- To go all the way up: Ctrl + Up arrow
- To go all the way down: Ctrl + Down arrow
- To clear the entire code line: Ctrl + d
- Multi cursor[to change a particular word, ex: the file's name]: Hold down Ctrl  and click on different places to edit the word. [Works only on one cell at a time]
- Code Completion: Type in half the word and click on the tab to autocomplete
- Magic commands:
  - !ls: to list the files inside the Jupyter notebook
  - %pwd: Returns the path
  - !pip install seaborn: Can be run inside the notebook
  - %mkdir test: Creates a file called test in the current directory
  - %%bash: when using multiple lines of magic command, this can be used
  - %lsmagic: Lists all the magic codes that can be used within the notebook
    - Line magic: runs only for one line -> % used 
    - Cell magic: runs for the entire line -> %% used
  - %%timeit: returns the total time taken to run the cell

# Python

- Chaining comparison: if 4 < mark <=6: print("pass")
- List comprehension(used to list all the columns that start with a particular word) for loop can be used. 
    - loan_columns = [] 
    - for col in credit.columns:
    - if 'loan' in col:
    - loan_columns.append(col)
    - or loan_columns = [col for col in credit.columns if 'loan' in col]
    - loan_columns -> This returns the list of columns that contains the word 'loan' in it.
-  Pandas Profiling:
-  Highlighting tables: Apply colors to a dataframe
    - def highlight_min_max(data_frame, min_color, max_color) : 
    - numeric_cols = data_frame.select_dtypes ( [np. number]).columns
    - #This first line create a styler object
    - final data = data_frame.style.highlight_max (color=max_color, subset=numeric_cols)
    - #On this second line, no need to use ".style"
    - final data final data.highlight_min(color = min_color, subset=numeric_cols) 
    - return final data
    - #Function to apply ORANGE to min and GREEN to max
    - highlight_min_max (my_data, min_color='orange', max_color="green")
