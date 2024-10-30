- Filter means removing or selecting specific data subsets for different purposes and use cases.
- Use Case
  - Reduce the size of the dataset to optimize performance
  - Interactivity and analysis by offering filters to users.
  - Data Security by removing sensitive data.
  - Data Access Control by applying RLS (Row Level Security)
- Filter Type
  - Optimize & Performance
    - Extract Filer
      - Filter between the source system and data source 
    - Data Source Filter
      - Filter between the data source and the worksheet
    - Context Filter
      - Filter on the worksheet
  - Interactivity: Offer on the Dashboard
    - Dimension Filter
    - Measure Filter
    - Table Calculation Filter

| Filter Type       | Extract Filter                                  | Data Source Filter                           |
|-------------------|-------------------------------------------------|----------------------------------------------|
| Connection Type   | Only Extract Connection                         | Extract & Live Connection                    |
| Availability      | Only Tableau Desktop                            | Tableau Desktop & Public                     |
| Purpose           | - Optimize Load Performance<br>- Optimize Performance in Views | - Optimize Performance in Views<br>- Hide Sensitive Data |

| Feature                  | Normal Filter                                  | Context Filter                                           |
|--------------------------|-----------------------------------------------|----------------------------------------------------------|
| **Filter Order**         | Applied independently; each filter acts on the entire dataset | Applied first, creating a subset of data for other filters |
| **Effect on Other Filters** | No effect on other filters                 | Limits data for all subsequent filters                    |
| **Use Case**             | General filtering                             | Dependent filtering; improves performance with large datasets |
| **Performance Impact**   | May slow down with multiple complex filters   | Can enhance performance by reducing data processed by other filters |
| **Typical Example**      | Filtering for a single region or category     | Filtering a specific region as a context before applying further category filters |

- The filters affect all the worksheets
- Data Source Filter
  - Data Source Tab -> Filter -> Add -> Select the field -> Select the rows to exclude -> Click on exclude -> Click ok -> Click ok
- Context Filter
  - Filter on the worksheet
  - Context filters don't help protect sensitive data -> The show filter option also has the option to list all the values in the database
- Dimension Filter
  - Click on the down arrow -> Show Filter
- Measure Filter
  - Click on the down arrow -> Show Filter. Check the aggregation of the field and choose the same from the menu.
- Table Calculation Filter
  - Click the down arrow -> Quick Table Calculation -> Aggregation -> Ctrl + field to filters -> Show Filter

- Apply one filter to multiple visualizations or worksheets
  - Click on the drop-down arrow -> Apply to worksheets -> 4 Options
  - Only this worksheet is the default option for the filter
  - 
