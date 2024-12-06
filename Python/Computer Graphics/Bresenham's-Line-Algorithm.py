import matplotlib.pyplot as plt

def main():
   print("\n### ALGORITMO DE BRESENHAM PARA RETAS ###\n")

   # Os valores devem ser informados separados por espaço
   x_inicial, y_inicial= (input("Informe os valores de x e y iniciais: ").split(" "))
   x_final, y_final = (input("Informe os valores de x e y finais: ").split(" "))

   # Conversão dos valores informados para o tipo inteiro
   x_inicial = int(x_inicial)
   y_inicial = int(y_inicial)

   x_final = int(x_final)
   y_final = int(y_final)

   print("\n### RESULTADOS ###")
   # Calculo do delta x e delta y
   delta_x = abs(x_final - x_inicial)
   delta_y = abs(y_final - y_inicial)

   print(f"\nDelta x: {delta_x}")
   print(f"\nDelta y: {delta_y}")

   # Cálculo do coeficiente angular
   m = delta_y / delta_x

   print(f"Coeficiente angular = {m}")

   # Inicializo as variáveis de trabalho
   x_ponto = x_inicial
   y_ponto = y_inicial

   pontos = [] # Declaro uma lista que armazenará tuplas referentes aos pontos calculados

   # Cálculo do parâmetro de decisão
   p = 2 * delta_y - delta_x

   pontos.append((x_ponto, y_ponto)) # Adiciono o primeiro ponto à lista
   
   # Cálculo dos próximos pontos
   while x_ponto < x_final or y_ponto < y_final: # Repete-se os passos até que os ponto (x_final,	y_final)	sejam	alcançados

      if p < 0:
         x_ponto += 1; # Incremento o x
         y_ponto = y_ponto # Instrução desnecessária, mas apenas para explicitar que y_ponto permanece igual
         p = p + 2 * delta_y # O parâmetro de decisão vai ser atualizado
      else:
         x_ponto += 1 # Incremento o x
         if y_inicial > y_final:
            y_ponto -= 1
         else:
            y_ponto += 1 # Incremento o y também
         p = p + (2 * delta_y) - (2 * delta_x) # Atualizo o valor do parâmetro de decisão
      
      pontos.append((x_ponto, y_ponto)) # Adição dos pontos à lista

   # Impressão dos pontos calculados
   print("Pontos calculados pelo Algoritmo de Bresenham para Retas:")
   print(pontos)

   # Impressão dos pontos calculados
   x,y = zip(*pontos) # Aqui eu separo os valores de x e y que estão armazenados em uma lista de tuplas para que a plotagem possa ser feita

   plt.title("Algoritmo de Bresenham para Retas")
   plt.xlabel("Eixo X")
   plt.ylabel("Eixo Y")
   plt.grid(True, linestyle='--', linewidth=0.5)
   plt.gca().set_axisbelow(True)
   plt.plot([x_inicial, x_final], [y_inicial, y_final], label='Segmento de reta original') # Aqui eu ploto o segmento de reta original
   plt.scatter(x, y, label='Pontos calculados', color='black', zorder=5) # Aqui eu faço o plot dos pontos calculados anteriomente, utilizei o 'zorder' para que os pontos não fiquem abaixo da linha
   plt.legend()
   plt.show()

   print("\n##################")   


if __name__ == "__main__":
   main()