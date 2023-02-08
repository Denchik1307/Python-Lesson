from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime
from dateutil.relativedelta import relativedelta
import game_x_o
from my_calc import calculator
import weather
import eng_lesson
import joke

_state_message_handler = ""

_help = "/help - helper use commands\n" \
        "/hello - hello message\n" \
        "/eng_world - random world with translate\n" \
        "/joke - random joke\n" \
        "/weather - weather for city\n" \
        "/time2ny - Stay to New Year\n" \
        "/calculate - calculator\n" \
        "/play_x_o - game cross-zero\n" \
        "/exit - end subprogram\n"


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = ""
    await update.message.reply_text(f'It`s you HAMLO {update.effective_user.first_name} 😎')


async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = ""
    await update.message.reply_text(f'Bye :-)')


async def eng_world_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = ""
    await update.message.reply_text(eng_lesson.get_world_random())


async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = ""
    await update.message.reply_text(joke.rand_joke())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "exit"
    await update.message.reply_text(_help)


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "weather"
    await update.message.reply_text("Input City name")


async def time_to_new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = ""
    date_now = datetime.today()
    date_new_year = datetime(date_now.year + 1, 1, 1, 0, 0, 0)
    remained = relativedelta(date_new_year, date_now)
    await update.message.reply_text(
        text=f'To {str(datetime.today().year + 1)} stay:\n'
             f'{str(remained.months)} months\n'
             f'{str(remained.days)} days\n'
             f'{str(remained.hours)} hours\n'
             f'{str(remained.minutes)} minutes\n'
             f'{str(remained.seconds)} seconds')


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    _state_message_handler = "calc"
    await update.message.reply_text(text="input for calculate or 'exit' for close calculator")


async def play_x_o_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global _state_message_handler
    game_x_o.first_move()
    _state_message_handler = "game_x_o"
    await update.message.reply_text(text=game_x_o.show_matrix())


async def selector(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global _state_message_handler
    print(True if update.message.text else False)
    print(True if update.message.voice else False)
    print(True if update.message.audio else False)
    if update.message.text:
        if update.message.text == "exit":
            await exit_command()
        # await update.message.reply_text(text=_state_message_handler)
        if _state_message_handler == "calc":
            res = calculator(update.message.text)
            await update.message.reply_text(text=f"{update.message.text}={res}")
            await update.message.reply_text(text="input for calculate or 'exit' for close calculator")
        if _state_message_handler == "game_x_o":
            await update.message.reply_text(game_x_o.start_game(update.message.text))
        elif not game_x_o.is_first:
            game_x_o.is_first = True
        if _state_message_handler == "weather":
            await update.message.reply_text(weather.get_weather(update.message.text))
