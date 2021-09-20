from aiogram.dispatcher.filters.state import StatesGroup, State


class InteractivePanels(StatesGroup):
    Serial = State()
    Photo = State()
    Question = State()
    End = State()
