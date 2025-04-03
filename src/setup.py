import os

def setup_bot():
    bot_file_path = os.path.join(os.path.dirname(__file__), "bot.py")

    # Check if bot.py exists
    if not os.path.exists(bot_file_path):
        print("Error: bot.py not found.")
        return

    # Ask the user for the Discord token
    discord_token = input("Please enter your Discord bot token: ").strip()

    if not discord_token:
        print("Error: No token provided.")
        return

    # Write the token to bot.py
    with open(bot_file_path, "a") as bot_file:
        bot_file.write(f'\nDISCORD_TOKEN = "{discord_token}"\n')

    print("Discord token has been added to bot.py.")

if __name__ == "__main__":
    setup_bot()