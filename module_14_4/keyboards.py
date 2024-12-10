from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить', ), ]
    ],
    resize_keyboard=True)

inline_kb = InlineKeyboardMarkup()
button_i = InlineKeyboardButton(text='Информация', callback_data='info')
button_i_calc = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_i_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.row(button_i_calc, button_i_formulas)

inline_product = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Product1", callback_data="product_buying"),
         InlineKeyboardButton(text="Product2", callback_data="product_buying"),
         InlineKeyboardButton(text="Product3", callback_data="product_buying"),
         InlineKeyboardButton(text="Product4", callback_data="product_buying")
         ]
    ], resize_keyboard=True
)
