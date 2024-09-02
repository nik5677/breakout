import configparser
import sys

import pygame

from src.ball import Ball
from src.brick import Brick
from src.button import Button
from src.paddle import Paddle
from src.resources import Resources
from src.settings import Settings


def change_pause_state():
    """Changes pause state"""
    if settings.pause:
        settings.pause = False
    else:
        settings.pause = True


def quit_game():
    """Save options and exit the program"""
    settings.save_to_file("resources/config.ini")
    pygame.quit()
    sys.exit()


def put_logo():
    """Put the logo on a screen"""
    logo = resources.logo
    logo_rect = logo.get_rect(center=(400, 100))
    screen.blit(logo, logo_rect)


def options():
    """Show 'options' screen"""
    theme_counter = settings.theme_list.index(settings.theme)
    ball_speed_counter = settings.ball_speed_list.index(settings.ball_speed)
    sound_counter = settings.sound_state_list.index(settings.sound_state)

    while True:
        options_mouse_pos = pygame.mouse.get_pos()
        screen.blit(resources.background, (0, 0))
        put_logo()

        options_speed = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 225), text_input=f"Ball speed: {settings.ball_speed}", text_color=resources.text_color)
        options_sound = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 300), text_input=f"Sound: {settings.sound_state}", text_color=resources.text_color)
        options_theme = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 375), text_input=f"Theme: {settings.theme}", text_color=resources.text_color)
        options_back = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 525), text_input="Back", text_color=resources.text_color)

        for button in [options_speed, options_sound, options_theme, options_back]:
            button.hover(options_mouse_pos)
            button.place(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_speed.check_for_input(options_mouse_pos):
                    ball_speed_counter += 1
                    if ball_speed_counter >= len(settings.ball_speed_list):
                        ball_speed_counter = 0
                    settings.ball_speed = settings.ball_speed_list[ball_speed_counter]

                if options_sound.check_for_input(options_mouse_pos):
                    sound_counter += 1
                    if sound_counter >= len(settings.sound_state_list):
                        sound_counter = 0
                    settings.sound_state = settings.sound_state_list[sound_counter]

                if options_theme.check_for_input(options_mouse_pos):
                    theme_counter += 1
                    if theme_counter >= len(settings.theme_list):
                        theme_counter = 0
                    settings.theme = settings.theme_list[theme_counter]
                    resources.change_theme(settings.theme)

                if options_back.check_for_input(options_mouse_pos):
                    main_menu()

        pygame.display.update()


def how_to_play():
    """Show 'how to play' screen"""
    while True:
        htp_mouse_pos = pygame.mouse.get_pos()
        screen.blit(resources.background, (0, 0))
        put_logo()

        htp_text1 = resources.header_font.render("How to play", True, resources.text_color)
        htp_rect1 = htp_text1.get_rect(center=(400, 200))
        screen.blit(htp_text1, htp_rect1)

        htp_text2 = resources.button_font.render("destroy all blocks to win", True, resources.text_color)
        htp_rect2 = htp_text2.get_rect(center=(400, 270))
        screen.blit(htp_text2, htp_rect2)

        htp_text3 = resources.button_font.render("use mouse to move the paddle", True, resources.text_color)
        htp_rect3 = htp_text3.get_rect(center=(400, 325))
        screen.blit(htp_text3, htp_rect3)

        htp_text4 = resources.button_font.render("press ESC to pause the game", True, resources.text_color)
        htp_rect4 = htp_text4.get_rect(center=(400, 380))
        screen.blit(htp_text4, htp_rect4)

        htp_back = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 525), text_input="Back", text_color=resources.text_color)
        htp_back.hover(htp_mouse_pos)
        htp_back.place(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if htp_back.check_for_input(htp_mouse_pos):
                    main_menu()

        pygame.display.update()


def lose_screen():
    """Show 'you lose' screen"""
    if settings.sound_state == 'on':
        resources.lose_sound.play()

    while True:
        lose_mouse_pos = pygame.mouse.get_pos()
        screen.blit(resources.background, (0, 0))
        put_logo()

        lose_text = resources.header_font.render("You lost the game.", True, resources.text_color)
        lose_rect = lose_text.get_rect(center=(400, 200))
        screen.blit(lose_text, lose_rect)

        lose_playagain = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 300), text_input="Play again", text_color=resources.text_color)
        lose_playagain.hover(lose_mouse_pos)
        lose_playagain.place(screen)

        lose_menu = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 375), text_input="Menu", text_color=resources.text_color)
        lose_menu.hover(lose_mouse_pos)
        lose_menu.place(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lose_playagain.check_for_input(lose_mouse_pos):
                    game()
                if lose_menu.check_for_input(lose_mouse_pos):
                    main_menu()

        pygame.display.update()


def win_screen():
    """Show 'you win' screen"""
    if settings.sound_state == 'on':
        resources.win_sound.play()

    while True:
        win_mouse_pos = pygame.mouse.get_pos()
        screen.blit(resources.background, (0, 0))
        put_logo()

        win_text = resources.header_font.render("Congratulations! You win.", True, resources.text_color)
        win_rect = win_text.get_rect(center=(400, 200))
        screen.blit(win_text, win_rect)

        win_playagain = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 300), text_input="Play again", text_color=resources.text_color)
        win_playagain.hover(win_mouse_pos)
        win_playagain.place(screen)

        win_menu = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 375), text_input="Menu", text_color=resources.text_color)
        win_menu.hover(win_mouse_pos)
        win_menu.place(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if win_playagain.check_for_input(win_mouse_pos):
                    game()
                if win_menu.check_for_input(win_mouse_pos):
                    main_menu()

        pygame.display.update()


def pause_screen():
    """Show 'pause' screen"""
    while True:
        pause_mouse_pos = pygame.mouse.get_pos()
        screen.blit(resources.background, (0, 0))
        put_logo()

        pause_text = resources.header_font.render("You paused the game.", True, resources.text_color)
        pause_rect = pause_text.get_rect(center=(400, 200))
        screen.blit(pause_text, pause_rect)

        pause_resume = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 300), text_input="Resume", text_color=resources.text_color)
        pause_resume.hover(pause_mouse_pos)
        pause_resume.place(screen)

        pause_menu = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 375), text_input="Menu", text_color=resources.text_color)
        pause_menu.hover(pause_mouse_pos)
        pause_menu.place(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_resume.check_for_input(pause_mouse_pos):
                    change_pause_state()
                if pause_menu.check_for_input(pause_mouse_pos):
                    settings.pause = False
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    change_pause_state()

        pygame.display.update()

        return pause_resume.rect, pause_menu.rect


def game():
    """Start the game"""
    score = 0
    lives = 3
    clock = pygame.time.Clock()  # the clock will be used to control how fast the screen updates
    all_sprites_list = pygame.sprite.Group()

    paddle = Paddle(image=resources.paddle)
    all_sprites_list.add(paddle)

    ball = Ball(image=resources.ball, speed=settings.ball_speed)
    all_sprites_list.add(ball)

    # Create the bricks
    all_bricks = pygame.sprite.Group()
    for brick_color in resources.brick_color_list:
        for i in range(10):
            brick = Brick(resources.brick_list[brick_color])
            brick.rect.x = i * 80
            brick.rect.y = 301 - resources.brick_color_list.index(brick_color) * 22
            all_sprites_list.add(brick)
            all_bricks.add(brick)

    while True:
        if settings.pause:  # If pause = true, pause the game
            pause_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:  # If user clicks the mouse, the ball starts
                ball.start()
            if event.type == pygame.KEYDOWN:  # If user presses the esc button, the pause changes its state
                if event.key == pygame.K_ESCAPE:
                    change_pause_state()

        if not settings.pause:
            # Moving the paddle when the user uses the mouse
            mx, my = pygame.mouse.get_pos()
            paddle.move(mx - 50)

            all_sprites_list.update()

            # Check if the ball is bouncing against any of the 4 walls:
            if ball.rect.x <= 0:
                ball.rect.x = 0  # to prevent from falling behind the wall
                ball.bounce_x()
            if ball.rect.x >= 785:
                ball.rect.x = 785
                ball.bounce_x()
            if ball.rect.y <= 47:
                ball.rect.y = 47
                ball.bounce_y()
            if ball.rect.y >= 585:
                ball.rect.y = 585
                ball.bounce_y()
                lives -= 1
                ball.reset()

                if lives == 0:
                    pygame.time.wait(500)
                    lose_screen()

            # Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(ball, paddle):
                ball.bounce(paddle)

            # Check if there is the ball that collides with any of the bricks
            brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
            for brick in brick_collision_list:
                if settings.sound_state == 'on':
                    resources.bounce_sound.play()
                ball.bounce(brick)
                score += 1
                brick.kill()

                if len(all_bricks) == 0:
                    pygame.time.wait(500)
                    win_screen()

            screen.blit(resources.background, (0, 0))
            pygame.draw.line(screen, resources.text_color, [0, 45], [800, 45], 1)

            score_text = resources.score_font.render("Score: " + str(score), 1, resources.text_color)
            screen.blit(score_text, (20, 5))
            lives_text = resources.score_font.render("Lives: " + str(lives), 1, resources.text_color)
            lives_rect = lives_text.get_rect()
            screen.blit(lives_text, (780 - lives_rect.width, 5))

            all_sprites_list.draw(screen)
            pygame.display.flip()
            clock.tick(60)


def main_menu():
    """Show main menu"""
    while True:
        main_menu_mouse_pos = pygame.mouse.get_pos()
        screen.blit(resources.background, (0, 0))
        put_logo()

        play_button = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 225), text_input="Play", text_color=resources.text_color)
        htp_button = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 300), text_input="How to play", text_color=resources.text_color)
        options_button = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 375), text_input="Options", text_color=resources.text_color)
        quit_button = Button(image_normal=resources.normal_button, image_hover=resources.hover_button, font=resources.button_font, position=(400, 525), text_input="Quit", text_color=resources.text_color)

        for button in [play_button, htp_button, options_button, quit_button]:
            button.hover(main_menu_mouse_pos)
            button.place(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(main_menu_mouse_pos):
                    game()
                if htp_button.check_for_input(main_menu_mouse_pos):
                    how_to_play()
                if options_button.check_for_input(main_menu_mouse_pos):
                    options()
                if quit_button.check_for_input(main_menu_mouse_pos):
                    quit_game()

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Breakout")

    settings = Settings()
    try:  # try to load options from file (if exist)
        settings.load_from_file("resources/config.ini")
    except configparser.NoSectionError:
        pass
    resources = Resources(settings.theme)

    main_menu()
