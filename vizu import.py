import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]
#x2 = [2, 4, 6, 8, 10]
#y2 = [5, 1, 3, 7, 4]

titulo = 'Grafico de Barras'
eixox = 'Eixo X'
Eixoy = 'Eixo Y'

#Titulo do Grafico
plt.title("meu primeiro grafico em Python")

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


#Mostra pontos nos valores dos graficos 
plt.scatter(x,y, label = "Meus Pontos",
            color = '#000000', #cor dos pontos
            marker=".", #muda o tipo de objeto(ponto) que vai ser exibido
            s=z)#aumenta o tamanho do ponto
plt.plot(x,y, color="k", linestyle="--")#interliga os pontos acima 

#plt.bar(x1,y1, label = 'Grupo 1') #Grafico de Barras
#plt.bar(x2,y2, label = 'Grupo 2')
#plt.legend()#plotando o label das linhas de cima(uma legenda)
#plt.plot(x,y) # Grafico Linear


#plt.show()
#plt.savefig('figura.png')#salvando grafico como imagem
#plt.savefig('figura.pdf')salvando como arquivo pdf
plt.savefig('figura.png',dpi=300)#atributo dpi é o tamanho da imagem

