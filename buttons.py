
from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Row, Column, Group, ScrollingGroup
from aiogram_dialog.widgets.text import Const

# Go button bosilganda ishga tushuvchi funksiya
async def go_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    await c.message.answer("Going on!")


# Run button bosilganda ishga tushovchi funksiya
async def run_clicked(c: CallbackQuery, button: Button, manager: DialogManager):
    await c.message.answer("Running!")

# row Row classi yordamida qator buttonlari yozilmoqda
row = Row(
    Button(Const("Go"), id="go", on_click=go_clicked),
    Button(Const("Run"), id="run", on_click=run_clicked),
    Button(Const("Fly"), id="fly"),
)



# Column - ustun buttonlari yozilmoqda
column = Column(
    Button(Const("Go"), id="go"),
    Button(Const("Run"), id="run"),
    Button(Const("Fly"), id="fly")
)

# Group - guruxli button yozilmoqda
group = Group(
    Row(
        Button(Const("Go"), id="go"),
        Button(Const("Run"), id="run"),
    ),
    Button(Const("Fly"), id="fly")
)



def test_buttons_creator(btn_quantity):
    buttons = []
    for i in btn_quantity:
        i = str(i)
        buttons.append(Button(Const(i), id=i))
    return buttons

test_buttons = test_buttons_creator(range(0, 100))


# ScrollingGroup - tugmalar ro'yxati
scrolling_group = ScrollingGroup(
    *test_buttons,
    id="numbers",
    width=6,
    height=6
)