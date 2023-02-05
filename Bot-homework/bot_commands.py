from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime
from dateutil.relativedelta import relativedelta
import game_x_o
from my_calc import calculator
import weather

_state_message_handler = ""


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = ""
    await update.message.reply_text(f'It`s you HAMLO {update.effective_user.first_name} :-)')


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "weather"
    await update.message.reply_text(weather.get_weather(update.message.text.split()[1]))


async def time_to_new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = ""
    date_now = datetime.today()
    date_new_year = datetime(date_now.year + 1, 1, 1, 0, 0, 0)
    remained = relativedelta(date_new_year, date_now)
    await update.message.reply_text(
        text=f'To {str(datetime.today().year + 1)} stay:\n'
             f'{str(remained.days)} days\n'
             f'{str(remained.months)} months\n'
             f'{str(remained.hours)} hours\n'
             f'{str(remained.minutes)} minutes\n'
             f'{str(remained.seconds)} seconds')


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "calc"
    await update.message.reply_text(text="input for calculate or 'exit' for close calculator")
    # await update.message.reply_text(text=update.message.text)


async def play_x_o_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "game_x_o"
    await update.message.reply_text(text=game_x_o.show_matrix())


async def selector(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global _state_message_handler
    if update.message.text == "exit":
        _state_message_handler = ""
        await update.message.reply_text(text="Bye )")
    # await update.message.reply_text(text=_state_message_handler)
    if _state_message_handler == "calc":
        res = calculator(update.message.text)
        await update.message.reply_text(text=f"{update.message.text}={res}")
        await update.message.reply_text(text="input for calculate or 'exit' for close calculator")
    if _state_message_handler == "game_x_o":
        await update.message.reply_text(game_x_o.start_game(update.message.text))
    elif not game_x_o.is_first:
        game_x_o.is_first = True
