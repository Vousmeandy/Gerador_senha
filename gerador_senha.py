import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError

        caracteres = string.ascii_letters
        if var_numeros.get():
            caracteres += string.digits
        if var_simbolos.get():
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, senha)

    except ValueError:
        messagebox.showerror("Erro", "Digite um tamanho válido e selecione pelo menos uma opção de caractere.")

def copiar_senha():
    senha = entry_resultado.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Copiado!", "Senha copiada para a área de transferência.")
    else:
        messagebox.showwarning("Aviso", "Gere uma senha primeiro.")

def salvar_senha():
    senha = entry_resultado.get()
    if not senha:
        messagebox.showwarning("Aviso", "Gere uma senha primeiro.")
        return
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, "w") as f:
            f.write(senha)
        messagebox.showinfo("Salvo!", f"Senha salva em:\n{arquivo}")

# Interface gráfica
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("420x300")
janela.resizable(False, False)

# Título
label_titulo = tk.Label(janela, text="Gerador de Senhas", font=("Arial", 16, "bold"))
label_titulo.pack(pady=10)

# Entrada do tamanho
frame_tamanho = tk.Frame(janela)
frame_tamanho.pack()

label_tamanho = tk.Label(frame_tamanho, text="Tamanho da senha:")
label_tamanho.pack(side=tk.LEFT)

entry_tamanho = tk.Entry(frame_tamanho, width=5)
entry_tamanho.pack(side=tk.LEFT, padx=5)

# Checkboxes
frame_check = tk.Frame(janela)
frame_check.pack(pady=5)

var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

check_numeros = tk.Checkbutton(frame_check, text="Incluir números", variable=var_numeros)
check_numeros.pack(side=tk.LEFT, padx=10)

check_simbolos = tk.Checkbutton(frame_check, text="Incluir símbolos", variable=var_simbolos)
check_simbolos.pack(side=tk.LEFT)

# Botão de gerar
btn_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha, bg="lightblue", width=20)
btn_gerar.pack(pady=10)

# Resultado
entry_resultado = tk.Entry(janela, font=("Arial", 14), justify='center', width=30)
entry_resultado.pack(pady=10)

# Botões adicionais
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

btn_copiar = tk.Button(frame_botoes, text="Copiar", command=copiar_senha, bg="lightgreen", width=12)
btn_copiar.pack(side=tk.LEFT, padx=5)

btn_salvar = tk.Button(frame_botoes, text="Salvar .txt", command=salvar_senha, bg="lightyellow", width=12)
btn_salvar.pack(side=tk.LEFT, padx=5)

# Executar o app
janela.mainloop()
