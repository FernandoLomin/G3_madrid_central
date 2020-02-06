#!/usr/bin/env python
# -*- coding: latin-1 -*-

from datetime import datetime, timedelta
from threading import Thread
from time import sleep


class UpdateChecker(Thread):
    def __init__(self, delay, funcion):
        # El constructor recibe como par�metros:
        ## delay = tiempo de espera entre comprobaciones en segundos.
        ## funcion = funci�n a ejecutar.

        Thread.__init__(self)
        self._status = True
        self.delay = delay
        self.funcion = funcion

    def stop(self):
        self._status = False

    def get_status(self):
        return self._status

    def run(self):
        # # Pasamos el string a dato tipo datetime
        # hora_aux = datetime.strptime(self.hora, '%H:%M:%S')
        # Obtenemos la fecha y hora actuales.
        hora = datetime.now()
        # Comprobamos si la hora ya a pasado o no, si ha pasado sumamos una hora (hoy ya no se ejecutar�).

        print('Ejecuci�n autom�tica iniciada : Desde hilo')
        # print('Proxima ejecuci�n programada el {0} a las {1}'.format(hora.date(), hora.time()))

        # Iniciamos el ciclo:
        while self._status:
            # Esperamos x segundos para volver a ejecutar la comprobaci�n.
            nx = hora + timedelta(seconds=self.delay)
            print('Pr�xima ejecuci�n programada el {0} a las {1}'.format(hora.date(), nx))
            sleep(self.delay)
            # Comparamos la hora actual con la de ejecuci�n y ejecutamos o no la funci�n.
            self.funcion()

        # Si usamos el m�todo stop() salimos del ciclo y el hilo terminar�.
        else:
            print('Ejecuci�n autom�tica finalizada')
