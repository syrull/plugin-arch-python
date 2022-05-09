from importlib import import_module


from actions import BaseAction
from configuration import ACTIONS


def load_actions():
    # Ensure loading of the classes
    _ = [import_module(i) for i in ACTIONS]
    actions = BaseAction.__subclasses__()
    return actions