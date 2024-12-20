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
  - We can use data sets to group up those data points. So sets can define your data based on specific criteria or selection into two groups of data. The first group we call the in group. And this group you're going to find all the data points that are included in the subsets of data. These data points are the members of the set. And the other group is the out-group. This group contains all the data points that are not included in the subsets of the data. So that means the data points in this group are not the members of the set. So the sets in Tableau divide our data into two groups the in and out groups.
  - When to use Sets?
    - To focus on specific data points
    - Compare the subset data to the remaining data
    - Actions

  - Methods to create sets
    - Fixed set [Manual Selection]
    - Dynamic set [Condition, Rank]
    - Combined set
      - Fill: In at least one set
      - Inner: In both sets
      - Left: member in set1 but not member in set2
      - Right: member in set2 but not member in set1

  - How to create sets?
    - Fixed: Right-click on field -> Create -> Sets [Manual Selection]
    - Dynamic Set [Condition]: Right-click on field -> Create -> Sets -> Condition -> By field -> Enter the condition and click on ok
    - Dynamic Set [Rank]: Right-click on field -> Create -> Sets -> Top -> By field -> Enter the top value or bottom value and click on ok
    - Combined set: Right-click on the created set -> Combined sets -> Give it a name -> Select the sets from both dropdowns -> Opt one of the four options -> Click on ok
  - Sets Use Case
    - To showcase only specific data points
    - To focus on a specific subset
    - Set as a filter

- Sets divide data based on specific criteria into two subsets :
  - IN: contains all members of the set.
  - Out: contains members not included in the set.
- Sets are useful for focusing on a subset of the data and comparing it with the remaining data.
- Sets add interactivity and dynamics to views by allowing users to define which subset they want to focus on.

- Bins & Histogram
  - Divide the data into groups of equal-sized containers resulting in a systematic data distribution.
  - Bins used to create charts called Histograms
  - Right-click on field -> Create -> Bins -> Mention the size of bins -> ok
  - Make the created bins continous by clicking on the arrow 
