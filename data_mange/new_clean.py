import pandas as pd

df_airthai = pd.read_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\source\\air4thai_44t_2023-01-01_2024-02-27.csv")


clean_data02 = df_airthai.dropna(axis=1, thresh=1)

not_number_columns = ['DATETIMEDATA', 'stationID']
number_columns = clean_data02.columns.difference(not_number_columns)
clean_data02[number_columns] = clean_data02[number_columns].fillna(clean_data02[number_columns].mean())

clean_data02.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean02_air4thai_44t_2023-01-01_2024-02-27.csv")




