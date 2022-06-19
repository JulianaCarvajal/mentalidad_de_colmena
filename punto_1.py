"""Ace quiere ser voluntario para viajar a K-Pax, para ello la Agencia Espacial Canadiense
requiere que llene un formulario que ayude a obtener más información de él y su familia.
Tu debes ayudar a Ace creando un programa para completar la información solicitada sin sobrescribir el archivo.
Ten presente que los datos con * son los más importantes, si uno de esos campos no se llena, no podrá ser admitido,
en caso de que el dato solicitado no sea importante, el programa deberá poner “unknown”.
"""

def family_members(line, writer):
    """Check if the line is a family member's line

    Args:
        line (str): current line in the file
        writer (file): file to write the information

    Returns:
        bool: sentinel
    """
    family_members = ['Mother', 'Father', 'Brother', 'Sister']
    sent = False
    for member in family_members:
        # Check if the line is a family member:
        if member in line:
            print(f'Enter your {member.lower()}\'s data: \n')
            # Write the same line in the file:
            writer.write(line)
            sent = True
    return sent

def fill_form(line):
    """Ask for the information and store it

    Args:
        line (str): Current line in the file

    Returns:
        str: Line to be written
    """
    if '*' in line:
        # Advise Ace to enter this information:
        print('The following information is mandatory')
        entry = ''
        while entry == '':
            # Ask for the information:
            entry = input(line)
            if entry == '':
                # Remember Ace that he needs to enter this information:
                print('I told you it was mandatory')
    else:
        # Ask for the information:
        entry = input(line)
        if entry == '':
            # Set the default value for the less important information:
            entry = 'unknown'
    return line.rstrip('\n') + ' ' + entry + '\n'

def main():
    """Main function"""
    # Open and close the file:
    with open('required_data.txt', 'r') as reader, open('filled_form.txt', 'w') as writer:

        print('Enter your personal data \n')
        # Iterating over each line in the file:
        for line in reader:
            # Select the lines on which information is to be filled in:
            if ':' in line:
                # Check if the line is a family member:
                sent = family_members(line, writer)
                # If there's a family member in the line, skip it:
                if sent == True:
                    continue
                else:
                    # If there's no family member in the line, ask for the information:
                    new_line = fill_form(line)
            # Write the same line if it is not a line to be filled in:               
            else:
                new_line = line
            # Write the information in the file:    
            writer.write(new_line)

main()