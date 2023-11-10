waga = input('Podaj wagę: ')
wzrost = input('Podaj wzrost: ')
if 'g' in waga and 'k' not in waga:
    waga = float(waga.strip('g')) / 1000
else:
    waga = float(waga.strip('kg'))
if 'c' in wzrost:
    wzrost = float(wzrost.strip('cm')) / 100
else:
    wzrost = float(wzrost.strip('m'))
bmi = waga / (wzrost**2)
if bmi < 16.0:
    werdykt = 'wygłodzenie'
elif bmi < 17.0:
    werdykt = 'wychudzenie'
elif bmi < 18.5:
    werdykt = 'niedowaga'
elif bmi < 25.0:
    werdykt = 'OK'
elif bmi < 30.0:
    werdykt = 'nadwaga'
elif bmi < 35.0:
    werdykt = 'otyłość I stopnia'
elif bmi < 40.0:
    werdykt = 'otyłość II stopnia'
else:
    werdykt = 'otyłość III stopnia'
print(f'BMI wynosi: {bmi}, {werdykt}.')