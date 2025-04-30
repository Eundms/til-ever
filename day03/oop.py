class Student :
    schoolName = "우도 초등학교"
    # 인스턴스를 생성할 때 호출하는 메서드 : 생성자, 초기화 메서드
    def __init__(self, name="이름없음"):
        self.name = name
    def __del__(self):
        print("인스턴스가 소멸될 떄 호출됨")

    def insa(self):
        print("안녕하세요")

    def printName(self, name):
        # 인스턴스 속성 생성
        self.num = 1
        print(f"이름은 {name}")

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    # 파이썬에서는 @로 시작하는 단어를 decorator라고 한다
    # 함수를 만들 때 특별한 코드를 삽입해서 기능을 추가한다
    @staticmethod
    def smethod():
        print("static method")
    @classmethod
    def cmethod(cls):
        print("class method")
        print(cls)

student = Student()
student.printName("아담")

# 기본 상태
print(f"클래스로 접근 : {Student.schoolName} / 인스턴스로 접근 : {student.schoolName}")

# 클래스 이용해서 수정
Student.schoolName = "제일 중학교"
print(f"클래스로 접근 : {Student.schoolName} / 인스턴스로 접근 : {student.schoolName}")

# 인스턴스로 수정
student.schoolName = "명덕 고등학교"
print(f"클래스로 접근 : {Student.schoolName} / 인스턴스로 접근 : {student.schoolName}")

# printName을 호출할 떄 num 인스턴스 변수 생성
print(student.num)

# Getter Setter 이용
student = Student()
student.setName("이름임")
student.getName()

student = None

# 참조 +1 되는지 확인해보자
student1 = Student()
student2 = student1
student1 = None
student2 = None
print("소멸되나?")


# __slots__ 는 클래스에서 정의할 수 있는 속성을 제한함
class Student:
    # 특정한 속성만 인스턴스가 소유하도록 할 때 사용하는 속성
    __slots__= ["num", "name"]
    def __init__(self):
        pass
stu = Student()
stu.num = 1
stu.name = "adam"

stu1 = Student()
# stu1.bunho = 1 # 안됨
# stu1.irum = "adam" # 안됨


class Student:
    def __init__(self, name="noname", age = 0):
        self.name = name
        # 이 속성은 클래스 내부에서는 사용이 가능하지만 클래스 외부에서는 사용 불가
        self.__age = age

student99 = Student()
print(student99.name)
#print(student99.__age) # 에러

# private : __필드명
class Student:
    def __init__(self, name="noname", age = 0):
        self.__name = name
        self.__age = age
    def setName(self, name):
        print("setter 호출")
        self.__name = name
    def getName(self):
        print("getter 호출")
        return self.__name

    name = property(fget=getName, fset=setName)

student99 = Student()
student99.setName("쥬니")
print(student99.getName())

# property 사용한다면
student99.name = "으아아아"
print(student99.name)

