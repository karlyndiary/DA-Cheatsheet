- Parameters are variables that allow users to replace a fixed constant value
- Parameters can be used in calculations, filters, text, bins, reference lines and more.
- Use Case
  - Dynamic Calculations
    ```
    IF SUM([Profit]) > [Profit Parameter] THEN 'GREEN'
    ELSE 'RED'
    END
    ```
  - Dynamic Reference Lines
  - Dynamic Filters
  - Dynamic swap between dimensions and dynamic swap between measures
  - Dynamic Texts
  - Dynamic Bins in Histogram
