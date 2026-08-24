import threading
import os
from flask import Flask

app = Flask(__name__)

# 1. Health check endpoint'i (UptimeRobot buraya istek atacak)
@app.route('/')
def health_check():
    return "Technocore Agent is Running!", 200

# 2. FLOP Labs Agent kodunuzu arka plan iş parçacığında (Thread) başlatın
def run_agent():
    print("Agent başlatılıyor...")
    # Botunuzun ana scripti neyse (örn: agent.py veya main.py) onu çalıştırın:
    os.system("python main.py")  # Repo içindeki ana çalıştırma dosyasının adı

if __name__ == "__main__":
    # Botu ayrı bir thread'de başlat
    threading.Thread(target=run_agent, daemon=True).start()
    # Web sunucusunu başlat
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
