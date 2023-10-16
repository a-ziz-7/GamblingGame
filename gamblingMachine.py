import pygame
import random
from sys import exit

balance = 100
price = 6 # 6.75

def generate():
    chances = {0: 20, 1: 20, 2: 20, 3: 15, 4: 10, 5: 10, 6: 5}
    # chances = {0: 20, 1: 20, 2: 20, 3: 15, 4: 10, 5: 10, 6: 5}
    array_of_chances = []
    for key in chances:
        array_of_chances.extend([key]*chances[key])
    return array_of_chances


array_of_chances = generate()


def get_lines(num):
    ans = []
    global balance
    global price
    if isinstance(num, str):
        temp = num.split(" ")
        for i in range(len(temp)):
            try:
                v = int(temp[i])
            except:
                continue
            if ((v-1) not in ans and 0 < v < 4 and balance >= price):
                ans.append(v-1)
                balance -= price
        return ans
    else:
        return ans


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Gambling Game")
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# test_surface = pygame.Surface((100,200))
# test_surface.fill((250,100,100))

background_surface = pygame.image.load("gg.jpg")


font = pygame.font.SysFont('Verdana', 43)
font_B = pygame.font.SysFont('Verdana', 43)
balance_surface = font_B.render(f"Balance: {balance}$", True, (0, 255, 100))
surface1 = font.render("| 0 | 0 | 0 |", True, (68, 188, 216))
surface2 = font.render("-------------", True, (0, 255, 100))
surface3 = font.render("| 0 | 0 | 0 |", True, (255, 250, 10))
surface4 = font.render("-------------", True, (0, 255, 100))
surface5 = font.render("| 0 | 0 | 0 |", True, (246, 17, 16))
big2 = big4 = "-"*13

button_surface = font.render("Play", True, (110, 255, 100))
# button = pygame.Rect(300, 300, 300, 300)
while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        if event.type == pygame.MOUSEBUTTONDOWN and (balance >= price or len(lines) > 0):
            lines = get_lines("1 2 3")
            balance_surface = font_B.render(
                f"Balance: {balance}$", True, (0, 255, 100))
            out = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            amount_won_counter = 0
            big1 = big3 = big5 = "| "
            for i in range(3):
                for j in range(3):
                    out[i][j] = random.choice(array_of_chances)
                    if i == 0:
                        big1 += (str(out[i][j]) + " | ")
                    elif i == 1:
                        big3 += (str(out[i][j]) + " | ")
                    else:
                        big5 += (str(out[i][j]) + " | ")
                if i == 0:
                    big1 += "  " + str(sum(out[i])) + \
                        ("$ won" if i in lines else "$")
                elif i == 1:
                    big3 += "  " + str(sum(out[i])) + \
                        ("$ won" if i in lines else "$")
                else:
                    big5 += "  " + str(sum(out[i])) + \
                        ("$ won" if i in lines else "$")
                balance += sum(out[i]) if i in lines else 0
            balance_surface = font_B.render(
                f"Balance: {round(balance,1)}$", True, (0, 255, 100))
            surface1 = font.render(big1, True, (68, 188, 216))
            surface2 = font.render(big2, True, (0, 255, 100))
            surface3 = font.render(big3, True, (255, 250, 10))
            surface4 = font.render(big4, True, (0, 255, 100))
            surface5 = font.render(big5, True, (246, 17, 16))
            

    # pygame.draw.rect(screen, (0, 255, 100), button)
    screen.blit(background_surface, (0, 0))
    screen.blit(balance_surface, (20, 20))
    screen.blit(surface1, (20, 150-40))
    screen.blit(surface2, (20, 200-40))
    screen.blit(surface3, (20, 250-40))
    screen.blit(surface4, (20, 300-40))
    screen.blit(surface5, (20, 350-40))
    screen.blit(button_surface, (400, 20))

    pygame.display.update()
    clock.tick(90)
    # time.sleep(1)
