import pandas as pd

data =  { 'name' : ['Prashanth', 'vilas', 'Charan'], 
          'Subject': [ 'python', 'java', 'sql' ], 
          'skills': ['java','J2EE', 'MYSQL'] 
        }

df = pd.DataFrame(data)
# print("Data")
# print(df)



for index, row  in df.iterrows():
    print(f'{index}')
    print(f"{row['name']}")

date_list = ['2025-02-01', '2025-02-02', '2025-02-03', '2025-02-04']

df1 = pd.to_datetime(date_list)
print(df1)