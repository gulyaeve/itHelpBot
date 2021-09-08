from aiogram.dispatcher.filters.state import StatesGroup, State


class InteractivePanels(StatesGroup):
    Serial = State()
    Q1 = State()
    Q2 = State()
