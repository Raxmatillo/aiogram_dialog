from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Group
from input_types import check, fruits_kbd, get_data

from aiogram_dialog_url import go_btn
from buttons import row, column, group, scrolling_group

storage = MemoryStorage()
bot = Bot(token='5536456718:AAFcwdBSUxgiFNvIrvR17vottb3s169-1fY')
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


class MySG(StatesGroup):
    main = State()




main_window = Window(
    Const("Selected fruits"),
    fruits_kbd,
    state=MySG.main,
    getter=get_data
)


dialog = Dialog(main_window)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)