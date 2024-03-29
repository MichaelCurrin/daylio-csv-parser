# -*- coding: utf-8 -*-
"""
Lib application configuration file.
"""
import os
from configparser import ConfigParser

from . import APP_DIR


class AppConf(ConfigParser):
    """
    App configuration object.

    Make app configuration filenames absolute paths and relative to app
    config dir. Then configure the conf object with data.
    The local app conf file is optional and in values in it will overwrite
    those set in the main app conf file.
    """

    def __init__(self):
        """
        Initialise instance of AppConf class.

        Read config files in three locations, expecting the first versioned
        file to always be present and the two optional files to either override
        the default values or be ignored silently if they are missing.
        """
        super().__init__()

        etc_conf_names = ("app.conf", "app.local.conf")
        conf_paths = [os.path.join(APP_DIR, "etc", c) for c in etc_conf_names]

        user_config_path = os.path.join(
            os.path.expanduser("~"), ".config", "dayliopy.conf"
        )
        conf_paths.append(user_config_path)

        self.read(conf_paths)
        self.set("DEFAULT", "app_dir", APP_DIR)

        self.MOODS = {
            self.get("daylio", "mood1"): 1,
            self.get("daylio", "mood2"): 2,
            self.get("daylio", "mood3"): 3,
            self.get("daylio", "mood4"): 4,
            self.get("daylio", "mood5"): 5,
        }


def main():
    """
    Test to display the values read in across the three conf file locations.
    """
    conf = AppConf()

    for section in conf.sections():
        print(section)

        for option, value in conf.items(section):
            print(f" {option:15}: {value}")

    print(conf.MOODS)


if __name__ == "__main__":
    main()
