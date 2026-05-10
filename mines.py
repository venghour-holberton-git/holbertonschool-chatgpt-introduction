#!/usr/bin/python3
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    """
    Function description:
        Creates and manages a Minesweeper game.

    Parameters:
        width (int): Width of the board.
        height (int): Height of the board.
        mines (int): Number of mines.

    Returns:
        None
    """

    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_mines = mines

        # Generate mine positions
        self.mines = set(random.sample(range(width * height), mines))

        # Track revealed cells
        self.revealed = [
            [False for _ in range(width)]
            for _ in range(height)
        ]

    def print_board(self, reveal=False):
        """
        Function description:
            Prints the game board.

        Parameters:
            reveal (bool): Reveal all mines if True.

        Returns:
            None
        """

        clear_screen()

        print("   " + " ".join(str(i) for i in range(self.width)))

        for y in range(self.height):
            print(f"{y:2}", end=" ")

            for x in range(self.width):

                if reveal or self.revealed[y][x]:

                    if (y * self.width + x) in self.mines:
                        print("*", end=" ")

                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else " ", end=" ")

                else:
                    print(".", end=" ")

            print()

    def count_mines_nearby(self, x, y):
        """
        Function description:
            Counts nearby mines around a cell.

        Parameters:
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            int: Number of nearby mines.
        """

        count = 0

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:

                # Skip current cell
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:

                    if (ny * self.width + nx) in self.mines:
                        count += 1

        return count

    def reveal(self, x, y):
        """
        Function description:
            Reveals a cell and nearby empty cells.

        Parameters:
            x (int): X coordinate.
            y (int): Y coordinate.

        Returns:
            bool: False if a mine is hit, True otherwise.
        """

        # Prevent invalid coordinates
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True

        # Skip already revealed cells
        if self.revealed[y][x]:
            return True

        # Mine hit
        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        # Reveal nearby cells automatically if no nearby mines
        if self.count_mines_nearby(x, y) == 0:

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:

                    if dx == 0 and dy == 0:
                        continue

                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)

        return True

    def check_win(self):
        """
        Function description:
            Checks if all non-mine cells are revealed.

        Parameters:
            None

        Returns:
            bool: True if the player wins, False otherwise.
        """

        revealed_cells = 0

        for y in range(self.height):
            for x in range(self.width):

                if self.revealed[y][x]:
                    revealed_cells += 1

        total_safe_cells = (
            self.width * self.height
        ) - self.total_mines

        return revealed_cells == total_safe_cells

    def play(self):
        """
        Function description:
            Runs the game loop.

        Parameters:
            None

        Returns:
            None
        """

        while True:

            self.print_board()

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # Check bounds
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds.")
                    input("Press Enter to continue...")
                    continue

                # Reveal selected cell
                if not self.reveal(x, y):

                    self.print_board(reveal=True)

                    print("Game Over! You hit a mine.")
                    break

                # Check win condition
                if self.check_win():

                    self.print_board(reveal=True)

                    print("Congratulations! You won!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
