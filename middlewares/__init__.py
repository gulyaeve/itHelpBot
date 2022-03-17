from .id4me import Get4me

from loader import dp

if __name__ == "middlewares":
    dp.middleware.setup(Get4me())