import tkinter as tk
from tkinter import messagebox
import os
import sys
import webbrowser

def save_config():
    openrouter = entry_openrouter.get()
    riot = entry_riot.get()
    consent = var_consent.get()
    
    if not openrouter or not riot:
        messagebox.showerror("Erro", "As chaves da OpenRouter e Riot são obrigatórias!")
        return

    # Criar arquivo .env
    try:
        with open(".env", "w", encoding="utf-8") as f:
            f.write(f"OPENROUTER_API_KEY=\"{openrouter}\"\n")
            f.write(f"RIOT_API_KEY=\"{riot}\"\n")
            # Token do GitHub será tratado internamente ou deixado em branco se não houver
            f.write(f"GITHUB_TOKEN=\"\"\n") 
            f.write(f"GITHUB_REPO_OWNER=\"kbelludoo\"\n")
            f.write(f"GITHUB_REPO_NAME=\"tft-ai-overlay-pro\"\n")
            f.write(f"CONSENT_ERROR_REPORT={consent}\n")
            f.write(f"USER_EMAIL_REPORT=\"kbelludoo@gmail.com\"\n")
        
        messagebox.showinfo("Sucesso", "Configurações salvas! O programa será iniciado.")
        root.destroy()
        sys.exit(0)
    except Exception as e:
        messagebox.showerror("Erro Crítico", f"Não foi possível salvar o arquivo .env:\n{str(e)}")

root = tk.Tk()
root.title("Configuração Inicial - TFT AI Overlay")
root.geometry("550x450")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Título
tk.Label(root, text="Bem-vindo ao TFT AI Overlay Pro!", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=15)
tk.Label(root, text="Insira suas chaves de API para começar:", font=("Arial", 10), bg="#f0f0f0").pack()

# Frame OpenRouter
frame_or = tk.Frame(root, bg="#f0f0f0")
frame_or.pack(pady=5)
tk.Label(frame_or, text="Chave OpenRouter (IA):", bg="#f0f0f0").pack(anchor="w")
entry_openrouter = tk.Entry(frame_or, width=60)
entry_openrouter.pack(pady=2)
btn_or = tk.Button(frame_or, text="Pegar Chave Grátis (OpenCode)", fg="blue", cursor="hand2", bg="#f0f0f0", relief="flat", command=lambda: webbrowser.open("https://opencode.ai/br"))
btn_or.pack(anchor="w")

# Frame Riot
frame_riot = tk.Frame(root, bg="#f0f0f0")
frame_riot.pack(pady=5)
tk.Label(frame_riot, text="Chave Riot Games:", bg="#f0f0f0").pack(anchor="w")
entry_riot = tk.Entry(frame_riot, width=60)
entry_riot.pack(pady=2)
btn_riot = tk.Button(frame_riot, text="Pegar Chave (Riot Developer)", fg="blue", cursor="hand2", bg="#f0f0f0", relief="flat", command=lambda: webbrowser.open("https://developer.riotgames.com/"))
btn_riot.pack(anchor="w")

# Consentimento
var_consent = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Enviar relatórios de erros anônimos para melhorar o app", variable=var_consent, bg="#f0f0f0").pack(pady=10)

# Botão Salvar
btn_save = tk.Button(root, text="SALVAR E INICIAR", command=save_config, bg="#28a745", fg="white", font=("Arial", 12, "bold"), padx=30, pady=10)
btn_save.pack(pady=20)

root.mainloop()
