from aiogram import Dispatcher
from .authcheck import AuthCheck
from .admincheck import AdminCheck


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AuthCheck)
    dp.filters_factory.bind(AdminCheck)
