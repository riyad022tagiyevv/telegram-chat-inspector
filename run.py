from bot import create_bot

token = "7246915007:AAHa_Pn-_pf3jsnFL_sUeFBMcMAIblJ-gjk"
bot = create_bot(token)

if __name__ == "__main__":
    bot.start_polling(1.0)
    bot.idle()
