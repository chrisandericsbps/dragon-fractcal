from tqdm import tqdm

class Generator:
    def __init__(self, first_move="R"):
        """
        Initialize the generator with a single starting move.
        """
        self.first_move = first_move
        self.cache = [[], [self.first_move]]  # Start with empty at index 0, and "R" at index 1
        self.iteration = 1  # Tracks the last generated iteration

    def generate(self, target_iter):
        # Input validation
        if not isinstance(target_iter, int) or target_iter < 1:
            raise ValueError("target_iter must be a positive integer.")

        with tqdm(total=target_iter, desc="Generating iterations") as t:
            t.update(self.iteration)  # Initialize progress bar

            # Dynamically generate the sequence until we reach the target iteration
            while self.iteration <= target_iter:
                last_iter_data = self.cache[self.iteration]  # Get the previous iteration

                # Next iteration: Duplicate the previous sequence
                next_iter_data = last_iter_data + last_iter_data

                if self.iteration>=2:
                    next_iter_data[int((len(last_iter_data) / 2))] = 'L' #length of previous


                # Update cache and progress
                self.cache.append(next_iter_data)
                self.iteration += 1
                t.update(1)

        return self.cache[target_iter]  # Return the generated sequence for the target iteration