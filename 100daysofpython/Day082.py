import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (242, 85, 96)
X_COLOR = (28, 170, 156)
BG_COLOR = (28, 170, 156)
CIRCLE_RADIUS = 60
X_WIDTH = 25
GRID_SIZE = 3
LINE_LENGTH = WIDTH // GRID_SIZE

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')

# Create the game grid
grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Current player
current_player = 'X'

# Function to draw the grid
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * LINE_LENGTH), (WIDTH, row * LINE_LENGTH), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * LINE_LENGTH, 0), (row * LINE_LENGTH, HEIGHT), LINE_WIDTH)

# Function to draw X or O on the grid
def draw_mark(row, col, player):
    center_x = col * LINE_LENGTH + LINE_LENGTH // 2
    center_y = row * LINE_LENGTH + LINE_LENGTH // 2
    if player == 'X':
        pygame.draw.line(screen, X_COLOR, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50), X_WIDTH)
        pygame.draw.line(screen, X_COLOR, (center_x - 50, center_y + 50), (center_x + 50, center_y - 50), X_WIDTH)
    elif player == 'O':
        pygame.draw.circle(screen, CIRCLE_COLOR, (center_x, center_y), CIRCLE_RADIUS, LINE_WIDTH)

# Function to check if the current player has won
def check_winner(player):
    # Check rows and columns
    for i in range(GRID_SIZE):
        if all(grid[i][j] == player for j in range(GRID_SIZE)) or all(grid[j][i] == player for j in range(GRID_SIZE)):
            return True
    # Check diagonals
    if all(grid[i][i] == player for i in range(GRID_SIZE)) or all(grid[i][GRID_SIZE - 1 - i] == player for i in range(GRID_SIZE)):
        return True
    return False

# Function to check if the board is full (for a draw)
def is_full():
    return all(grid[row][col] != '' for row in range(GRID_SIZE) for col in range(GRID_SIZE))

# Main game loop
def game_loop():
    global current_player
    running = True

    while running:
        screen.fill(BG_COLOR)
        draw_grid()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not is_full():
                mouse_x, mouse_y = event.pos
                clicked_row = mouse_y // LINE_LENGTH
                clicked_col = mouse_x // LINE_LENGTH

                # Make a move if the cell is empty
                if grid[clicked_row][clicked_col] == '':
                    grid[clicked_row][clicked_col] = current_player
                    draw_mark(clicked_row, clicked_col, current_player)

                    # Check for winner
                    if check_winner(current_player):
                        print(f"Player {current_player} wins!")
                        pygame.time.wait(1000)  # Wait for 1 second before restarting
                        return  # Restart the game

                    # Check for draw
                    if is_full():
                        print("It's a draw!")
                        pygame.time.wait(1000)  # Wait for 1 second before restarting
                        return  # Restart the game

                    # Switch player
                    current_player = 'O' if current_player == 'X' else 'X'

        pygame.display.update()

# Run the game loop
if __name__ == "__main__":
    game_loop()
    pygame.quit()
    sys.exit()
