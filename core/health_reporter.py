class HealthReporter:
    def __init__(self, config):
        self.config = config
        
    def send_final_summary(self):
        print("📧 Enviando resumo final de erros e performance...")
        # Lógica de envio para GitHub/Email