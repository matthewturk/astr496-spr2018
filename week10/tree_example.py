class Page:
    def __init__(self, text):
        self.text = text
        self.choices = []

    def add_choice(self, choice_name, page):
        self.choices.append((choice_name, page))

    def make_choice(self):
        print(self.text)
        if len(self.choices) == 0:
            print("You have died.")
            return
        else:
            for i, c in enumerate(self.choices):
                print("{}: {}".format(i, c[0]))
            answer = int(input("Which do you want?"))
            self.choices[answer][1].make_choice()

p1 = Page("You find yourself in a classroom.")
p2 = Page("You're outside in the hallway.")
p3 = Page("The professor calls on you.")
p4 = Page("It's raining and your feet are cold.")
p5 = Page("You answer correctly.")
p6 = Page("Wrong answer!")

p1.add_choice("Leave?", p2)
p1.add_choice("Stay inside?", p3)

p2.add_choice("Go in the classroom?", p1)
p2.add_choice("Go outside?", p4)

p3.add_choice("Guess?", p5)
p3.add_choice("Guess!", p6)
