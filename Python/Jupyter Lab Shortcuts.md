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
