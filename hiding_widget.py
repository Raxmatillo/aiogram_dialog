from typing import Dict

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.kbd import Group, Row, Button
from aiogram_dialog.widgets.text import Multi, Const, Format
from aiogram_dialog.widgets.when import Whenable


class MySG(StatesGroup):
    main = State()


async def get_data(**kwargs):
    return {
        "name": "Raxmatillo",
        "extended": True
    }

def is_raxmatillo(data: Dict, widget: Whenable, manager: DialogManager):
    print(data)
    print(data.keys())
    return data.get("name") == "Raxmatillo"


window = Window(
    Multi(
        Const("Hello"),
        Format("{name}", when="extended"),
        sep=" "
    ),
    Group(
        Row(
            Button(Const("Wait"), id="wait"),
            Button(Const("Ignore"), id="ignore"),
            when="extended",
        ),
        Button(Const("Admin mode"), id="nothing", when=is_raxmatillo),
    ),
    state=MySG.main,
    getter=get_data
)