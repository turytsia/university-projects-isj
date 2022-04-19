def gen_quiz(qpool,*indexes,altcodes = 'ABCDEF',quiz=None):
    altcodes = list(altcodes)

    result = quiz if quiz is not None else []
    
    for index in indexes:
        try:
            result.append((qpool[index][0],[f"{altcodes[n]}: {qpool[index][1][n]}" for n in range(len(altcodes)) if n < len(qpool[index][1])]))
        except IndexError as e:
            print(f"Ignoring index {index} - {e}")
    return result
