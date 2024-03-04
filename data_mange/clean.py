import pandas as pd



df_airthai_02 = pd.read_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\source\\air4thai_02t_2024-02-27_2024-02-27.csv")
#print(df_airthai_02)
clean_df_airthai_02 = df_airthai_02.dropna(axis=1)
#print(clean_df_airthai_02)
clean_df_airthai_02.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean_airthai_02.csv")


df_airthai_03 = pd.read_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\source\\air4thai_03t_2024-02-27_2024-02-27.csv")
#print(df_airthai_03)
clean_df_airthai_03 = df_airthai_03.dropna(axis=1)
#print(clean_df_airthai_03)
clean_df_airthai_03.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean_airthai_03.csv")


df_airthai_05 = pd.read_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\source\\air4thai_05t_2024-02-27_2024-02-27.csv")
#print(df_airthai_05)
clean_df_airthai_05 = df_airthai_05.dropna(axis=1)
#print(clean_df_airthai_05)
clean_df_airthai_05.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean_airthai_05.csv")


df_airthai_08 = pd.read_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\source\\air4thai_08t_2024-02-27_2024-02-27.csv")
#print(df_airthai_08)
clean_df_airthai_08 = df_airthai_08.dropna(axis=1)
#print(clean_df_airthai_08)
clean_df_airthai_08.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean_airthai_08.csv")
