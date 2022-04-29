# Python projects
Learn more about python course at VUT **[here](https://www.fit.vut.cz/study/course/244880/.cs)**

| Project # | Points |
| ------ | ------ |
| 1 | 5/5 |
| 2 | 5/5 |
| 3 | 5/5 |
| 4 | 5/5 |
| 5 | -/5 |
| 6 | -/5 |
| 7 | -/5 |
| 8 | -/5 |

## Project #1
Write a function that converts camelCase to a snake_case with regex
```python
camel_to_snake_case('camelCaseNameAllowed')
'camel_case_name_allowed'

camel_to_snake_case('longVATNumber')
'long_vat_number'
```
Write a function that returns a list of names not preceded by [Pp]rof./[Dd]oc. and 
followed by ', Ph.D.'
```python
not_both_titles('doc. Josef Tyl, Rudolf Srp, Ph.D., Pavel Vlk, doc. RNDr. Petr Berka, Ph.D., Jan Hora')
['doc. Josef Tyl', 'Rudolf Srp, Ph.D.', 'Pavel Vlk', 'Jan Hora']
```

## Project #2
Write a function that replaces y/i, removes spaces, returns reversed
```python
she_says_he_says('ma rymu')
'umiram'
```
Partitions the input string to (an optional) title, ': ', and the hymn,
takes a sublist starting from the first string, skipping always two 
other strings, and ending 3 strings from the end, returns the result 
as a string with ', ' as a separator
```python
solfege('Hymn of St. John: Ut queant laxis re sonare fibris mi ra gestorum fa muli tuorum sol ve polluti la bii reatum Sancte Iohannes')
'Ut, re, mi, fa, sol, la'

solfege('Ut queant laxis re sonare fibris mi ra gestorum fa muli tuorum sol ve polluti la bii reatum Sancte Iohannes')
'Ut, re, mi, fa, sol, la'
```

## Project #3
Write a function that returns 0 if there is the same number of even numbers and odd numbers
in the input list of ints, or there are only odd or only even numbers.
Returns the first odd number in the input list if the list has more even
numbers. Returns the first even number in the input list if the list has more odd 
numbers.
```python
first_odd_or_even([2,4,2,3,6])
3

first_odd_or_even([3,5,4])
4

first_odd_or_even([2,4,3,5])
0

first_odd_or_even([2,4])
0

first_odd_or_even([3])
0
```
Write a function that returns a list of pilot alpha codes corresponding to the input word
```python
pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

to_pilot_alpha('Smrz')
['Sierra', 'Mike', 'Romeo', 'Zulu']
```

## Project #4
Write a function that generates all permutations of all substrings of the input string
```python
match_permutations_substrings('okna', ['a', 'z', 'v', 'o', 'k', 'ok', 'ano', 'no', 'hlava', 'oko', 'noky', 'nok', 'on', 'ona', 'ony']) == {'ona', 'a', 'ok', 'o', 'nok', 'no', 'ano', 'on', 'k'}
True

match_permutations_substrings('opak', ['ok', 'pak', 'pako', 'ano', 'noha', 'oka', 'kap', 'kopa', 'kopat', 'ona', 'okap']) == {'kopa', 'kap', 'pako', 'ok', 'pak', 'okap', 'oka' }
True
```
Write a function that returns the input sequence unified and sorted (according to the values)
```python
uniq_srt([3, 3, 5, 3, 4, 2, 4])
[2, 3, 4, 5]

uniq_srt('abrakadabra')
['a', 'b', 'd', 'k', 'r']
```

Write a function that returns the input sequence, items ordered by the order of their
first appearance
```python
uniq_orig_order([3, 3, 5, 3, 4, 2, 4])
[3, 5, 4, 2]

uniq_orig_order('abrakadabra')
['a', 'b', 'r', 'k', 'd']
```
## Project #5

Definujte funkci gen_quiz, která bude moci být volána se 4 parametry:
qpool - seznam dvojic otázka a seznam odpovědí
libovolný počet indexů do seznamu qpool
altcodes - sekvence, přes kterou lze projít konstrukcí for a která vrací řetězce, jež se mají ve výsledku předřadit (spolu s ': ') před každou z odpovědí 
quiz - vstupní podoba kvízu ve formě seznamu dvojic otázka a seznam formátovaných odpovědí.

Pokud bude některý z indexů do seznamu qpool mimo rozsah, nebo nastane jiná chyba při zpracování konkrétního indexu, má se vypsat:
`Ignoring index <číslo> - <text výjimky>`
(poněkud nesmyslně na standardní výstup, nikoliv na standardní chybový výstup, aby fungoval doctest)

Pokud bude sekvence altcodes kratší než seznam možných odpovědí v některém ze seznamů, dá se do výsledného kvízu pouze daný počet (lze využít konstrukci zip(altcodes, answers)). Defaultně jsou odpovědi označovány písmeny a je maximálně 6 možných odpovědí, tedy altcodes = `'ABCDEF'`)

Pokud není zadána vstupní podoba kvízu, vytvoří se nový kvíz s položkami podle definovaných indexů. Defaultní hodnota je tedy prázdný kvíz.

```python
test_qpool7 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
gen_quiz(test_qpool7, 0, 4, 2, altcodes = ['101','201']) 
Ignoring index 4 - list index out of range
[('Question1', ['101: Answer1', '201: Answer2']), ('Question3', ['101: Answer1', '201: Answer2'])]
```

## Project #6

Do souboru, nazvaného podle konvence isj_proj6_xnovak00.py, implementujte třídu Polynomial, která bude pracovat s polynomy reprezentovanými pomocí seznamů. Například **2x^3 - 3x + 1** bude  reprezentováno jako `[1,-3,0,2]` (seznam začíná nejnižším řádem, i když se polynomy většinou zapisují opačně).

Instance třídy bude možné vytvářet několika různými způsoby:
```python
pol1 = Polynomial([1,-3,0,2])
pol2 = Polynomial(1,-3,0,2)
pol3 = Polynomial(x0=1,x3=2,x1=-3)
```

Volání funkce print() vypíše polynom v obvyklém formátu:
```python
print(pol2)
"2x^3 - 3x + 1"
```

Bude možné porovnávat vektory porovnávat:
```python
pol1 == pol2
True
```

Polynomy bude možné sčítat a umocňovat nezápornými celými čísly:
```python
print(Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))
"2x^3 + x^2 - x + 1"
print(Polynomial(-1, 1) ** 2)
"x^2 - 2x  + 1"
```

## Project #7

Do souboru, nazvaného podle konvence isj_proj7_xnovak00.py, implementujte funkci (decorator factory) log_and_count, která umožní použití dekorátoru s určením jména key (klíče ve struktuře Counter), pod kterou má být volání dané funkce započítáno, nebo použije jako klíč následující jméno funkce. Druhým parametrem, který bude muset být zadán s klíčovým jménem counts, bude jméno struktury Counter, do níž má být počítání ukládáno. Mělo by tedy fungovat následující:

# Input
```python
import collections

my_counter = collections.Counter()

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)
```
# Output
```bash
called f1 with (2,) and {}
called f2 with (2,) and {'b': 4}
called f1 with () and {'a': 2, 'b': 4}
called f2 with (4,) and {}
called f2 with (5,) and {}
called f3 with (5,) and {}
called f3 with (5, 4) and {}
```
