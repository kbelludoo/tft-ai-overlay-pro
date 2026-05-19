import speech_recognition as sr
import threading
import time

class VoiceManager:
    def __init__(self, config):
        self.config = config
        self.recognizer = sr.Recognizer()
        self.active = False
        self.listen_thread = None
        
    def start_listening(self):
        self.active = True
        self.listen_thread = threading.Thread(target=self._loop, daemon=True)
        self.listen_thread.start()

    def _loop(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.active:
                try:
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    text = self.recognizer.recognize_google(audio, language='pt-BR').lower()
                    if "oi overlay" in text:
                        self.process_command(text)
                except:
                    pass

    def process_command(self, text):
        print(f"🎤 Comando Recebido: {text}")
        # Lógica de processamento de comando aqui