import tkinter as tk

def converter():
    try:
        centimetros = float(entrada_cm.get())
        metros = centimetros / 100
        resultado_label.config(text=f"{centimetros} centímetros é igual a {metros} metros")
    except ValueError:
        resultado_label.config(text="Por favor, insira um valor válido.")

janela = tk.Tk()
janela.geometry("300x180")
janela.title("Conversor de Centímetros para Metros")

instrucao_label = tk.Label(janela, text="Digite o valor em centímetros:")
instrucao_label.pack()

entrada_cm = tk.Entry(janela)
entrada_cm.pack()

botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()
