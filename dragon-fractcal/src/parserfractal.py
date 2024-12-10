class ParserFractal:

    def __init__(self):
        self.heading = 0

    def parse(self, sequence, angle):
        # parse the sequence by converting the sequence of Ls and Rs to a sequence of heading angles for the turtle head
        calculated = []

        for move in sequence:
            if move == "L":
                self.heading = -angle
            elif move == "R":
                self.heading = angle

            calculated.append(self.heading)

        return calculated