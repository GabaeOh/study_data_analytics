import pandas as pd

df_titanic = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
#print(df_titanic)

df_Name = pd.Series(df_titanic['Name'].unique())
#print(df_Name)

pattern_firstname = r'^([^,]+)' #성만 추출 

df_Name_firstname = df_Name.str.extract(pattern_firstname)
#print(df_Name_firstname)
#print(df_Name_firstname.isnull().sum()) #0 확인 

pattern_middlename = r'([A-Za-z]+)\.' # 결혼 여부 

df_Name_middlename = df_Name.str.extract(pattern_middlename)
#print(df_Name_middlename)
#print(df_Name_middlename.isnull().sum()) #0확인

#컬럼추가 
df_Name['firstname']= df_Name.str.extract(pattern_firstname)
#print(df_Name['firstname'])

df_Name['middlename']= df_Name.str.extract(pattern_middlename)
#print(df_Name['middlename'])


# apply 함수를 사용하여 중간 이름 추출
def extract_middle_name(name):
    pattern = r'([A-Za-z]+)\.'
    result = re.findall(pattern, name)
    if result:
        return result[0]
    else:
        return None

df_Name['MiddleName(apply적용)'] = df_Name.apply(extract_middle_name)
print(df_Name['MiddleName(apply적용)'])