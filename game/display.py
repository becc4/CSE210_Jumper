class display:
    
    def __init__(self):
        # Set up jumper man.
        self.body = []
        self.body.append("  ___  ")
        self.body.append(" /___\ ")
        self.body.append(" \   / ")
        self.body.append("  \ /  ")
        self.body.append("   0   ")
        self.body.append("  /|\  ")
        self.body.append("  / \  ")

        # Set up the floor under the guy, seperated
        # so that it doesn't mess up the counter.
        self.danger_floor = "^^^^^^^"


    def display_jumper(self):
        # Display the jumper.
        for i in len(self.body):
            print(self.body[i-1])
        print()
        print(self.danger_floor)

    def update_jumper(self):
        # Remove body parts.
        self.body.pop(0)