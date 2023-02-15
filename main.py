import operator

from environs import Env


from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Group, Column, Select

from hiding_widget import window, MySG
from input_types import check, fruits_kbd, get_data, on_fruit_selected, fruits_kbd_radio, fruits_kbd_multiselect

from aiogram_dialog_url import go_btn
from buttons import row, column, group, scrolling_group
from switch import dialog, DialogSG

env = Env()
env.read_env()


storage = MemoryStorage()
API_TOKEN = env.str("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)







main_window = Window(
    Format("{fruits} list"),
    fruits_kbd_multiselect,
    state=MySG.main,
    getter=get_data
)



# dialog = Dialog(window)
registry.register(dialog)


@dp.message_handler(commands=["start"])
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=DialogSG.first, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)