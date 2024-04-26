import sys

def arithmetic_arranger(problems, show_answers=False):
    #Chequeamos que no sean más de 5 problemas
    if len(problems)>5:
        return 'Error: Too many problems.'
        
    #Defino strings vacíos para manipular la información en lineas
    primera = ""
    segunda = ""
    linea = ""
    resultadosstr = ""

    #Para cada problema tomo sus componenetes (primer numero, operador, segundo numero)
    for op in problems:
        n1 = op.split(' ')[0]
        n2 = op.split(' ')[2]
        operator = op.split(' ')[1]
        #Defino el largo maximo como del numero mas largo
        length = max(len(n1), len(n2))
        #Defino el ancho de la ecuacion usando el numero mas largo y sabiendo que debe haber un espacio entre el numero mas largo y el operador, sin importar la ubicacion del numero.
        width = length + 2
        
        #Reviso el largo de los numeros
        if len(n1) > 4 or len(n2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            

        #Reviso que sean numeros
        if not n1.isdigit() or not n2.isdigit():
            return 'Error: Numbers must only contain digits.'
            

        #Si el operador es positivo
        if operator not in '+-':
            return "Error: Operator must be '+' or '-'."
        else:   
            if operator == '+':
                result = int(n1) + int(n2)
                lres = len(str(result))
                #Definimos el caso de "la ultima cuenta"
                if op != problems[-1]:
                    primera += n1.rjust(width) + ' '*4
                    segunda += operator + ' ' + n2.rjust(length) + ' '*4
                    resultadosstr += str(result).rjust(width) + ' '*4
                    linea += '-' * width + ' '* 4
                else:
                    primera += n1.rjust(width)
                    segunda += operator + ' ' + n2.rjust(length)
                    resultadosstr += str(result).rjust(width)
                    linea += '-' * width
            #Si el operador es negativo
            elif operator == '-':
                result = int(n1) - int(n2)
                lres = len(str(result))
                #Definimos el caso de "la ultima cuenta"
                if op != problems[-1]:
                    primera += n1.rjust(width) + ' '*4
                    segunda += operator + ' ' + n2.rjust(length) + ' '*4
                    resultadosstr += str(result).rjust(width) + ' '*4
                    linea += '-' * width + ' '* 4
                else:
                    primera += n1.rjust(width)
                    segunda += operator + ' ' + n2.rjust(length)
                    resultadosstr += str(result).rjust(width)
                    linea += '-' * width
            
            
    problemasfor = formater(primera, segunda, linea, resultadosstr, show_answers)
    return problemasfor

def formater(primera, segunda, linea, resultadosstr, show_answers=False):
    chainstr = primera + '\n' + segunda + '\n' + linea
    if show_answers == True:
        chainstr += '\n' + resultadosstr
    
    return chainstr


print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
