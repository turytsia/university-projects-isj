# Python projects
Learn more about python course at VUT **[here](https://www.fit.vut.cz/study/course/244880/.cs)**

| Project # | Points |
| ------ | ------ |
| 1 | 5/5 |
| 2 | 5/5 |
| 3 | 5/5 |
| 4 | 5/5 |
| 5 | 5/5 |
| 6 | 5/5 |
| 7 | 5/5 |
| 8 | 5/5 |

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

Definujte funkci gen_quiz, kter?? bude moci b??t vol??na se 4 parametry:
qpool - seznam dvojic ot??zka a seznam odpov??d??
libovoln?? po??et index?? do seznamu qpool
altcodes - sekvence, p??es kterou lze proj??t konstrukc?? for a kter?? vrac?? ??et??zce, je?? se maj?? ve v??sledku p??ed??adit (spolu s ': ') p??ed ka??dou z odpov??d?? 
quiz - vstupn?? podoba kv??zu ve form?? seznamu dvojic ot??zka a seznam form??tovan??ch odpov??d??.

Pokud bude n??kter?? z index?? do seznamu qpool mimo rozsah, nebo nastane jin?? chyba p??i zpracov??n?? konkr??tn??ho indexu, m?? se vypsat:
`Ignoring index <????slo> - <text v??jimky>`
(pon??kud nesmysln?? na standardn?? v??stup, nikoliv na standardn?? chybov?? v??stup, aby fungoval doctest)

Pokud bude sekvence altcodes krat???? ne?? seznam mo??n??ch odpov??d?? v n??kter??m ze seznam??, d?? se do v??sledn??ho kv??zu pouze dan?? po??et (lze vyu????t konstrukci zip(altcodes, answers)). Defaultn?? jsou odpov??di ozna??ov??ny p??smeny a je maxim??ln?? 6 mo??n??ch odpov??d??, tedy altcodes = `'ABCDEF'`)

Pokud nen?? zad??na vstupn?? podoba kv??zu, vytvo???? se nov?? kv??z s polo??kami podle definovan??ch index??. Defaultn?? hodnota je tedy pr??zdn?? kv??z.

```python
test_qpool7 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
gen_quiz(test_qpool7, 0, 4, 2, altcodes = ['101','201']) 
Ignoring index 4 - list index out of range
[('Question1', ['101: Answer1', '201: Answer2']), ('Question3', ['101: Answer1', '201: Answer2'])]
```

## Project #6

Do souboru, nazvan??ho podle konvence isj_proj6_xnovak00.py, implementujte t????du Polynomial, kter?? bude pracovat s polynomy reprezentovan??mi pomoc?? seznam??. Nap????klad **2x^3 - 3x + 1** bude  reprezentov??no jako `[1,-3,0,2]` (seznam za????n?? nejni??????m ????dem, i kdy?? se polynomy v??t??inou zapisuj?? opa??n??).

Instance t????dy bude mo??n?? vytv????et n??kolika r??zn??mi zp??soby:
```python
pol1 = Polynomial([1,-3,0,2])
pol2 = Polynomial(1,-3,0,2)
pol3 = Polynomial(x0=1,x3=2,x1=-3)
```

Vol??n?? funkce print() vyp????e polynom v obvykl??m form??tu:
```python
print(pol2)
"2x^3 - 3x + 1"
```

Bude mo??n?? porovn??vat vektory porovn??vat:
```python
pol1 == pol2
True
```

Polynomy bude mo??n?? s????tat a umoc??ovat nez??porn??mi cel??mi ????sly:
```python
print(Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))
"2x^3 + x^2 - x + 1"
print(Polynomial(-1, 1) ** 2)
"x^2 - 2x  + 1"
```

## Project #7

Do souboru, nazvan??ho podle konvence isj_proj7_xnovak00.py, implementujte funkci (decorator factory) log_and_count, kter?? umo??n?? pou??it?? dekor??toru s ur??en??m jm??na key (kl????e ve struktu??e Counter), pod kterou m?? b??t vol??n?? dan?? funkce zapo????t??no, nebo pou??ije jako kl???? n??sleduj??c?? jm??no funkce. Druh??m parametrem, kter?? bude muset b??t zad??n s kl????ov??m jm??nem counts, bude jm??no struktury Counter, do n???? m?? b??t po????t??n?? ukl??d??no. M??lo by tedy fungovat n??sleduj??c??:

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

## Project #8

Do souboru, nazvan??ho podle konvence isj_proj8_xnovak00.py, definujte gener??torovou funkci first_with_given_key, kter?? bude m??t 2 parametry - povinn?? parametr iterable, odpov??daj??c?? p??edan??mu iterovateln??mu objektu (m????e b??t i nekone??n??), a d??le nepovinn?? parametr key, odpov??daj??c?? funkci, kter?? p??i vol??n?? na polo??ce objektu iterable vr??t?? hodnotu kl????e, s defaultn?? hodnotou identick?? funkce (tedy vr??cen?? p????mo polo??ky, na kter?? je funkce zavol??na), implementovan?? pomoc?? konstrukce lambda. Funkce aplikuje kl???? na polo??ky objektu iterable a vyb??r?? (generuje) pouze ty, jejich?? kl???? se dosud nevyskytl. V p????pad?? pot??eby pamatovat si nehashovateln?? objekty pou??ijte funkci repr.
Nap????klad:

```python
print(tuple(first_with_given_key([[1],[2,3],[4],[5,6,7],[8,9]], key = len)))

([1], [2, 3], [5, 6, 7])
```
