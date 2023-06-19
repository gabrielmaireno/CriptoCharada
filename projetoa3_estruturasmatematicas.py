import math
from tkinter import *
from tkinter import messagebox
    
janela = Tk()

    
frase_secreta = "baba"
array_numeros = []

for letra in frase_secreta:
    alfabeto = ord(letra.lower()) - 96 # subtrai 96 para obter o número correspondente a 'a'
    array_numeros.append(alfabeto)

    #Função Cifra de César

def teste(numeros, resultados):
    if ((numeros + resultados) % 26) == 0:
        return (numeros + resultados) % 27
    else:
        return (numeros + resultados) % 26

#Função Para converter Cifra de César númerica em letras

def conversaoLetras(numeros):
    if (numeros<= 26):
        return chr(numeros+96)
    else:
        chr(numeros % 26 +96)

# Primeira técnica matemática - Teorema de pitágoras
a = 8
b = 6
t1 = int(math.sqrt(a**2 + b**2))
array_numeros = [teste(num, t1) for num in array_numeros]
array_letras = [conversaoLetras(num) for num in array_numeros]
frase_t1 = "".join(array_letras)
print("Frase criptografada 3:", frase_t1)

# Segunda técnica matemática - Equação de primeiro grau
z = 1
t2 = 2*z + 1
array_numeros = [teste(num, t2) for num in array_numeros]
array_letras = [conversaoLetras(num) for num in array_numeros]
frase_t2 = "".join(array_letras)
print("Frase criptografada 2:", frase_t2)

# Terceira técnica matemática - Distância de Manhattan
x = [1, 5, 4]
y = [2, 8, 3]
t3 = sum([abs(xi - yi) for xi, yi in zip(x, y)])
array_numeros = [teste(num, t3) for num in array_numeros]
array_letras = [conversaoLetras(num) for num in array_numeros]
frase_t3 = "".join(array_letras)
print("Frase criptografada 1:", frase_t3)


def abrirTela():
    def logicaTexto():
        if(texto_input.get()!=frase_t1 and texto_input.get()!=frase_t2 and texto_input.get()!=frase_t3 and texto_input.get()!=frase_secreta):    
            messagebox.showinfo("Errou","Você infelizmente errou! Tente novamente")
            texto_input.delete(0, "end")
        elif(texto_input.get()==frase_t2):
            texto_orientacao.configure(text="Há um pato entre dois patos, um pato atrás de um pato\ne um pato na frente de outro pato.De quantos patos estamos falando?")
            texto_cript.configure(text=frase_t2)
            texto_input.delete(0, "end")
        elif(texto_input.get()==frase_t1):
            texto_orientacao.configure(text="Caminhando ao fim da tarde, uma senhora contou 10 casas em uma rua à sua direita.\nNo regresso, ela contou 10 casas à sua esquerda. Quantas casas ela viu no total?")
            texto_cript.configure(text=frase_t1)
            texto_input.delete(0, "end")
        elif(texto_input.get()==frase_secreta):
            texto_orientacao.configure(text="Concluido")
            messagebox.showinfo("Concluido", "Voce acertou a palavra!!!")
            janela.destroy()
        else:(print("Ocorreu algum erro!"))

    janela.title("Criptografador")
    janela.geometry("480x240")
    janela.resizable(0,0)
    janela.columnconfigure(0,weight=10)
    janela.columnconfigure(1,weight=10)
    janela.columnconfigure(2,weight=10)
    janela.geometry()
    texto_orientacao = Label(janela, text="Meu avô tem 2 filhos, cada filho tem 5 filhos. Quantos primos eu tenho?")
    texto_orientacao.grid(column=1,row=0,pady=7)
    texto_cript_tx = Label(janela,text="Texto Criptografado: ")
    texto_cript_tx.grid(column=1,row=1,pady=5)
    texto_dica = Label(janela,text="Dica: Você precisa voltar para prosseguir.")
    texto_dica.grid(column=1,row=5,pady=20)
    texto_cript = Label(janela, text=frase_t3)
    texto_cript.grid(column=1,row=2,pady=5)
    texto_input = Entry(janela,width=25)
    texto_input.grid(column=1,row=4,pady=5)
    texto_button = Button(janela,text="Prosseguir",command=lambda:(logicaTexto()))
    texto_button.grid(column=1,row=3,pady=5)
    janela.mainloop()

janela.title("Iniciar")
janela.geometry("480x240")
janela.resizable(0,0)
janela.columnconfigure(0,weight=10)
janela.columnconfigure(1,weight=10)
janela.columnconfigure(2,weight=10)
janela.geometry()
texto_orientacao = Label(janela, text="Bem-vindo")
texto_orientacao.grid(column=1,row=0,pady=7)
texto_button = Button(janela,text="Começar",command=lambda:(abrirTela(),))
texto_button.grid(column=1,row=3,pady=5)
janela.mainloop()






