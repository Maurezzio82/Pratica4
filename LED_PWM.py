import RPi.GPIO as GPIO                                        #importa RPi.GPIO, o pacote de mais baixo nível, se comparado ao gpiozero
from time import sleep                                         #importa a função de sleep, opera como delay

GPIO.setmode(GPIO.BCM)                                          #estabelece o setmode baseado no chip, e não na placa
GPIO.setwarnings(False)                                         #desliga avisos

GPIO.setup(21, GPIO.OUT)                                        #declara o pino 21 como saída

pwm = GPIO.PWM(21, 100)                                         #cria objeto PWM. Isso estabelece um sinal de PWM de 100 Hz no pino 21
pwm.start(0)                                                    #inicializa o PWM

while True:                                                     #início do laço da rotina
    duty_cycle = int(input("Digite o DutyCycle:"))              #pede o novo duty cycle
    pwm.ChangeDutyCycle(duty_cycle)                             #atualiza o duty cycle baseado na entrada fornecida

try:
	while True:
		pass
except KeyboardInterrupt:
    GPIO.cleanup()                                           #limpesa das atribuições de GPIO com a interrupção do programa pelo teclado