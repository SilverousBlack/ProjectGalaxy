import pathlib as pl
import typing

import configparser as cp
import json
import jsonschema

__module_init_flag = False

COMMON_CONFIG: pl.Path
GALAXY_CONFIG: dict

def load(path: pl.Path):
    global COMMON_CONFIG, GALAXY_CONFIG
    COMMON_CONFIG_PATH: pl.Path = pl.Path(path).parents[1].joinpath("meta/.common.conf")
    
    COMMON_CONFIG = cp.ConfigParser()
    COMMON_CONFIG.read(COMMON_CONFIG_PATH)
    
    GALAXY_CONFIG = json.load(open(COMMON_CONFIG_PATH.parent.joinpath(COMMON_CONFIG["lib.galaxy"]["path"]), "r"))

if not __module_init_flag:
    load(__file__)
    print()
