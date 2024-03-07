import pandas as pd

df_airthai = pd.read_csv('C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\clean02_air4thai_44t_2023-01-01_2024-02-27.csv')

data_for_train = df_airthai.drop(['Unnamed: 0', 'Unnamed: 0.1', 'DATETIMEDATA', 'stationID'], axis=1, inplace=False)
data_for_model = data_for_train.drop(index=(range(1114, len(data_for_train))))
data_for_test = data_for_train.drop(index=(range(0, 1114)))

data_for_train.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\data_train_air4thai_44t_2023-01-01_2024-02-27.csv")
data_for_model.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\data_model_air4thai_44t_2023-01-01_2024-02-27.csv")
data_for_test.to_csv("C:\\Users\\ASUS\\Desktop\\VS code\\PsuTerm02\\241-152\\final_project\\data_mange\\data_test_air4thai_44t_2023-01-01_2024-02-27.csv")

