# ... (código anterior do config_gui.py)

# Adicione este campo na interface, logo abaixo da chave da Riot
tk.Label(root, text="GitHub Token (Opcional - Para relatórios de erro):", bg="#f0f0f0").pack()
entry_github = tk.Entry(root, width=50)
entry_github.pack(pady=5)
tk.Label(root, text="Deixe vazio se não quiser enviar logs.", fg="gray", font=("Arial", 8)).pack()

# ... (na função save_config)
def save_config():
    openrouter = entry_openrouter.get()
    riot = entry_riot.get()
    github = entry_github.get() # Pega o token se o usuário digitou
    consent = var_consent.get()
    
    if not openrouter or not riot:
        messagebox.showerror("Erro", "Chaves da OpenRouter e Riot são obrigatórias!")
        return

    with open(".env", "w") as f:
        f.write(f"OPENROUTER_API_KEY=\"{openrouter}\"\n")
        f.write(f"RIOT_API_KEY=\"{riot}\"\n")
        if github:
            f.write(f"GITHUB_TOKEN=\"{github}\"\n") # Salva apenas se fornecido
        else:
            f.write("GITHUB_TOKEN=\"\"\n")
        
        f.write(f"GITHUB_REPO_OWNER=\"kbelludoo\"\n")
        f.write(f"GITHUB_REPO_NAME=\"tft-ai-overlay-pro\"\n")
        f.write(f"CONSENT_ERROR_REPORT={consent}\n")

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
