"""
This file deletes a specified environment variable
"""

def delete_env(args, scene_root, history_db, current_scene_db):
    """deletes the environment variable specified in args. Can be passed only a name or an ordinal"""
    from src.mtool.util.sqlite import sqlite_environment
    from src.mtool.display import display_env
    from src.mtool.display import display_error

    name = args.name

    if f"{name}".isdigit():
        #checking if the user passed an ordinal instead of a string
        name = sqlite_environment.get_env_by_ord(current_scene_db, int(name))
        if name == "":
            display_error.env_not_found_error(args.name)
            return "env_not_found"

    if(sqlite_environment.delete_env(current_scene_db, name)):
        display_env.display_delete_env(name)
        return name
    else:
        display_error.env_not_found_error(name)
        return "env_not_found"
    