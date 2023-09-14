class utils:
    def reversed(n):
        rev = 0
        
        while(n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10
        return rev

    def formatter(number):
        binary_format = bin(number)[2:]  
        octal_format = oct(number)[2:]  
        
        return binary_format, octal_format