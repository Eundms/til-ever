
import pymysql
def insertPrepared(cursor) :
    cursor.execute("insert into usertbl values(%s, %s, %s, %s, %s, %s)", ('efa', '이럴리', 2000, '서울', '01012345678', '1970-10-31'))

try:
    con = pymysql.connect(host='127.0.0.1', port=3306, user = 'root', passwd= 'root', db = 'autoever', charset = 'utf8mb4')
    print(con)

    # sql 실행 객체 생성
    cursor = con.cursor()

    # # 삽입 실행
    # # insertPrepared(cursor)
    # # cursor.execute("insert into usertbl values('ljy', '이진연', 1970, '서울', '01012345678', '1970-10-31')")
    #
    # # Prepared Statement
    # cursor.execute("delete from usertbl where name = %s", ('이지연'))
    #
    # # 조회 구문 실행
    # cursor.execute("select * from usertbl")
    #
    # # 데이터 가져오기
    # data = cursor.fetchone()
    # print(type(data)) # tuple
    # # 에러 # data[0] = 'kt'
    #

    # 프로시저
    cursor.callproc('myproc', args=('momo', '모모', 1996, '교토', '01000000000', '1986-11-09'))
    con.commit()

    # 데이터 여러개 가져오기
    datas = cursor.fetchall()
    print(type(datas)) # tuple

    for data in datas:
        print(data)

    con.close()

except Exception as e:
    print("MongoDB 연결 실패:", e)
