import pygame
import json
from copy import deepcopy

class Menu:
    def __init__(self, screen):
        font = pygame.font.Font(None, 80)
        self.text_start = font.render("Start Game", True, "white")
        self.text_table_record = font.render("Records", True, "white")
        self.text_quit = font.render("Quit", True, "white")
        self.start_width, self.start_height = self.text_start.get_size()
        self.table_record_width, self.table_record_height = self.text_table_record.get_size()
        self.quit_width, self.quit_height = self.text_quit.get_size()
        self.screen = screen
        # setting coordinates
        self.start_x = (1520 / 2) - (self.start_width / 2)
        self.start_y = (720 / 2) - (self.start_height / 2) - 100
        self.table_record_x = (1520 / 2) - (self.table_record_width / 2)
        self.table_record_y = (720 / 2) - (self.table_record_height / 2)
        self.quit_x = (1520 / 2) - (self.quit_width / 2)
        self.quit_y = (720 / 2) - (self.quit_height / 2) + 100

        self.start_button = pygame.Rect(self.start_x, self.start_y, self.start_width, self.start_height)
        self.record_button = pygame.Rect(self.table_record_x, self.table_record_y, self.table_record_width, self.table_record_height)
        self.quit_button = pygame.Rect(self.quit_x, self.quit_y, self.quit_width, self.quit_height)


    def run(self):
        self.screen.blit(self.text_start, (self.start_x, self.start_y))
        self.screen.blit(self.text_table_record, (self.table_record_x, self.table_record_y))
        self.screen.blit(self.text_quit, (self.quit_x, self.quit_y))
        pygame.draw.rect(self.screen, "white", self.start_button, 2)
        pygame.draw.rect(self.screen, "white", self.record_button, 2)
        pygame.draw.rect(self.screen, "white", self.quit_button, 2)

class Records:
    def __init__(self, screen):
        font = pygame.font.Font(None, 80)
        self.screen = screen
        with open("records.json", "r") as records:
            self.record_table_data = json.load(records)
        self.text_menu = font.render("Menu", True, "white")
        self.menu_width, self.menu_height = self.text_menu.get_size()
        self.menu_x = 670
        self.menu_y = 500
        self.menu_button = pygame.Rect(self.menu_x, self.menu_y, self.menu_width, self.menu_height)


    def print_top_10_positions(self):
        font = pygame.font.Font(None, 48)  # Change the font and size to your liking
        y = 50  # Starting y-coordinate for the first position
        for i, position in enumerate(sorted(self.record_table_data, key=lambda x: x["score"], reverse=True)[:10]):
            text = f"{i + 1}. {position['name']}: {position['score']}"
            rendered_text = font.render(text, True, (255, 255, 255))  # Change the color to your liking
            self.screen.blit(rendered_text, (600, y))
            y += 40  # Increase the y-coordinate for the next position

        self.screen.blit(self.text_menu, (self.menu_x, self.menu_y))
        pygame.draw.rect(self.screen, "white", self.menu_button, 2)


    def add_score(self, score):
        copy_of_record_table = deepcopy(self.record_table_data)
        self.record_table_data.append({"name": f"Player {len(copy_of_record_table)+1}", "score": score})
        with open("records.json", "w") as write_file:
            json.dump(self.record_table_data, write_file)
