- Workbook
  - Data -> send the extract as a .hyper
  - Data Source -> Tableau Data Source [.tds]
  - Data + Data Source
    - The users dont have access to the source system, cannot use the live connection. Don't mind sharing the data.
    - Send extract + Data Source -> .tdsx
    - Visualization -> Data Source + visualization [.twb]
  - For a combination of all 3 -> Data + Data Source + Visualization [.twbx] Tableau packaged workbook

- With Data
  - Data Source -> Extract -> [.hyper]
  - Data + Data Source -> [.tdsx]
  - Data + Data Source + Visualization [.twbx] 

- Without Data
  - Data Source -> Live -> [.tds]
  - Data + Data Source -> [.twb]
    
| **File Type** | **Tableau Desktop** | **Tableau Reader** | **Tableau Public** |
|---------------|---------------------|--------------------|--------------------|
| .HYPER        | ✓                   | ✗                  | ✗                  |
| .TDSX         | ✓                   | ✗                  | ✗                  |
| .TWBX         | ✓                   | ✓                  | ✓                  |
| .TDS          | ✓                   | ✗                  | ✗                  |
| .TWB          | ✓                   | ✗                  | ✗                  |

Metadata: Data about the data. Stored as XML file. It describes your data and what you have done in the workbook, anything you click.
Data: The actual data stored as .hyper file. Data is stored in columns in the memory of Tableau.
