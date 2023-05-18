import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.generate_data import generate_df


class Model:
    def __init__(self) -> None:
        self.file_path = None
        self.df = None
        self.active_df = None

    def load_df(self, path):
        self.file_path = path
        try:
            self.df = pd.read_csv(path)

        except (FileNotFoundError, pd.errors.EmptyDataError):
            self.df = generate_df()

        self.df.to_csv(path, index=False)
        self.active_df = self.df

    def get_list(self):
        try:
            return self.active_df.values.tolist()
        except AttributeError:
            return []

    def add_line(self, line):
        print(line)
        self.df.loc[len(self.df.index)] = line
        self.df.to_csv(self.file_path, index=False)

        self.active_df = self.df

    def delete(self, competitions):

        if not len(competitions):
            return
        for line in competitions:
            self.df = self.df[(self.df['tour_name'] != line[0]) |
                              (self.df['date'] != line[1]) |
                              (self.df['sport'] != line[2]) |
                              (self.df['name'] != line[3]) |
                              (self.df['reward'] != float(line[4])) |
                              (self.df['winner_reward'] != float(line[5]))]

            self.active_df = self.active_df[(self.active_df['tour_name'] != line[0]) |
                              (self.active_df['date'] != line[1]) |
                              (self.active_df['sport'] != line[2]) |
                              (self.active_df['name'] != line[3]) |
                              (self.active_df['reward'] != float(line[4])) |
                              (self.active_df['winner_reward'] != float(line[5]))]

        self.df.to_csv(self.file_path, index=False)

    def filter(self, filter_options):
        self.active_df = self.df
        if filter_options['tour_name'] is not None:
            re_str = f'.*{filter_options["tour_name"]}.*'
            self.active_df = self.active_df[self.active_df.tour_name.str.match(re_str)]

        if filter_options['date'] is not None:
            self.active_df = self.active_df[self.active_df.date == filter_options['date']]

        if filter_options['sport'] is not None:
            self.active_df = self.active_df[self.active_df.sport.isin([x.strip() for x in filter_options['sport'].split(',')])]

        if filter_options['name'] is not None:
            re_str = f'.*{filter_options["name"]}.*'
            self.active_df = self.active_df[self.active_df.name.str.match(re_str)]

        if filter_options['min_reward'] is not None:
            self.active_df = self.active_df[self.active_df.reward >= filter_options['min_reward']]
        if filter_options['max_reward'] is not None:
            self.active_df = self.active_df[self.active_df.reward <= filter_options['max_reward']]

        if filter_options['min_winner_reward'] is not None:
            self.active_df = self.active_df[self.active_df.winner_reward >= filter_options['min_winner_reward']]
        if filter_options['max_winner_reward'] is not None:
            self.active_df = self.active_df[self.active_df.winner_reward <= filter_options['max_winner_reward']]

    def disable_filter(self):
        self.active_df = self.df


