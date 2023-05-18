import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.model import Model
from app.view.view import View


class Controller:
    def __init__(self) -> None:
        self.dialog = None
        self.model = Model()
        self.view = View(controller=self)

    def get_view(self):
        return self.view.root

    def dispatch(self, action):
        print(action.type, action.content)
        if action.type == 'REMOVE':
            print(self.view.table.children[0].get_row_checks())
            self.model.delete(
                list(map(lambda el: el, self.view.table.children[0].get_row_checks())))
            self.view.update()
        if action.type == 'FILTER':
            form = self.view.dialog.content_cls.ids

            filter_line = {
                'tour_name': form.tour_name.text,
                'date': form.date.text,
                'sport': form.sport.text,
                'name': form.name.text,
                'min_reward': form.min_reward.text,
                'max_reward': form.max_reward.text,
                'min_winner_reward': form.min_winner_reward.text,
                'max_winner_reward': form.max_winner_reward.text,
            }

            validated = True

            for key in filter_line.keys():
                if filter_line[key] == '':
                    filter_line[key] = None

            if filter_line['min_reward'] is not None \
                    and re.match(r'^\d+\.*\d*$', filter_line['min_reward']):
                filter_line['min_reward'] = float(filter_line['min_reward'])
            elif filter_line['min_reward'] is not None:
                form.min_reward.error = True
                validated = False

            if filter_line['max_reward'] is not None \
                    and re.match(r'^\d+\.*\d*$', filter_line['max_reward']):
                filter_line['max_reward'] = float(filter_line['max_reward'])
            elif filter_line['max_reward'] is not None:
                form.max_reward.error = True
                validated = False

            if filter_line['min_winner_reward'] is not None \
                    and re.match(r'^\d+\.*\d*$', filter_line['min_winner_reward']):
                filter_line['min_winner_reward'] = float(filter_line['min_winner_reward'])
            elif filter_line['min_winner_reward'] is not None:
                form.min_winner_reward.error = True
                validated = False

            if filter_line['max_winner_reward'] is not None \
                    and re.match(r'^\d+\.*\d*$', filter_line['max_winner_reward']):
                filter_line['max_winner_reward'] = float(filter_line['max_winner_reward'])
            elif filter_line['max_winner_reward'] is not None:
                form.max_winner_reward.error = True
                validated = False

            if validated \
                    and filter_line['min_reward'] is not None \
                    and filter_line['max_reward'] is not None\
                    and filter_line['min_reward'] > filter_line['max_reward']:
                form.reward.error = True
                validated = False

            if validated \
                    and filter_line['min_winner_reward'] is not None \
                    and filter_line['max_winner_reward'] is not None\
                    and filter_line['min_winner_reward'] > filter_line['max_winner_reward']:
                form.reward.error = True
                validated = False

            if validated:
                self.model.filter(filter_line)
                self.view.close_dialog()
                self.view.update()

        if action.type == 'OPEN_FILTER_DIALOG':
            self.view.open_filter_dialog()
        if action.type == 'DISABLE_FILTER':
            self.model.disable_filter()
            self.view.close_dialog()
            self.view.update()

        if action.type == 'OPEN_CHOOSE_FILE_DIALOG':
            self.view.open_choose_file_dialog()

        if action.type == 'FILE_CHOOSE':
            self.model.load_df(action.content)
            self.view.close_choose_file_dialog()
            self.view.update()

        if action.type == 'CLOSE_CHOOSE_FILE_DIALOG':
            self.view.close_choose_file_dialog()

        if action.type == 'CLOSE_DIALOG':
            self.view.close_dialog()

        if action.type == 'OPEN_ADDING_DIALOG':
            self.view.open_adding_dialog()
        if action.type == 'ADD':
            form = self.view.dialog.content_cls.ids
            print(form)
            self.view.close_dialog()
            self.view.update()

        if action.type == 'ADD':
            form = self.view.dialog.content_cls.ids

            new_line = {
                'tour_name': form.tour_name.text,
                'date': form.date.text,
                'sport': form.sport.text,
                'name': form.name.text,
                'reward': form.reward.text
            }

            validated: bool = True

            if not new_line['tour_name']:
                form.tour_name.error = True
                validated = False

            if not new_line['date']:
                form.date.error = True
                validated = False

            if not new_line['sport']:
                form.sport.error = True
                validated = False

            if not new_line['name']:
                form.name.error = True
                validated = False

            if not new_line['reward'] or not re.match(r'^\d+\.*\d*$', new_line['reward']):
                form.reward.error = True
                validated = False
            else:
                new_line['reward'] = float(new_line['reward'])
                new_line['winner_reward'] = new_line['reward'] * 0.6

            if validated:
                self.model.add_line(new_line)
                self.view.close_dialog()
                self.view.update()

    def get_competitions(self):
        return self.model.get_list()
