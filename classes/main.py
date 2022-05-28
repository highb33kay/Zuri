class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    @classmethod
    def change_name(self,name):
        self.name = name
        print("the student name is", self.name)

    @classmethod
    def change_age(self,age):
        self.age = int(age)
        print(self.name, "'s age is", self.age)

    @classmethod
    def add_track(self,tracks):
        self.tracks = tracks
        print(self.name, "tracks are", self.tracks)


    def get_score (self):       
        print("Student's score is", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
