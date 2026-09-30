import requests
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '<REDACTED_HISTORICAL_SECRET>')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '<REDACTED_HISTORICAL_SECRET>')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        response = requests.post(url, data=payload)
        return response.status_code
    except Exception as e:
        print(f"Erro ao enviar mensagem Telegram: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        send_telegram_message(' '.join(sys.argv[1:]))
    else:
        send_telegram_message("⚡ TopazioCoin server status: Script testado com sucesso!")
