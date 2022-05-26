
class Student:
    def __init__(self,  name, age, tracks, score):
        self.tracks = tracks
        self.name = name
        self.age = age
        self.score = score

    def set_height(self, height):
        self.height = height

    def change_age(self, age):
        self.age = age

    def get_score(self):
        return self.score

    def change_name(self, name):
        self.name = name

    def add_track(self, track):
        self.tracks = self.tracks.append(track)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)


Bob.change_name('Peter')
Bob.change_age(34)
Bob.add_track('UI/UX')
Bob.get_score()
