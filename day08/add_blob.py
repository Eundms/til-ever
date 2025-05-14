
import pymysql

try:
    con = pymysql.connect(host='127.0.0.1', port=3306, user = 'root', passwd= 'root', db = 'autoever', charset = 'utf8mb4')
    # sql 실행 객체 생성
    cursor = con.cursor()

    # 파일의 내용을 읽을 수 있는 준비
    filename = 'image/dangun.jpg'
    f = open(filename, 'rb')

    # 파일의 내용 읽기
    photo = f.read()
    cursor.execute("insert into member values(%s, %s, %s)", ('당근', "dangun.jpg", photo))

    cursor.execute("select * from member")
    datas = cursor.fetchall()

    for data in datas:
        # 파일명을 생성
        f = open(data[1], 'wb')
        # 파일 실제로 기록
        f.write(data[2])
        f.close()

    con.commit()
except Exception as a:
    print(a)