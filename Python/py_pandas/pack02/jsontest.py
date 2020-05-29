import json

dictData = {'name':'tom', 'age':33, 'score':[90, 80, 50]}
str_val = json.dumps(dictData)
print(str_val, type(str_val)) #dumps를 함으로써 string으로 변환됨

json_val = json.loads(str_val)
print(json_val, type(json_val)) #str을 다시 dict로 변환 가능

# for k in json_val.keys():
#     print(k)
# for v in json_val.values():
#     print(v)
    
name_data = json_val.get('name')
age_data = json_val['age']
print(name_data, age_data)