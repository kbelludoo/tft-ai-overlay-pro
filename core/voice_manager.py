import threading
import time
import sys

class VoiceManager:
    def __init__(self, config):
        self.config = config
        self.active = False
        self.listen_thread = None
        self.engine_available = False
        
        # Tenta importar as bibliotecas de forma segura
        try:
            import speech_recognition as sr
            self.sr = sr
            self.recognizer = sr.Recognizer()
            
            # Tenta configurar o microfone
            try:
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                self.engine_available = True
                print("✅ Microfone detectado e pronto!")
            except Exception as e:
                print(f"⚠️ Microfone não detectado: {e}")
                
        except ImportError:
            print("⚠️ Bibliotecas de voz não encontradas. Modo de voz desativado.")
            self.engine_available = False

    def start_listening(self):
        if not self.engine_available:
            return
            
        self.active = True
        self.listen_thread = threading.Thread(target=self._loop, daemon=True)
        self.listen_thread.start()
        print("🎙️ Ouvindo comandos de voz... (Diga 'Oi Overlay')")

    def _loop(self):
        with self.sr.Microphone() as source:
            # Ajuste dinâmico de ruído a cada 30 segundos
            while self.active:
                try:
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
                    text = self.recognizer.recognize_google(audio, language='pt-BR').lower()
                    
                    if "oi overlay" in text or "estrategista" in text:
                        print(f"🗣️ Comando Detectado: {text}")
                        self.process_command(text)
                    elif "parar de ouvir" in text:
                        print("🔇 Modo de voz pausado.")
                        time.sleep(2) # Pausa breve
                        break
                except self.sr.WaitTimeoutError:
                    pass
                except self.sr.UnknownValueError:
                    pass
                except Exception as e:
                    print(f"Erro no loop de voz: {e}")
                    time.sleep(1)

    def process_command(self, text):
        # Lógica simplificada para demonstração
        if "deuses" in text:
            print("🔮 Analisando seus deuses disponíveis...")
        elif "inimigo" in text:
            print("⚔️ Registrando composição inimiga...")
        else:
            print("❓ Comando recebido. Processando...")
