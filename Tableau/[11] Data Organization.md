- Hierarchies
  - Level 0 - All - Root Node
  - Level 1 - Country
  - Level 2 - City
  - Level 3 - Pin Code - Leaf Node

- Level 0 to level 3 - Drill Down else Drill Up

- Hierarchies are only created in Dimensions, not measures

- To create a hierarchy
  - 1st method: Right-click on the field -> hierarchy -> Create hierarchy -> Give it a name -> Drag and drop the related field under this drop-down
  - 2nd method: Drag and drop one field onto another related field to create a hierarchy.

  - Date & Time Hierarchy
    - L1: Year
    - L2: Quarter
    - L3: Month
    - L4: Day
    - L5: Hour
    - L6: Minute
    - L7: Second

- Groups
  - Groups combine similar related values into higher-level categories, creating new dimension for data analysis.
  - How to create groups
    - In the Data Pane
      - Select the field -> Right Click -> Create -> Group -> Rename the field -> Select the similar distinct values and click on group -> Rename the group
    - In the View
      - Create the visualization -> Cluster -> Select the data points -> Right click -> Group
      - The new group will be created in the data pane, right-click to edit the name of the group in the group made.
- Cluster Groups
- Sets
