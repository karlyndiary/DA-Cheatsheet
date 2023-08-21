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
-  Highlighting tables: Apply colours to a data frame
    - def highlight_min_max(data_frame, min_color, max_color) : 
    - numeric_cols = data_frame.select_dtypes ( [np. number]).columns
    - #This first line creates a styler object
    - final data = data_frame.style.highlight_max (color=max_color, subset=numeric_cols)
    - #On this second line, no need to use ".style"
    - final data final data.highlight_min(color = min_color, subset=numeric_cols) 
    - return final data
    - #Function to apply ORANGE to min and GREEN to max
    - highlight_min_max (my_data, min_color='orange', max_color="green")
- Type hinting:

# RStudio
- Multiple line comment: Select all the lines and Ctrl + Shift + C
- New Script or new file: Ctrl + Shift + N
- When referencing script names from another script: Ctrl + click on the function -> this will direct you to the main function
- data.table package: Essential for Data cleaning, Data Wrangling, EDA
- Data Profiling: library(inspectdf) -> Displays the memory size of each column, lists all the columns in a pie chart, and checks for correlations between all numeric columns, similar to ggplot but better
- library(doParallel): It speeds up your execution time by running it in parallel

# Excel
- Right-click on the bottom bar to select or unselect the average, sum or max
- Analyze Data: Home -> All the way to the right (Analyze data)—suggested Analysis. Ask a question and the result will be provided as well. 
- Excel Table: Insert -> Table. This you can call in the table name itself. Example: =average(credit_risk[person_income]) -> credit_risk: the renamed table name, person_income: the column name
  - This is helpful when adding additional columns at the end. 
- Slicer: Insert -> slicer -> select all the columns you want to filter.
- Shortcuts
  - Select the entire row: Ctrl + Shift + ->
  - Select the entire data range: Ctrl + Shift + Down arrow
  - Select the entire column: Click on the column and Ctrl + Shift + Down arrow
  - To move between sheets: Ctrl + Page up/ Page down
  - To type in the headers continuously without moving down when hitting enter: Highlight the entire row and type
  - Statistical Analysis: Data Tab -> Analysis Option -> Analysis ToolPak -> ok. This now becomes an option
  - Filling in missing values: Highlight the range -> Home -> Find & Replace -> Special -> Select Blanks
  - Ctrl + Enter -> To fill in all the cells with the same value as before
  - Conditional Formatting: Select the columns -> Home -> Conditional Formatting option -> Highlight cell rules
  - Use Macros for repeated tasks: Developer -> Record Macros -> Give it a name and click on ok to start recording. Now you can do the usual repeated tasks and once done, stop recording. Click on the Macros button -> The recorded macro will be listed here and available for other workbooks as well.
