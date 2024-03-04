import pandas as pd

df_airthai = pd.read_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\source\\air4thai_44t_2023-01-01_2024-02-27.csv")
print(df_airthai)

clean_data01 = df_airthai.dropna(axis=1)
clean_data02 = df_airthai.dropna(axis=1, thresh=5)

clean_data01.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean01_air4thai_44t_2023-01-01_2024-02-27.csv")
clean_data02.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean02_air4thai_44t_2023-01-01_2024-02-27.csv")



