import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 1080
screen_height = 1920
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flufftopia")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load fonts
title_font = pygame.font.Font(None, 150)
menu_font = pygame.font.Font(None, 100)

# Render text for title screen
title_text = title_font.render("FLUFFTOPIA", True, GREEN)
start_text = menu_font.render("Start Game", True, WHITE)
load_text = menu_font.render("Load Game", True, WHITE)
quit_text = menu_font.render("Quit", True, WHITE)

# Calculate positions for centering title screen text
title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4))
start_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2))
load_rect = load_text.get_rect(center=(screen_width // 2, screen_height // 2 + 120))
quit_rect = quit_text.get_rect(center=(screen_width // 2, screen_height // 2 + 240))

# Define button areas for title screen
start_button = pygame.Rect(start_rect.left, start_rect.top, start_rect.width, start_rect.height)
load_button = pygame.Rect(load_rect.left, load_rect.top, load_rect.width, load_rect.height)
quit_button = pygame.Rect(quit_rect.left, quit_rect.top, quit_rect.width, quit_rect.height)

# Define player races
races = ["Human", "Elf", "Dwarf", "Orc", "Troll", "Goblin", "Gnome", "Halfling", "Vampire", "Werewolf"]

# Player attributes
attributes = {"Strength": 10, "Intelligence": 10, "Willpower": 10, "Agility": 10, "Speed": 10, "Endurance": 10, "Personality": 10, "Luck": 10}

# Player creator elements
name_input_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 50, 300, 50)
race_rects = []
race_texts = []
for i, race in enumerate(races):
    text = menu_font.render(race, True, WHITE)
    rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 80 + i * 60))
    race_texts.append(text)
    race_rects.append(rect)

def draw_title_screen():
    screen.fill(BLACK)
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    screen.blit(load_text, load_rect)
    screen.blit(quit_text, quit_rect)
    pygame.display.flip()

def draw_player_creator(player_name, selected_race):
    screen.fill(BLACK)
    title = title_font.render("Create Your", True, GREEN)
    screen.blit(title, title.get_rect(center=(screen_width // 2, screen_height // 4)))
    title2 = title_font.render("Character", True, GREEN)
    screen.blit(title2, title.get_rect(center=(screen_width // 2, screen_height // 3)))
    name_label = menu_font.render("Name:", True, WHITE)
    screen.blit(name_label, (screen_width // 2 - 375, screen_height // 2 - 62))
    pygame.draw.rect(screen, WHITE, name_input_rect, 2)
    name_text = menu_font.render(player_name, True, WHITE)
    screen.blit(name_text, (name_input_rect.x + 10, name_input_rect.y + 5))
    race_label = menu_font.render("Select", True, WHITE)
    screen.blit(race_label, (screen_width // 2 - 375, screen_height // 2 + 20))
    race_label2 = menu_font.render("Race:", True, WHITE)
    screen.blit(race_label2, (screen_width // 2 - 375, screen_height // 2 + 80 ))
    for i, text in enumerate(race_texts):
        if i == selected_race:
            pygame.draw.rect(screen, GREEN, race_rects[i], 4)  # Highlight selected race
        screen.blit(text, race_rects[i])
    pygame.display.flip()

def main():
    running = True
    in_player_creator = False
    player_name = ""
    selected_race = 0
    
    while running:
        if in_player_creator:
            draw_player_creator(player_name, selected_race)
        else:
            draw_title_screen()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not in_player_creator:
                    if start_button.collidepoint(event.pos):
                        in_player_creator = True
                    elif load_button.collidepoint(event.pos):
                        print("Loading game...")
                        # Add code to load a game here
                    elif quit_button.collidepoint(event.pos):
                        print("Quitting game...")
                        running = False
                else:
                    for i, rect in enumerate(race_rects):
                        if rect.collidepoint(event.pos):
                            selected_race = i
            elif event.type == pygame.KEYDOWN and in_player_creator:
                if event.key == pygame.K_RETURN:
                    print(f"Character created: Name - {player_name}, Race - {races[selected_race]}")
                    # Add code to start the game with the created character
                    running = False  # End the loop for now
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif len(player_name) < 20:  # Limit name length
                    player_name += event.unicode

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
