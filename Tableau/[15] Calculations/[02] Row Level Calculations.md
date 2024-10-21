### Number Functions

- Ceiling: Rounds up the number. Ceiling(1.8) => 2
  - Ceiling([Sales])
- Floor: Rounds down the number. Floor(1.8) => 1
  - Floor([Sales])
- Round: Round the number to its nearest integer. Round(1.8) => 2
  - Round([Sales]), Round([Sales], 2)

### String Function

- Change Case
  - Upper: Uppercase. Upper(Name) => LOLA. Good for Codes
  - Lower: Lowercase. Lower(Name) => lola. Good for long sentences.

- Remove Spaces
  - LTrim: Removes leading spaces. LTrim( Product) => Product
  - RTrim: Removes trailing spaces. RTrim(Product ) => Product
  - Trim: Removes leading and trailing spaces. Trim( Product ) => Product

- Extract
  - Left: Left(Canon-456-cer5, 5) => Canon
  - Right: Right(Canon-456-cer5, 4) => cer5
  - Mid: Mid(Canon-456-cer5, start, length) => Mid(Canon-456-cer5, 7, 3) => 456

- Search for patterns
  - Startwith: Returns True or False.
    - Startwith(string, substring)
    - startwith(Canon-456-cer5, "Canon") => True
    - startwith(Canon-456-cer5, "non") => False
  - Endwith: Returns True or False.
    - Endwith(string, substring)
    - endwith(Canon-456-cer5, "cer5") => True
    - endwith(Canon-456-cer5, "cer") => False
  - Contains: Returns True or False.
    - Contains(string, substring)
    - Contains(Canon-456-cer5, "-") => returns True
    - Contains(Canon-456-cer5, "54") => returns False
  - Find: Returns the position. Contains(Canon-456-cer5, "-") => returns 6 
  - Findnth: Returns the position.

- Combine and split
  - Concat
  - Split

- Replace
  - Replace
