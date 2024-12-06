import matplotlib.pyplot as plt

def pontos_octantes(x_ponto, y_ponto): # Essa função auxilia na identificação dos pontos simétricos a serem plotados nos oito octantes
   return([(x_ponto, y_ponto), (-x_ponto, y_ponto), (x_ponto, -y_ponto), (-x_ponto, -y_ponto), (y_ponto, x_ponto), (-y_ponto, x_ponto), (y_ponto, -x_ponto), (-y_ponto, -x_ponto)])

def main():
   print("\n### ALGORITMO DE BRESENHAM PARA CIRCUNFERÊNCIAS ###\n")

   raio = int(input("Informe o raio da circunferência: "))
   # Os valores devem ser informados separados por espaço
   x_centro, y_centro = (input("Informe os valores de x e y do centro da circunferência: ").split(" "))

   # Conversão dos valores informados para o tipo inteiro
   x_centro = int(x_centro)
   y_centro = int(y_centro)

   print("\n### RESULTADOS ###")

   # Inicializo as variáveis de trabalho
   x_ponto = 0
   y_ponto = raio

   pontos = [] # Declaro uma lista que armazenará tuplas referentes aos pontos calculados

   # Cálculo do parâmetro de decisão
   p = 1 - raio

   pontos.extend(pontos_octantes(x_ponto, y_ponto)) # Adiciono o primeiro ponto à lista
      
   # Cálculo dos próximos pontos
   while x_ponto < y_ponto: # Repete-se os passos enquanto x for menor que y
      x_ponto += 1 # Incrementa-se X

      if p < 0:
         y_ponto = y_ponto # Instrução desnecessária, mas apenas para explicitar que y_ponto permanece igual
         p = p + 2 * x_ponto + 1 # O parâmetro de decisão vai ser atualizado
      else:
         y_ponto -= 1
         p = p + 2 * x_ponto + 1 - 2 * y_ponto # Atualizo o valor do parâmetro de decisão
      
      pontos.extend(pontos_octantes(x_ponto, y_ponto)) # Adição dos pontos à lista

   # Impressão dos pontos calculados
   print("Pontos calculados pelo Algoritmo de Bresenham para Circunferência:")
   print(pontos)

   # Aplicação da translação. Estudamos que isso é necessário caso a circunferência não esteja centrada no ponto (0,0)
   pontos = [(x_ponto+x_centro, y_ponto+y_centro) for x_ponto, y_ponto in pontos]

   # Impressão dos pontos calculados
   x,y = zip(*pontos) # Aqui eu separo os valores de x e y que estão armazenados em uma lista de tuplas para que a plotagem possa ser feita

   plt.title("Algoritmo de Bresenham para Circunferência")
   plt.xlabel("Eixo X")
   plt.ylabel("Eixo Y")
   circunferencia = plt.Circle((x_centro, y_centro), raio, color='blue', fill=False, linestyle='-', linewidth=1, label='Circunferência original') # Realizo aqui o plota da circunferência
   plt.gca().add_patch(circunferencia)   
   plt.grid(True, linestyle='--', linewidth=0.5)
   plt.gca().set_axisbelow(True)
   plt.scatter(x, y, label='Pontos calculados', color='black', zorder=5) # Aqui eu faço o plot dos pontos calculados anteriomente, utilizei o 'zorder' para que os pontos não fiquem abaixo da linha
   plt.legend()
   plt.show()

   print("\n##################")   


if __name__ == "__main__":
   main()