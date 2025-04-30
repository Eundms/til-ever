from abc import ABC, abstractmethod

# 추상 클래스 : 인스턴스를 만들지 못하는 클래스로 상속을 통해서만 사용
class Game(ABC):
    def start(self):
        self.initialize()
        self.play()
        self.end()
    @abstractmethod
    def initialize(self):
        pass
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def end(self):
        pass


class Chess(Game):
    def initialize(self):
        print("체스 판 준비")
    def play(self):
        print("체스 시작")
    def end(self):
        print("체스 끝")

chess = Chess()
chess.initialize()
chess.play()
chess.end()