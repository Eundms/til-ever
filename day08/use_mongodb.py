from pymongo import MongoClient
def print_result(cursor):
    for car in cursor:
        print(car)
def insert_data():
    cars.insert_one({'name': '그랜저', 'price': 4000})
    cars.insert_many([
        {'name': '소나타', 'price': 2500},
        {'name': '제네시스', 'price': 6000}])
try:
    con = MongoClient('127.0.0.1', 27017)
    hyundai = con.hyundai
    cars = hyundai.cars
    # insert_data()
    cursor = cars.find()
    print_result(cursor)

    print("소나타만 검색해보기 : ")
    cursor = cars.find({'name':'소나타'})
    print_result(cursor)

    print("3000이상 검색해보기 : ")
    cursor = cars.find({'price': {'$gte' : 5000}})
    print_result(cursor)

    # ------ update ------
    cars.update_many({'name' : '소나타'}, {'$set': {'name' : 'sonata'}})

    # ------ delete ------
    cars.delete_one({'name': '제네시스'}) # 무조건 하나만 지워짐
    #cars.delete_many({'name': '그랜저'})
    print_result(cursor)
    print("MongoDB 연결 성공:", cars)

except Exception as e:
    print("MongoDB 연결 실패:", e)


