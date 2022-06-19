"""Ace quiere ser voluntario para viajar a K-Pax, para ello la Agencia Espacial Canadiense
requiere que llene un formulario que ayude a obtener más información de él y su familia.
Tu debes ayudar a Ace creando un programa para completar la información solicitada sin sobrescribir el archivo.
Ten presente que los datos con * son los más importantes, si uno de esos campos no se llena, no podrá ser admitido,
en caso de que el dato solicitado no sea importante, el programa deberá poner “unknown”.
"""

# Open and close the file:
with open('required_data.txt', 'r') as reader, open('filled_form.txt', 'w') as writer:

    print('Enter your personal data')
    # Iterating over each line in the file:
    for line in reader:
        # Select the lines on which information is to be filled in:
        if ':' in line:
            family_members = ['Mother', 'Father', 'Brother', 'Sister']
            cent = False
            for member in family_members:
                if member in line:
                    print(f'Enter your {member.lower()}\'s data:')
                    writer.write(line)
                    cent = True
            if cent == True:
                continue
            else:
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
                new_line = line.rstrip('\n') + ' ' + entry + '\n'
        # Write the same line if it is not a line to be filled in:               
        else:
            new_line = line
        # Write the information in the file:    
        writer.write(new_line)
    