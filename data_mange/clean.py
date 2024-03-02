import pandas as pd

df_airthai_02 = pd.read_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\source\\air4thai_02t_2024-02-27_2024-02-27.csv")
#print(df_airthai_02)
clean_df_airthai_02 = df_airthai_02.dropna(axis=1)
#print(clean_df_airthai_02)
clean_df_airthai_02.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean_airthai_02.csv")
