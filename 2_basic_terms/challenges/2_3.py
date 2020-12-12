name = input("Hva er navnet ditt? ").lower()

reverse_name = name[::-1]

reverse_name = reverse_name[0].upper() + reverse_name[1::1]

print(F"Navnet ditt baklengs er {reverse_name}")