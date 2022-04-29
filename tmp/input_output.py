import matematicka_knihovna
import re

def parse(line):
    change = re.findall(r'log[0-9]+|log /[0-9]+', line) + re.findall(r'log/[0-9]+', line)
    for item in change:
        line = re.sub(item, item+"|", line)
    line = list(line)
    result = ""
    for character in line:
        if character==" ":
            continue
        if character.isdigit():
            result+=str(character)
        
        elif character=="." or character=="^" or character=="!" or character=="√" or character=="l" or character=="o" or character=="g" or character=="|" or character=="/":
            result+=str(character)
        else:
            result+=" "+ str(character) + " "
    while "  " in result:
        result= result.replace("  ", " ")
    if re.match(r' -', result):
        result = "/" + result[3:]
    if re.match(r'//', result):
        result = result[2:]
    result = result.split()
    return result
    
def check_brackets (line):
    count=0
    for sign in line:
        if sign == "(":
            count+=1
        if sign == ")":
            count-=1
            if count<0:
                return 1
    if count==0: return 0
    else: return 1

def check_exp(result):
    for item in range(len(result)):
        search_exp = re.findall(r'\^', result[item])
        if search_exp:
            exp = re.split(r'\^', result[item])
            if exp[0].isdigit():
                 x = int(exp[0])
            elif re.match(r'/', exp[0]):
                tmp_exp = exp[0]
                exp[0] = tmp_exp[1:]
                if exp[0].isdigit():
                    x = int("-" + exp[0])
                else:
                    x = float("-" + exp[0])
            else:
                x = float(exp[0])
            if exp[1].isdigit():
                 y = int(exp[1])
            elif re.match(r'/', exp[1]):
                tmp_exp = exp[1]
                exp[1] = tmp_exp[1:]
                if exp[1].isdigit():
                    y = int("-" + exp[1])
                else:
                    y = float("-" + exp[1])
            else:
                y = float(exp[1])
            result[item] = str(matematicka_knihovna.exponenta(x,y))
            if re.match(r'-', result[item]):
                tmp_exp = result[item]
                result[item] = "/" + tmp_exp[1:]
    return result

def check_fact(result):
    for item in range(len(result)):
        search_fact = re.findall(r'\!', result[item])
        if search_fact:
            fact = re.split(r'\!', result[item])
            if fact[0].isdigit():
                 x = int(fact[0])
                 result[item] = str(matematicka_knihovna.faktorial(x))
            elif re.match(r'/', fact[0]):
                tmp_fact = fact[0]
                fact[0] = tmp_fact[1:]
                if fact[0].isdigit():
                    x = int(fact[0])
                    result[item] = "/" + str(matematicka_knihovna.faktorial(x))
                else:
                    x = float(fact[0])
                    result[item] = "/" + str(matematicka_knihovna.faktorial(x))
            else:
                x = float(fact[0])
                result[item] = str(matematicka_knihovna.faktorial(x))
    return result
    
def check_kor(result):
    for item in range(len(result)):
        search_kor = re.findall(r'√', result[item])
        if search_kor:
            kor = re.split(r'√', result[item])
            flag_min = 0
            if re.match(r'/', kor[0]):
                flag_min = 1
                tmp_kor = kor[0]
                kor[0] = tmp_kor[1:]
            if kor[0]:
                if kor[0].isdigit():
                    x = int(kor[0])
                else:
                    x = float(kor[0])
            else:
                x = int(2)
            
            if kor[1].isdigit():
                 y = int(kor[1])
            elif re.match(r'/', kor[1]):
                tmp_kor = kor[1]
                kor[1] = tmp_kor[1:]
                if kor[1].isdigit():
                    y = int("-" + kor[1])
                else:
                    y = float("-" + kor[1])
            else:
                y = float(kor[1])
            if flag_min:
                result[item] = "/" + str(matematicka_knihovna.koren(y, x))
            else:
                result[item] = str(matematicka_knihovna.koren(y, x))
            if re.match(r'-', result[item]):
                result[item] = "/" + result[item][1:]
            if re.match(r'/-', result[item]):
                result[item] = result[item][2:]
    return result
    
def check_log(result):
    for item in range(len(result)):
        search_log = re.findall(r'log', result[item])
        if search_log:
            loga = result[item]
            result[item] = loga[3:]
            loga = re.split(r'\|', result[item])
            if re.match(r'/', loga[0]):
                loga[0]=loga[0][1:]
                if loga[0].isdigit():
                    x = int("-" + loga[0])
                else:
                    x = float("-" + loga[0])
            else:
                if loga[0].isdigit():
                    x = int(loga[0])
                else:
                    x = float(loga[0])
            print(x)
            if re.match(r'/', loga[1]):
                loga[1]=loga[1][1:]
                if loga[1].isdigit():
                    y = int("-" + loga[1])
                else:
                    y = float("-" + loga[1])
            else:
                if loga[1].isdigit():
                    y = int(loga[1])
                else:
                    y = float(loga[1])
            result[item] = str(matematicka_knihovna.log(x,y))
            if re.match(r'-', result[item]):
                result[item] = "/" + result[item][1:]
    return result

def check_mul(result):
    result = " ".join(result)
    count_mul = re.findall(r'\*', result)
    count_mul = len(count_mul)
    result = parse(result)
    while count_mul>0:
        for item in range(len(result)):
            if result[item]=="*":
                flag_min_x=0
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.umnoz(x,y))
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_mul-=1
                result = result[:item-1] + result[item+1:]
                break
    return result
    
def check_div(result):
    result = " ".join(result)
    count_div = re.findall(r'÷', result)
    count_div = len(count_div)
    result = parse(result)
    while count_div>0:
        for item in range(len(result)):
            if result[item]=="÷":
                flag_min_x=0
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.podeli(x,y))
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_div-=1
                result = result[:item-1] + result[item+1:]
                break
    return result

def check_plus(result):
    result = " ".join(result)
    count_plus = re.findall(r'\+', result)
    count_plus = len(count_plus)
    result = parse(result)
    while count_plus>0:
        for item in range(len(result)):
            if result[item]=="+":
                flag_min_x=0
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.plus(x,y))
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_plus-=1
                result = result[:item-1] + result[item+1:]
                break
    return result

def check_minus(result):
    result = " ".join(result)
    count_min = re.findall(r'-', result)
    count_min = len(count_min)
    result = parse(result)
    while count_min>0:
        for item in range(len(result)):
            if result[item]=="-":
                flag_min_x=0
                flag_min_y=0
                if re.match(r'/', result[item-1]):
                    flag_min_x = 1
                    result[item-1] = result[item-1][1:]
                if result[item-1].isdigit():
                    if flag_min_x:
                        x = int("-" + result[item-1])
                    else:
                        x = int(result[item-1])
                else:
                    if flag_min_x:
                        x = float("-" + result[item-1])
                    else:
                        x = float(result[item-1])
                if re.match(r'/', result[item+1]):
                    flag_min_y = 1
                    result[item+1] = result[item+1][1:]
                if result[item+1].isdigit():
                    if flag_min_y:
                        y = int("-" + result[item+1])
                    else:
                        y = int(result[item+1])
                else:
                    if flag_min_y:
                        y = float("-" + result[item+1])
                    else:
                        y = float(result[item+1])
                result[item+1] = str(matematicka_knihovna.minus(x,y))
                if re.match(r'-', result[item+1]):
                    result[item+1] = "/" + result[item+1][1:]
                count_min-=1
                result = result[:item-1] + result[item+1:]
                break
    return result

def math_work (line):
    result = parse(line)
    result = check_exp(result)
    result = check_fact(result)
    result = check_kor(result)
    result = check_log(result)
    result = check_mul(result)
    result = check_div(result)
    result = check_plus(result)
    result = check_minus(result)
    result = " ".join(result)
    return result
    
def brackets(calculation, br):
    left=0
    right=0
    while br>0:
        for item in range(len(calculation)):
             if calculation[item]==")":
                right=item
                break
        for item in range(len(calculation[:right])):
             if calculation[item]=="(":
                left=item
        tmp_line=calculation[left+1:right]
        calculation = calculation[:left] + " " + str(math_work(tmp_line)) + " " + calculation[right+1:]
        br-=1
    return calculation