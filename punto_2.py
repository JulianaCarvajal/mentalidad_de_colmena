"""En un episodio de CSI un capo de la mafia diseño un interesante método para evitar que en sus mensajes
descubrieran los números telefónicos, las direcciones y los valores reales de sus transacciones.
El método se llamaba Saltando al 5. Es una estrategia simple e ingeniosa, cada digito es cambiado
por el opuesto del teclado telefónico saltando al número 5, como lo muestra la siguiente figura:

Como lo muestra la figura:
    • del 1 se salta al 9 y del 9 al 1 (por encima del 5).
    • del 2 se salta al 8 y del 8 al 2 (por encima del 5).
    • del 3 se salta al 7 y del 7 al 3 (por encima del 5).
    • del 4 se salta al 6 y del 6 al 4 (por encima del 5).
    • del 5 se salta al 0 y del 0 al 5.

Así cuando se pasaba un mensaje primero se codificaban todos los números en él de acuerdo con los saltos.

Por ejemplo, si el mensaje es: “Llamar después de las 9:54 al teléfono 3122345676”,
el mensaje codificado sería: “Llamar después de la 1:06 al teléfono 7988760434”.
Lo que debes haces es implementar una función que codifique y otra que decodifique
mensajes utilizando la estrategia Saltando al 5. Así que muestra un menú con las opciones.

"""