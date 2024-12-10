from tqdm import tqdm
import turtle

class TurtleFractal:
    def __init__(self, length=10, speed=10, show_updates=False):
        # Initialize the window
        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.title("Fractal")
        self.wn.setup(width=0.7, height=0.7)
        self.wn.screensize(canvwidth=3000, canvheight=3000)

        # Initialize the turtle
        self.turt = turtle.Turtle()
        self.turt.color("white")
        self.turt.speed(speed)
        self.turt.penup()
        self.turt.goto(0, 0)
        self.turt.pendown()

        # Parameters
        self.length = length
        self.show_updates = show_updates

        # Turn off auto updates for smoother rendering
        if not self.show_updates:
            self.wn.tracer(0)

    def draw_fractal(self, sequence):
        # Update title to show progress
        self.wn.title(f"Fractal: {len(sequence)} moves")

        moves = sequence[-1]
        heading = 0
        
        for move in tqdm(moves, desc="Moves Completed"):       
            heading = heading + move
            # Set heading and move the turtle
            self.turt.setheading(heading)
            self.turt.forward(self.length)          
            # Update the screen after drawing
            if move % 100:
                self.wn.update()

        # Exit gracefully when done
        self.wn.mainloop()
        turtle.done()



# Example Usage
# if __name__ == "__main__":
#     # Example sequence for drawing the fractal
#     sequence = [0, 90, 180, 270] * 500  # Repeating moves for demonstration
#     fractal = TurtleFractal(length=5, speed=0, show_updates=False)
#     fractal.draw_fractal(sequence)
