from bot_commands import *

# import os
# os.system("pip -V")

app = ApplicationBuilder().token("5883830490:AAEGqF4TaYaD2w69-Ef-_T9N6aDY5gGUnPI").build()
# app = ApplicationBuilder().token("5873069701:AAHypQc7tY8K5--o6yHe3BddYs5FsZdeyhI").build()


app.add_handler(CommandHandler(command="hello", callback=hello_command))
app.add_handler(CommandHandler(command="english_world", callback=eng_world_command))
app.add_handler(CommandHandler(command="joke", callback=joke_command))
app.add_handler(CommandHandler(command="help", callback=help_command))
app.add_handler(CommandHandler(command="time2ny", callback=time_to_new_year_command))
app.add_handler(CommandHandler(command="calculate", callback=calc_command))
app.add_handler(CommandHandler(command="play_x_o", callback=play_x_o_command))
app.add_handler(CommandHandler(command="weather", callback=weather_command))
app.add_handler(CommandHandler(command="exit", callback=exit_command))

my_filters = [filters.USER, filters.VOICE]
for my_filter in my_filters:
    app.add_handler(MessageHandler(filters=my_filter, callback=selector))

print("Server start")
app.run_polling()
print("Server stopped")
