from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.text import Const

from aiogram_dialog_url import go_btn
from buttons import row, column, group, scrolling_group

storage = MemoryStorage()
bot = Bot(token='5536456718:AAFcwdBSUxgiFNvIrvR17vottb3s169-1fY')
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


class MySG(StatesGroup):
    main = State()



class DialogSG(StatesGroup):
    ANIMALS = State()


async def get_data(**kwargs):
    return {
        "title": "Animals list",
        "animals": ['cat', 'dog', 'my brother\'s tortoise']
    }




main_window = Window(
    Const("Mening github sahifam"),
    go_btn,
    state=MySG.main
)

row_button_window = Window(
    Const("Bu row tugmalar"),
    row,
    state=MySG.main
)

column_button_window = Window(
    Const("Bu column tugmalar"),
    column,
    state=MySG.main
)

group_button_window = Window(
    Const("Group buttons"),
    group,
    state=MySG.main
)


scrolling_group_window = Window(
    Const("Scrolling buttons"),
    scrolling_group,
    state=MySG.main
)


dialog = Dialog(scrolling_group_window)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)