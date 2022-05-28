class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name (self, new_name):
        self.name = new_name
        print("My name is", self.name)
    def change_age (self, new_age):
        self.age = new_age
        int_age = int(self.age)
        print("I am aged", int_age)
    def add_track (self, tracks):
        self.tracks.append(tracks)
        print ("These is the track I enrolled:", tracks)
    def get_score (self):
        print("I scored", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
