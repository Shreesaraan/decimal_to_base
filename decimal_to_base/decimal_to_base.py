def decimal_to_base(decimal,base):
    if decimal==0:
        return 0
    number=''
    while decimal>0:
        reminder=decimal%base
        number=str(reminder)+number
        decimal//=base
    return number

decimal=int(input("Enter the Decimal : "))
base=int(input("Enter the Base : "))
print(decimal_to_base(decimal,base))