import pygame
import datetime 
import os
import json


class Leaderboard(pygame.font.Font):
    FILE_NAME = "score.json"
    score = None
    font = None
    new_score = None
    new_name = None
    scores = None

    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("monospace", 15)



    def sort_scores(self, json):
        # A somewhat dirty method for sorting the JSON entries... It works though!
        scores_dict = dict() # Create a dictionary object.
        sorted_list = list() # Create a list object.

        for obj in json:
            scores_dict[obj["score"]]=obj # Add every score to a dictionary with its score as key. Key collisions ensue...

        for key in sorted(scores_dict.keys(), reverse=True): # Read the sorted dictionary in reverse order (highest score first)...
            sorted_list.append(scores_dict[key]) # ...and add it to a list.

        return sorted_list # Tada! Returns a sorted list.

    # Reads the previous scores from the highscores.json-file
    # and adds it to a list (a python list object, that is).
    def load_previous_scores(self):
        with open(self.FILE_NAME) as highscore_file:
           self.scores = json.load(highscore_file)
           self.scores = self.scores

    # Just like every other draw method, this
    # paints the list. But this paints every score
    # in the list with a 20px padding to the next one.
    def draw(self, screen, sorted_scores):
        padding_y = 0
        max_scores = 8 # We *could* paint every score, but it's not any good if you can't see them (because we run out of the screen).
        nbr_scores = 1
        for name, score in sorted_scores:
            if nbr_scores <= max_scores:
                screen.blit(self.font.render(str(nbr_scores)+". " +str(name) +": " + str(score), 1, (0,0,0)), (220,200 + padding_y))
                padding_y += 20
                nbr_scores += 1