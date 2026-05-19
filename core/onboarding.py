class Onboarding:
    def __init__(self, config):
        self.config = config
        
    def run_wizard(self):
        print("🎓 Bem-vindo! Vamos calibrar sua IA...")
        print("Cenário 1: Você está no Round 15 com vida baixa...")
        # Simulação do tutorial
        self.config.save_user_data()
        print("✅ Calibração completa! Boa sorte na escalada.")