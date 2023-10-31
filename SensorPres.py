from gpiozero import MotionSensor, LED              #importa os objetos LED e MotionSensor da gpiozero

sensor = MotionSensor(19, threshold = .6)           #cria objeto MotionSensor, declarando o pino 19 (BCM) como entrada binária e estabelecendo o limiar do sensor em 60%
led = LED(12)                                       #cria objeto LED, delcarando o pino 12 (BCM) como saída

while True:                                         #início da rotina
    sensor.wait_for_no_motion()                     #essa função aguarda não haver sinal superior ao limiar no sensor de presença
    print("*Dorme tranquilamente\n")                #mensagem que é printada quando não há sinal
    led.off()                                       #desliga o led
    
    sensor.wait_for_motion()                        #essa função aguarda haver sinal superior ao limiar no sensor de presença, ou seja, a presença de alguma fonte de infravermelho
    led.on()                                        #liga o led
    x = input("Quem tá aí?\n")                      #requisita uma resposta
    if x == "sou eu":                               #caso a resposta esteja correta
        print("Ah bom\n")                           #essa outra mensagem é printada
        led.off()                                   #e o led é desligado
    


try:
	while True:
		pass
except KeyboardInterrupt:
    sensor.close()                                           #limpesa das atribuições de GPIO com a interrupção do programa pelo teclado