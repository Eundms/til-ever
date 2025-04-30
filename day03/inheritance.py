
class Person:
    def __init__(self, name = "noname"):
        self.name = name
    def printing(self):
        print("상위 클래스의 메서드")

class Student(Person):
    # 상위 클래스에 존재하는 메서드를 다시 정의하는 것을 메서드 오버라이딩이라고 한다
    # 상위 클래스의 메서드를 오버라이딩 하는 경우는 상위 클래스의 기능이 부족해서 추가하는 것이 목적이다
    def printing(self):
        super().printing()
        print("하위 클래스의 메서드")

student1 = Student()
# 상속을 받으면 하위 클래스의 인스턴스가 상위 클래스의 모든 멤버를 사용하는 것이 가능
student1.printing()
print(student1.name)

class Base1:
    def method(self):
        print("Base1의 메서드")

class Base2:
    def method(self):
        print("Base2의 메서드")

class Derived(Base1, Base2):
    def method(self):
        super().method() # Base1 메서드 호출
        super(Base1, self).method() # Base2 메서드 호출
        # Base2 다음에 존재하는 클래스의 메서드를 호출

instance = Derived()
instance.method()