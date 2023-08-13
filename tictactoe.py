import pygame
import sys   
pygame.init()
    
#constants
WIDTH,HEIGHT=300,300
cell_size=WIDTH//3
RED=(255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
LINE_COLOR=(50,50,50)
BOARD_SIZE=3
board=[[' ' for _ in range(3)] for _ in range(3)]
screen=pygame.display.set_mode((WIDTH,HEIGHT))
turn='X'
gameover=False
    
#create game window

pygame.display.set_caption("Tic-Tac_Toe")
    
def initialize_board():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board


   
def draw_grid():
        for i in range(1,3):
            pygame.draw.line(screen,LINE_COLOR,(i*cell_size,0),(i*cell_size,HEIGHT),5)
            pygame.draw.line(screen,LINE_COLOR,(0,cell_size*i),(WIDTH,i*cell_size),5)          
            
def draw_symbols():
        for row in range(3):
            for col in range(3):
                if board[row][col]=='X':
                    x_pos=col*cell_size +cell_size//2
                    y_pos=row*cell_size+ cell_size//2
                    pygame.draw.line(screen, BLACK, (x_pos - 30, y_pos - 30), (x_pos + 30, y_pos + 30), 3)
                    pygame.draw.line(screen, BLACK, (x_pos - 30, y_pos + 30), (x_pos + 30, y_pos - 30), 3)
            
                elif board[row][col]=='O':
                    x_pos=col*cell_size+cell_size//2
                    y_pos=row*cell_size+cell_size//2
                    pygame.draw.circle(screen,BLACK,(x_pos,y_pos),30,5)
   

def check_game_status():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
        return True
    return False

def is_board_full():
    return all([cell != " " for row in board for cell in row ])


def reset_game():
    global board
    board=[[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    return board
            
def show_play_again_message():
    font=pygame.font.Font(None,30)
    text=font.render("play again? (Y/N)",True,BLACK)
    screen.blit(text,((WIDTH-text.get_width())//2,HEIGHT-50))
                    
            
            
def show_game_over_message(message):
    font=pygame.font.Font(None,36)
    text=font.render(message,True,BLACK)
    screen.blit(text,((WIDTH-text.get_width())//2,(HEIGHT+30)//2))
    
def Play_tic_tac_toe():
    running=True
    current_player='X'
    gameover=False    
    
    
    
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN and not gameover:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                row=mouse_y//(HEIGHT//3)
                col=mouse_x//(WIDTH//3)
                
                
                if board[row][col]==' ':
                    board[row][col]=current_player
                    if check_game_status():
                        gameover=True
                    current_player='O' if current_player=='X' else 'X'
            
            keys=pygame.key.get_pressed()                
            if keys[pygame.K_y]:
                 initialize_board()
                 
                 current_player='X'
                 gameover=False
            if keys[pygame.K_n]:
                 return True
                           
                       
                   
                    
                    
        screen.fill(WHITE)
        draw_grid()
        draw_symbols() 
        
        if gameover:
            if is_board_full():
                show_game_over_message('its a draw!')
            elif current_player=='X':
                show_game_over_message(f"player O wins!")
            elif current_player=='O':
                show_game_over_message(f"player X wins!")
            play_again=show_play_again_message()
            
            if play_again:
                reset_game()
                current_player='X'
                gameover=False
          
        pygame.display.flip()
        

if __name__=='__main__':
    Play_tic_tac_toe()
    
    
pygame.quit()
sys.exit()
                        