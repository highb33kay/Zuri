class Student:
    # [assignment] Skeleton class. Add your code here

    def _init_(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    # define the name as a string
    def change_name(self, name):
        self.name = name
        print("the student name is", self.name)

    # define change age method as an integer
    def change_age(self, age):
        self.age = int(age)
        print(self.name, "'s age is", self.age)

    # define add track method
    def add_track(self, tracks):
        self.tracks = tracks
        print(self.name, "tracks are", self.tracks)

    # define get score method to return the score
    def get_score(self):
        print(self.name, "score is", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
