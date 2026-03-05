import pandas as pd

list_of_files = ['status.csv', 'Summit Count.csv', 'Student Admission Plan.csv']

df = pd.read_csv(list_of_files[0])

df['TITLE_NAME_ENG'] = df['TITLE_NAME_ENG'].replace({
    'Mister': 'Mr.',
    'MR.': 'Mr.',
    'MR': 'Mr.',
    'MISSTRESS': 'Miss',
})

print(df['TITLE_NAME_ENG'].value_counts())
df['NATIONALITY'] = df['NATIONALITY'].replace({
    'ไทย': 'Thai',
})

print(df['NATIONALITY'].value_counts())
gender_mapping = {
    'Mr.': 'Male',
    'Miss': 'Female',
}
major_map = {
    'TRM': 'Tourism Management',
    'HPM': 'Hospitality Management',
    'TAM': 'Tourism & Aviation Business Management',
    'IHM': 'International Hotel, Event & Restaurant Management',
    'SIM': 'Service Innovation Management',
    'BIZ INNO': 'Business Innovation Management',
    'INNO': 'Innovation Management',
    'BIM': 'Business Innovation Management'
}
major2_map = {
    'TRM': 'Tourism Management',
    'HPM': 'Hospitality Management',
    'TAM': 'Tourism & Aviation Business Management',
    'IHM': 'International Hotel, Event & Restaurant Management',
    'BIZ INNO': 'Business Innovation Management',
    'INNO': 'Innovation Management',
    'BIM': 'Business Innovation Management',
    'SIM_BIM':'Service Innovation Management and Business Innovation Management'
}
df['fullname_major2'] = df['MAJOR_1'].map(major2_map)
df['fullname_major'] = df['MAJOR'].map(major_map)
df['gender'] = df['TITLE_NAME_ENG'].map(gender_mapping)
print(df.head())
# df.to_csv('Status.csv', index=False)
# print("savedstatus.csv.")


# 2
df = pd.read_csv(list_of_files[1])
df.fillna(0, inplace=True)
print(df.head())
# df.to_csv('Summit Count.csv', index=False)
# print("saved Summit Count.csv.")

# 3
df = pd.read_csv(list_of_files[2])
df.fillna(0, inplace=True)
print(df.head())
# df.to_csv('Student Admission Plan.csv', index=False)
# print("saved Student Admission Plan.csv.")