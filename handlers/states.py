from aiogram.utils.helper import Helper, HelperMode, ListItem


class States(Helper):
    """
    машина состояний FSM
    теория и практика:
    https://mastergroosha.github.io/telegram-tutorial-2/fsm/
    https://surik00.gitbooks.io/aiogram-lessons/content/chapter3.html
    """
    mode = HelperMode.snake_case

    SEARCH = ListItem()
    OFFER = ListItem()
