import tkinter as tk
from tkinter import messagebox
import os
import sys

def save_config():
    openrouter = entry_openrouter.get()
    riot = entry_riot.get()
    github = entry_github.get()
    
    if not openrouter or not riot:
        messagebox.showerror("Erro", "As chaves da OpenRouter e Riot são obrigatórias!")
        return

    # Criar arquivo .env
    with open(".env", "w") as f:
        f.write(f"OPENROUTER_API_KEY=\"{openrouter}\"\n")
        f.write(f"RIOT_API_KEY=\"{riot}\"\n")
        f.write(f"GITHUB_TOKEN=\"{github}\"\n")
        f.write(f"GITHUB_REPO_OWNER=\"kbelludoo\"\n")
        f.write(f"GITHUB_REPO_NAME=\"tft-ai-overlay-pro\"\n")
        f.write(f"CONSENT_ERROR_REPORT=true\n")
        f.write(f"USER_EMAIL_REPORT=\"kbelludoo@gmail.com\"\n")
    
    messagebox.showinfo("Sucesso", "Configurações salvas! O instalador continuará agora.")
    root.destroy()
    sys.exit(0)

root = tk.Tk()
root.title("Configuração Inicial - TFT AI Overlay")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Bem-vindo! Insira suas chaves de API:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

# OpenRouter
tk.Label(root, text="Chave OpenRouter (IA):", bg="#f0f0f0").pack()
entry_openrouter = tk.Entry(root, width=50)
entry_openrouter.pack(pady=5)
tk.Label(root, text="(Pegue em: https://opencode.ai/br)", fg="blue", cursor="hand2").pack()

# Riot
tk.Label(root, text="Chave Riot Games:", bg="#f0f0f0").pack()
entry_riot = tk.Entry(root, width=50)
entry_riot.pack(pady=5)
tk.Label(root, text="(Pegue em: https://developer.riotgames.com/)", fg="blue", cursor="hand2").pack()

# GitHub (Opcional)
tk.Label(root, text="GitHub Token (Opcional - Para logs):", bg="#f0f0f0").pack()
entry_github = tk.Entry(root, width=50)
entry_github.pack(pady=5)

btn_save = tk.Button(root, text="Salvar e Continuar", command=save_config, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=20, pady=5)
btn_save.pack(pady=20)

root.mainloop()