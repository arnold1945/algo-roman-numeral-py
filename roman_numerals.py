def to_roman(num):
    
    output = ''
    roman_dict = {
        'I' : 1,
        'IV' : 4,
        'V' : 5,
        'IX': 9,
        'X' : 10,
        'XIV' : 14,
        'XLIV' : 44,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'CMXLIV' : 944,
        'M' : 1000
        }
    

    
    roman_list = ['M','CMXLIV',  'D', 'C', 'L','XLIV','XIV', 'X','IX', 'V','IV', 'I']

        
    
    for item in roman_list:
        while num >= roman_dict[item]:
        
            output = output + item
            num = num - roman_dict[item]

            

    return output
    
            



    
    