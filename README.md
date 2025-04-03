# Discord Moderation Bot

This project is a Discord bot that implements moderation commands inspired by Linux commands. The bot allows server administrators to manage users effectively using simple commands.

## Features

- **Moderation Commands**: Kick and ban users using commands inspired by Linux (`rm` for kick and `rm -r` for ban).
- **Easy Setup**: Simple installation and configuration process.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/discord-moderation-bot.git
   cd discord-moderation-bot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your bot token in the `bot.py` file.

## Usage

1. Run the bot:
   ```
   python src/bot.py
   ```

2. Use the following commands in your Discord server:
   - To kick a user: `rm @username`
   - To ban a user: `rm -r @username`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.