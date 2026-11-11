# Pandas is a library used for data manipulation and data analysis.
# It helps us Read data from CSV and Excel files, Organise data into rows and columns, Search and filter data etc
# Used in data analysis, machine learning, AI, financial data analysis etc

# Pandas has two main data structures: Series and DataFrame
# A Series is a 1D labelled array that can store data. It is like a single column in an Excel spreadsheet.
# A DataFrame is a 2D labelled data structure consisting of rows and columns. Its like an Excel spreadsheet or a database table.

import pandas as pd

marks = pd.Series([42, 20, 66, 100, 80])
print(marks) # prints with index number and value by default

data = {
    "Name": ["Ahmed", "Nihan", "Ali", "Umar"],
    "Age": [21, 22, 20, 21],
    "Mark": [85, 92, 76, 88]
} # dictionary

df = pd.DataFrame(data) # Converts the dictionary to a dataframe
print(df) # prints as a table

# Pandas can read and write to a CSV (Comma-Separated Values) file
# It is also possible to read from an excel file
c_read = pd.read_csv("countries.csv")
print(c_read)