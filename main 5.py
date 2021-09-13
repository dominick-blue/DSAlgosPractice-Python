init_key = int(input())

freq = float(init_key)
higher_key1 = freq * (1.05946309**1)
higher_key2 = freq * (1.05946309**2)
higher_key3 = freq * (1.05946309**3)
higher_key4 = freq * (1.05946309**4)

print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(freq, higher_key1, higher_key2, higher_key3, higher_key4))