# Play2Gold — Telegram Mini App

- `web/` — игра (index.html), публикуется через GitHub Pages
- `bot/` — Telegram-бот с кнопкой «Играть»

## Запуск
1. Settings → Pages → Source: **GitHub Actions**. Адрес будет `https://USERNAME.github.io/REPO/`.
2. Создай бота у @BotFather, получи токен.
3. Локально или на сервере:
   ```
   cd bot
   pip install -r requirements.txt
   export BOT_TOKEN=... WEBAPP_URL=https://USERNAME.github.io/REPO/
   python bot.py
   ```
Бот должен работать постоянно (GitHub Pages хостит только игру, не бота) — подойдут Railway, Render, Fly.io или VPS.
