import threading
import time

class VoiceManager:
    def __init__(self, config):
        self.config = config
        self.active = False
        self.available = False
        
        # Tenta importar, se falhar, apenas define como indisponível
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.available = True
            print("🎤 Módulo de voz carregado.")
        except Exception as e:
            print(f"⚠️ Módulo de voz indisponível (Sem erro crítico): {e}")
            self.available = False

    def start_listening(self):
        if not self.available:
            return
            
        self.active = True
        thread = threading.Thread(target=self._loop, daemon=True)
        thread.start()

    def _loop(self):
        import speech_recognition as sr
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                while self.active:
                    try:
                        audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                        text = self.recognizer.recognize_google(audio, language='pt-BR').lower()
                        if "oi overlay" in text:
                            self.process_command(text)
                    except:
                        pass
        except Exception as e:
            print(f"❌ Erro no loop de voz: {e}")
            self.active = False

    def process_command(self, text):
        print(f"🎤 Comando Recebido: {text}")
        # Lógica de comando aqui
