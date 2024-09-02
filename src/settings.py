import os
import configparser


class Settings:
    """This class is used to load, store, change and save game settings"""
    def __init__(self):
        self.pause = False
        self.theme = 'default'
        self.ball_speed = 7
        self.sound_state = 'on'

        self.theme_list = [f.name for f in os.scandir('resources/themes') if f.is_dir()]
        self.ball_speed_list = [5, 6, 7, 8, 9, 10]
        self.sound_state_list = ['on', 'off']

    def load_from_file(self, file_path):
        """
        Load game settings from 'config' file
        :param file_path: 'config' file directory
        """
        config = configparser.ConfigParser()
        config.read(file_path)

        self.theme = str(config.get('General', 'theme'))
        self.ball_speed = int(config.get('General', 'ball_speed'))
        self.sound_state = str(config.get('General', 'sound_state'))

    def save_to_file(self, file_path):
        """
        Save game settings to 'config' file
        :param file_path: 'config' file directory
        """
        config = configparser.ConfigParser()
        config['General'] = {'theme': self.theme, 'ball_speed': self.ball_speed, 'sound_state': self.sound_state}
        with open(file_path, 'w') as configfile:
            config.write(configfile)
