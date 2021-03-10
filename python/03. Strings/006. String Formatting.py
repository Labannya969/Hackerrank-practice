def print_formatted(number):
    for i in range(1,n+1):
        l=len(str(bin(n)[2: ]))
        print(str(i).rjust(l) + ' ' + oct(i)[2:].rjust(l) + ' ' + hex(i)[2:].upper().rjust(l) + ' ' + bin(i)[2:].rjust(l))

        
        
