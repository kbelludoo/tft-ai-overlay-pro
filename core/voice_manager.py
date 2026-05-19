import threading
import time

# Tenta importar, mas não quebra o programa se falhar
try:
    import speech_recognition as sr
    VOICE_AVAILABLE = True
except ImportError:
    VOICE_AVAILABLE = False
    print("⚠️ Módulo de voz não disponível (instale speech_recognition)")

class VoiceManager:
    def __init__(self, config):
        self.config = config
        self.active = False
        if not VOICE_AVAILABLE:
            print("🎤 Voz desativada: biblioteca não encontrada.")
            return
            
        self.recognizer = sr.Recognizer()
        
    def start_listening(self):
        if not VOICE_AVAILABLE: return
        self.active = True
        threading.Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                while self.active:
                    try:
                        audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=5)
                        text = self.recognizer.recognize_google(audio, language='pt-BR').lower()
                        if "oi overlay" in text:
                            print(f"🎤 Ouvi: {text}")
                            # Aqui entraria a lógica de comando
                    except Exception:
                        pass
        except Exception:
            self.active = False
