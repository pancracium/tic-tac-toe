import pygame
pygame.init()

#Set up the game window
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Set up the game board
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

#Set up the players
players = ['X', 'O']
current_player = 0

#Set up the font
font = pygame.font.Font(None, 50)

#Set up the game loop
running = True
while running:
    #Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Get the position of the mouse click
            pos = pygame.mouse.get_pos()

            #Get the row and column of the square clicked
            row = pos[1] // 100
            col = pos[0] // 100

            #Make the move if the square is empty
            if board[row][col] == '':
                board[row][col] = players[current_player]

                #Switch to the next player
                current_player = (current_player + 1) % 2

    #Draw the game board
    screen.fill((255, 255, 255))
    for row in range(3):
        for col in range(3):
            #Draw the squares
            pygame.draw.rect(screen, (0, 0, 0), (col * 100, row * 100, 100, 100), 1)

            #Draw the X's and O's
            if board[row][col] != '':
                text = font.render(board[row][col], True, (0, 0, 0))
                text_rect = text.get_rect(center=(col * 100 + 50, row * 100 + 50))
                screen.blit(text, text_rect)

    #Update the display
    pygame.display.update()

#Quit Pygame
pygame.quit()