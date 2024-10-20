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
    - Groups combine similar related values into higher-level categories.
    - Groups are created using dimensions only.
    - Groups simplify data by categorizing data points into clear, relevant categories.
- Cluster Groups
  - A statistical technique is used to group similar data points.
  - Cluster Algorithms: K-means [Tableau pick], Hierarchical and Density-Based.
  - How it works?
    - We're going to go with three clusters. And after that, the algorithm going to pick three points. And we call them centroids. And then it's going to assign the data points to the nearest centroid. So for this data point, it can belong to the green cluster. And then it's going to go to the next data point and calculate the length between it and the three centroids. And then it can assign it to the nearest centroid for this is going to be the red cluster. So the algorithm can do that for all data points and assign them to the closest centroid. So in the end, we will have three clusters green red and blue.
- Sets
  - 
