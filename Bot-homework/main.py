

from bot_commands import *
# import os
# os.system("pip -V")

app = ApplicationBuilder().token("5883830490:AAFrWHdmwn7FcVkAaXB1mQCcEjcJjbuEQEE").build()
# app = ApplicationBuilder().token("5873069701:AAHypQc7tY8K5--o6yHe3BddYs5FsZdeyhI").build()

# start_callback()

app.add_handler(CommandHandler(command="hello", callback=hello_command))
app.add_handler(CommandHandler(command="time", callback=time_to_new_year_command))
app.add_handler(CommandHandler(command="calculate", callback=calc_command))
app.add_handler(CommandHandler(command="play_x_o", callback=play_x_o_command))
app.add_handler(CommandHandler(command="weather", callback=weather_command))

mess_handler = MessageHandler(filters=filters.USER, callback=selector)
app.add_handler(mess_handler)

print("Server start")
app.run_polling()
print("Server stopped")
