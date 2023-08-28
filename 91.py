import time

def main():
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    
    tiempo_limite = horas * 3600 + minutos * 60 + segundos
    
    print("\nCronómetro iniciado:")
    tiempo_restante = tiempo_limite
    
    while tiempo_restante > 0:
        horas_restantes = tiempo_restante // 3600
        minutos_restantes = (tiempo_restante % 3600) // 60
        segundos_restantes = tiempo_restante % 60
        
        print(f"{horas_restantes:02d}:{minutos_restantes:02d}:{segundos_restantes:02d}", end="\r")
        time.sleep(1)
        
        tiempo_restante -= 1
    
    print("\nTiempo límite alcanzado.")

if __name__ == "__main__":
    main()
