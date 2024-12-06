import matplotlib.pyplot as plt

def main():
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
   print(f"Delta y: {delta_y}")

   # Cálculo dos steps (passos)
   steps = max(delta_x, delta_y)
   print(f"Quantidade de steps: {steps}")

   # Cálculo do incremento de x e y
   x_inc = delta_x / steps
   y_inc = delta_y / steps

   # Cálculo dos pontos
   pontos = []
   
   pontos.append((x_inicial, y_inicial))

   x_pontos = x_inicial
   y_pontos = y_inicial

   for i in range(steps):
      x_pontos += x_inc
      y_pontos += y_inc
      pontos.append((round(x_pontos),(round(y_pontos))))
   
   print("\nPontos calculados:")
   print(pontos)

   x,y = zip(*pontos)

   plt.title("Algoritmo DDA")
   plt.xlabel("Eixo X")
   plt.ylabel("Eixo Y")
   plt.grid(True, linestyle='--', which='both', linewidth=0.5)
   plt.gca().set_axisbelow(True)
   plt.plot([x_inicial,x_final], [y_inicial, y_final], label='Segmento de reta')
   plt.scatter(x,y, label='Pontos calculados', color='black', zorder=5)
   plt.legend()
   plt.show()

   print("\n##################")
if __name__ == "__main__":
   main()