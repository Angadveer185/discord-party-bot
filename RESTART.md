# Restart the Discord Bot

Use this runbook to deploy the latest code and restart the bot service on the server.

## 1. Connect to the Server

Replace the placeholders with your server username and address:

```bash
ssh user@server
```

## 2. Open the Project Directory

```bash
cd discord-party-bot
```

## 3. Pull the Latest Changes

Make sure the working tree is clean before pulling:

```bash
git status
git pull
```

## 4. Restart the Service

```bash
sudo systemctl restart discord-party-bot
```

## 5. Check the Service Status

Confirm that the service is active and running:

```bash
sudo systemctl status discord-party-bot
```

Press `q` to exit the status view.

## View Live Logs

To watch the bot logs while testing:

```bash
sudo journalctl -u discord-party-bot -f
```

Press `Ctrl+C` to stop following the logs.

## Quick Restart

Once connected and inside the project directory, the routine restart is:

```bash
git pull
sudo systemctl restart discord-party-bot
sudo systemctl status discord-party-bot
```

> Keep the server's `.env` file private. It contains the Discord bot token and should not be stored in Git.
