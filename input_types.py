from typing import Any
import operator

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Checkbox, ManagedCheckboxAdapter, Select, Radio, Multiselect
from aiogram_dialog.widgets.text import Const, Format

async def check_changed(event: ChatEvent, checkbox: ManagedCheckboxAdapter, manager: DialogManager):
    print("Check status changed:", checkbox.is_checked())


# checkbox
check = Checkbox(
    Const("✅ Checked"),
    Const("☑️ Unchecked"),
    id="check",
    default=True, # default holatda True bo'ladi
    on_state_changed=check_changed
)


# select
async def get_data(**kwargs):
    fruits = [
        ("Apple", "1"),
        ("Pear", "2"),
        ("Orange", "3"),
        ("Banana", "4"),
    ]
    return {
        "fruits": fruits,
        "count": len(fruits),
    }

async def on_fruit_selected(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    print("Fruit selected:", item_id)


async def on_fruit_radio(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    print("Fruit select: ", item_id)
    print(c)
    print(widget)
    print(manager)


fruits_kbd = Select(
    Format("{item[0]} ({pos}/{data[count]})"),  # E.g `✓ Apple (1/4)`
    id="s_fruits",
    item_id_getter=operator.itemgetter(1),  # each item is a tuple with id on a first position
    items="fruits",  # we will use items from window data at a key `fruits`
    on_click=on_fruit_selected,
)

# Radio funksiyasiga misol
fruits_kbd_radio = Radio(
    Format("⚫️ {item[0]}"),
    Format("⚪️ {item[0]}"),
    id="r_fruits",
    item_id_getter=operator.itemgetter(1),
    items="fruits",
    on_click=on_fruit_radio
)


# Multiselect bir qancha tanlash
fruits_kbd_multiselect = Multiselect(
    Format("✅ {item[0]}"),
    Format("{item[0]}"),
    id="m_fruits",
    item_id_getter=operator.itemgetter(1),
    items="fruits",
)

print(operator.itemgetter(1))