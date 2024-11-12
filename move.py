import rodi
import time

# Crear una instancia del robot RoDi
robot = rodi.RoDI(ip='192.168.4.1', port=1234)

# Función para detectar y evitar obstáculos
def detecta_obstáculos():
    global robot  
    try:
        while True:
            # Distancia del sensor de proximidad 
            # distance = robot.get_sonar()  # Comentado
            distance = 10  # Valor ficticio para prueba
            
            # Si el objeto está a menos de 5 cm, evitar el obstáculo
            if distance <= 5:
                print("Objeto detectado. Evitando...")
                robot.move_backward()  
                robot.move_left()     
                time.sleep(1)           
            else:
                # Si no hay ningún obstáculo, continuar
                print("Camino despejado. Avanzando...")
                robot.move_forward()
              
    except KeyboardInterrupt:
        print("Programa detenido por el usuario.")
        robot.move_stop()  

# Ejecutar la función de detección de obstáculos
detecta_obstáculos()