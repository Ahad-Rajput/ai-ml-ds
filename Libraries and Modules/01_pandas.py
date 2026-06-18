

import pandas as pd

df = pd.read_csv('data.csv')  # read the data from csv and store it in df 
# print(df)

# print(df['name'])  # Use [] brackets with dataframe to print a spcific column data


df_1 = df[df['name'] == 'Ahmad']   # Filter the dataset and gives only data of name: Ahmad
# print(df_1)

df_2 = df[df['marks'] <= 75]
# print(df_2)



# print(df.head())  # Gives first 5 rows of dataset
# print(df.tail())  # Gives last 5 rows of dataset
"""
- U can also specifies the no. rows like this, 'df.head(3)' => This'll print first 3 rows
- Same for tail()
""" 

# print(df.info())  # Provide information about the data


# print(df.describe())  # Provide basic statistics about our data




# print(df.columns)  # Display columns name


# print(df.shape)   # Display total no. of rows  nd columns


print(df['marks'].sum())  # Take sum of 'marks' column

print(df['marks'].mean())  # Take mean of 'marks' column

print(df['marks'].min())  # gives minimum value from 'marks' column

print(df['marks'].max())  # gives maximum value from 'marks' column



max_std = df[df['marks'] == df['marks'].max()]  # Filter the data of student with maximum marks
# print(max_std)

df.to_excel('some_data.xlsx')
print(df)
"""
df.to_excel() <- This create an excel file and copy our csv data in it
=> For that you should have installed "openpyxl" library
"""

# print("Everything is fine!")