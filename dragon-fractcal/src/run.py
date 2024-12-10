from .generator import Generator
from .parserfractal import ParserFractal
from .turtlefractal import TurtleFractal
from .csvgenerator import CSVGenerator

DEGREE_ROTATION = 90
NUM_ITERATIONS = 20
LENGTH = 2

def run():
    generator = Generator()
    parser = ParserFractal()
    csv = CSVGenerator()
    
    # for i in range(10):
    #     print(f"iteration {i}: \n{generator.generate(i)}\n\n")

    sequences = [generator.generate(i+1) for i in range(NUM_ITERATIONS)]
    #print(f"sequence: {sequences}")

    calculated = [parser.parse(sequence, 90) for sequence in sequences]
    #print(f"calculated: {calculated}")

    turtle = TurtleFractal(show_updates=False, speed=0, length=LENGTH)
    turtle.draw_fractal(calculated)

    csv.output_data(calculated)