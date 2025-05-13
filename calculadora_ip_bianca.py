import tkinter as tk
from tkinter import messagebox
import ipaddress

def calcular_dados_ip():
    ip = entrada_ip.get()
    mascara = entrada_mascara.get()
    
    try:
        rede = ipaddress.ip_network(f"{ip}/{mascara}", strict=False)
        endereco_rede = rede.network_address
        primeiro_host = list(rede.hosts())[0] if rede.num_addresses > 2 else "N/A"
        ultimo_host = list(rede.hosts())[-1] if rede.num_addresses > 2 else "N/A"
        endereco_broadcast = rede.broadcast_address
        classe = determinar_classe(ip)
        num_sub_redes = 2 ** (rede.max_prefixlen - rede.prefixlen)
        hosts_por_subrede = rede.num_addresses - 2 
        endereco_privado = "Privado" if rede.is_private else "Público"
        
     
        resultado_texto.set(
            f"Endereço de Rede: {endereco_rede}\n"
            f"Primeiro Host: {primeiro_host}\n"
            f"Último Host: {ultimo_host}\n"
            f"Endereço de Broadcast: {endereco_broadcast}\n"
            f"Classe do Endereço: {classe}\n"
            f"Número de Sub-redes: {num_sub_redes}\n"
            f"Hosts por Sub-rede: {hosts_por_subrede}\n"
            f"Endereço Público/Privado: {endereco_privado}"
        )
    except Exception as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}", font="arial",fg="red")

def determinar_classe(ip):
    primeiro_octeto = int(ip.split('.')[0])
    if 1 <= primeiro_octeto <= 126:
        return "A"
    elif 128 <= primeiro_octeto <= 191:
        return "B"
    elif 192 <= primeiro_octeto <= 223:
        return "C"
    elif 224 <= primeiro_octeto <= 239:
        return "D (Multicast)"
    elif 240 <= primeiro_octeto <= 255:
        return "E (Experimental)"
    else:
        return "Desconhecida"


janela = tk.Tk()
janela.title("Calculadora de IP")
janela.geometry("400x400")


tk.Label(janela, text="Digite o endereço de IP", font="arial",fg="black").pack(pady=5)
entrada_ip = tk.Entry(janela, width=30,font="arial")
entrada_ip.pack()

tk.Label(janela, text="Digite a máscara da sub-rede", font="arial",fg="black").pack(pady=5)
entrada_mascara = tk.Entry(janela, width=30,font="arial")
entrada_mascara.pack()


tk.Button(janela, text="Calcular", command=calcular_dados_ip, font="arial",bg="black",fg="white",width=10,height=1).pack(pady=10)


resultado_texto = tk.StringVar()
tk.Label(janela, textvariable=resultado_texto, justify="left", font="arial").pack(pady=10)

janela.mainloop()