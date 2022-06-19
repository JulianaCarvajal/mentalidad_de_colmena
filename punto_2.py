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

def codify(message):
    """Codify the message

    Args:
        message (str): Message to be codified

    Returns:
        str: Codified message
    """
    # Create a list with the numbers to be codified:
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # Create a list with the codified numbers:
    new_numbers = ['9', '8', '7', '6', '0', '4', '3', '2', '1', '5']
    codified_message = ''
    for letter in message:
        # Check if the letter is a number:
        if letter in numbers:
            # Get the index of the number:
            index = numbers.index(letter)
            # Add the codified number:
            codified_message += new_numbers[index]
        else:
            # If the letter is not a number, add it to the new message:
            codified_message += letter
    return codified_message

def decodify(message):
    """Decodify the message

    Args:
        message (str): Message to be decodified

    Returns:
        str: Decodified message
    """
    # Create a list with the numbers to be decodified:
    codified_numbers = ['9', '8', '7', '6', '0', '4', '3', '2', '1', '5']
    # Create a list with the decodified numbers:
    decodified_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    decodified_message = ''
    for letter in message:
        # Check if the letter is a number:
        if letter in codified_numbers:
            # Get the index of the number:
            index = codified_numbers.index(letter)
            # Add the decodified number:
            decodified_message += decodified_numbers[index]
        else:
            # If the letter is not a number, add it to the decodified message:
            decodified_message += letter
    return decodified_message

def menu():
    """Show the menu

    Returns:
        str: Menu
    """
    print('1. Codify a message')
    print('2. Decodify a message')
    print('3. Exit')
    return input('Enter your choice: ')

def main():
    """Main function"""
    while True:
        choice = menu()
        if choice == '1':
            message = input('Enter your message: ')
            print('Codified message: ' + codify(message))
        elif choice == '2':
            message = input('Enter your message: ')
            print('Decodified message: ' + decodify(message))
        elif choice == '3':
            break
        else:
            print('Invalid choice')

main()
