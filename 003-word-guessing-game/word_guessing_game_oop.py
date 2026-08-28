import random
import string


class WordGuessingGame:
    """A simple command-line word guessing game."""

    WORDS = [
        "python",
        "variable",
        "function",
        "iterator",
        "notebook",
        "pipeline",
        "dataset",
        "computer",
        "research",
        "analytics",
    ]

    def __init__(self, max_lives=6):
        # Initialize the state of a new game.
        self.secret_word = random.choice(self.WORDS)
        self.blanks = ["_"] * len(self.secret_word)
        self.lives = max_lives
        self.used_letters = set()

    def prompt_for_letter(self):
        """Ask the user for a valid, unused letter."""
        while True:
            guess = input("Guess a letter: ").strip().lower()

            # Validate that the input contains exactly one letter.
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("→ Please enter a single A-Z letter.")
                continue

            # Prevent the user from guessing the same letter twice.
            if guess in self.used_letters:
                print("→ You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter):
        """Reveal the guessed letter if it exists in the word."""
        found = False

        for index, character in enumerate(self.secret_word):
            if character == letter:
                self.blanks[index] = letter
                found = True

        return found

    def is_word_complete(self):
        """Return True when all letters have been revealed."""
        return "_" not in self.blanks

    def display_word(self):
        """Display the current state of the hidden word."""
        print(" ".join(self.blanks))

    def play(self):
        """Run the main game loop."""
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        self.display_word()

        while self.lives > 0:

            # Get a new letter and remember it.
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Check whether the guessed letter exists in the word.
            if self.reveal_letters(guess):
                print("\nWell done! Nice job. You found a letter.")
                self.display_word()

                # Check whether the entire word has been guessed.
                if self.is_word_complete():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    return

            else:
                # A wrong guess costs one life.
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                self.display_word()

        # The loop ends when the player has no lives remaining.
        print("\nOut of lives!")
        print(f"The word was: {self.secret_word}")
        print("GAME OVER")


def main():
    """Create a game and start playing."""
    game = WordGuessingGame()
    game.play()


if __name__ == "__main__":
    main()