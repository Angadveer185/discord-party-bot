# Discord Party Bot

A lightweight Discord bot that announces when a party starts in one of several configured voice channels. A party starts when the first non-bot member joins an empty configured channel, and it ends when that channel becomes empty again.

## Features

- Watches a configurable set of Discord voice channels.
- Sends a `Party Started!` embed to the server's `#announcements` text channel.
- Mentions `@everyone` when a party begins.
- Ignores bots joining voice channels.
- Applies a 10-second cooldown per voice channel to prevent duplicate announcements.
- Tracks multiple party channels independently.

## Requirements

- Python 3.10 or newer
- A Discord application and bot account
- Permission to add the bot to a Discord server

## Clone the Repository

Replace the placeholder URL with the repository URL from GitHub:

```bash
git clone https://github.com/<your-username>/discord-party-bot.git
cd discord-party-bot
```

## Installation

Create and activate a virtual environment.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Discord Bot Setup

1. Open the [Discord Developer Portal](https://discord.com/developers/applications) and create or select an application.
2. Open **Bot**, create the bot user, and copy its token.
3. Under **Privileged Gateway Intents**, enable **Server Members Intent**.
4. Open **OAuth2 > URL Generator**.
5. Select the `bot` scope.
6. Grant the bot these permissions in the target server:
   - View Channels
   - Send Messages
   - Embed Links
   - Mention Everyone
7. Use the generated URL to invite the bot to your server.

The bot uses the `voice_states` and `members` intents. Voice state events are required to detect joins and leaves; the members intent is enabled by the code and should also be enabled in the Developer Portal.

## Configuration

Create a `.env` file in the project root:

```dotenv
BOT_TOKEN=your_discord_bot_token_here
```

Never commit `.env` or publish your bot token. The token previously present in this working copy should be considered compromised: revoke or regenerate it from the Discord Developer Portal before running or sharing the project.

### Configure Voice Channels

Edit `PARTY_CHANNELS` in `bot.py` and replace the example IDs with the IDs of the voice channels the bot should watch:

```python
PARTY_CHANNELS = {
    123456789012345678,
    234567890123456789,
}
```

To copy a channel ID in Discord, enable **Developer Mode** under **User Settings > Advanced**, then right-click the voice channel and select **Copy Channel ID**.

The bot looks for a text channel named exactly `announcements`. Rename that channel or update the lookup in `bot.py` if your server uses a different name.

## Run the Bot

Activate the virtual environment, then run:

```bash
python bot.py
```

When the bot connects successfully, the terminal prints its Discord username. Keep the process running for the bot to remain online.

## How It Works

1. A non-bot member joins a configured voice channel.
2. If that member is the first person in the channel, the bot records the party as active.
3. The bot sends an embed to `#announcements` and mentions `@everyone`.
4. Additional members joining the same channel do not trigger another announcement.
5. Once the channel is empty, the party becomes inactive and can be announced again after the cooldown.

## Customization

The following values can be changed near the top of `bot.py`:

- `PARTY_CHANNELS`: voice-channel IDs to monitor.
- `COOLDOWN`: minimum number of seconds between announcements for one channel.
- The `announcements` channel name used for notifications.
- The embed title, description, and color.
- The command prefix, although this bot currently defines no text commands.

## Troubleshooting

- **The bot does not come online:** verify `BOT_TOKEN` is present, valid, and has no surrounding quotes or extra spaces.
- **No announcement appears:** check that the voice channel ID is in `PARTY_CHANNELS`, the target text channel is named `announcements`, and the bot can view and send messages there.
- **The bot cannot mention everyone:** grant the **Mention Everyone** permission and check the server's role and notification settings.
- **Voice events are not detected:** enable **Server Members Intent** in both the Developer Portal and the bot code configuration.
- **The bot announces too often or not often enough:** adjust `COOLDOWN` in `bot.py`.

## Project Files

```text
discord-party-bot/
├── bot.py             # Bot event handlers and party logic
├── requirements.txt   # Python dependencies
├── .env               # Local bot token; do not commit
└── .gitignore         # Ignored local and generated files
```

## License

No license has been specified yet. Add a license before distributing the project publicly.