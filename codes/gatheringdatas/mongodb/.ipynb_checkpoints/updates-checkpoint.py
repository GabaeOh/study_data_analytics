import pymongo as mg

client = mg.MongoClient(host='mongodb://localhost:27017')
database = client['study_data_analytics'] #Database 선택
collection = database['collect_update'] # 테이블 선택

# 여러 문서 삽입
documents = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 35, "city": "Incheon"}
]
#collection.insert_many(documents)
#하나만 update
collection.update_one({"name":"Alice"},{"$set":{"age":26}})