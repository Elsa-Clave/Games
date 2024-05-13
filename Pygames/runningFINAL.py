import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800, 400))

#Ventana Original

programIcon=pygame.image.load("skylines/shield.png")
pygame.display.set_icon(programIcon)
pygame.display.set_caption("Viking")

#Añadir la superficie
#test_surface=pygame.Surface((100, 200))
#test_surface.fill("Red")
test_surface=pygame.image.load("skylines/basic.jpg").convert()

test_surface=pygame.transform.scale(test_surface, (800, 300))

ground_surface=pygame.image.load("skylines/ground.png").convert()
ground_surface=pygame.transform.scale(ground_surface, (800, 100))

#TEXT

test_font=pygame.font.Font(None, 50)
text_surface=test_font.render("Vikings Game", False, "Green")
go_font=pygame.font.Font(None, 30)
text_gameover=go_font.render("GAME OVER GREAT WARRIOR!", False, "Black")
text_continue=go_font.render("Press 'Space' to continue or 'Q' to quit", False, "Black")


# Toni3, the snail
snail_surface=pygame.image.load("skylines/snail1.png").convert_alpha()
snail_x_pos=800
snail_rect=snail_surface.get_rect(bottomright=(700, 310))
velocity=4

# Mingo el Vikingo
player_surf=pygame.image.load("skylines/static_viking.png").convert()
player_surf=pygame.transform.scale(player_surf, (80, 100))
player_rect=player_surf.get_rect(midbottom=(100, 320))

color=pygame.Color(255, 255, 255)
player_surf.set_colorkey(color)

viking_jumping=pygame.image.load("skylines/jumping_viking.png").convert()
viking_jumping=pygame.transform.scale(viking_jumping, (80, 100))
viking_jumping.set_colorkey(color)

viking_falling=pygame.image.load("skylines/falling_viking.png").convert()
viking_falling=pygame.transform.scale(viking_falling, (80, 100))
viking_falling.set_colorkey(color)
#Controlar el Frame Rate
clock=pygame.time.Clock()
game_active=True
count=0
gravity=0
position=0


while True: 
    snailcount=go_font.render(f"Snail Count: {count}", False, "Black")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_active==True:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom==320:
                    gravity=-12
        else: 
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_active=True
                    snail_rect.left=800
                elif event.key==pygame.K_q:
                    exit()
    if game_active:
        screen.blit(test_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        screen.blit(text_surface, (300,350))
        screen.blit(snailcount, (575, 50))
        #screen.blit(player_surf, (100, 210))

        #screen.blit(snail_surface, (snail_x_pos, 270))

        screen.blit(snail_surface, snail_rect)

        snail_rect.x-=velocity
        if snail_rect.right<=0:
            snail_rect.left=800
            count+=1
            if count%3==0:
                velocity+=1

        #screen.blit(player_surf, player_rect)
        player_rect.y+=gravity
        if player_rect.bottom>=320:
            player_rect.bottom=320
        if position==player_rect.y:
            screen.blit(player_surf, player_rect)
        elif position<player_rect.y:
            screen.blit(viking_falling, player_rect)
        else:
            screen.blit(viking_jumping, player_rect)

        
        print(player_rect.colliderect(snail_rect))
        gravity+=0.4

        position=player_rect.y

    if snail_rect.colliderect(player_rect):
        game_active=False
        count=0
        velocity=4
        screen.blit(text_gameover, (250, 200))
        screen.blit(text_continue, (210, 230))
  



    pygame.display.update()
    clock.tick(60)