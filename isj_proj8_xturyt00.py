def first_with_given_key(iterable, key=lambda value: value):
    it = iter(iterable)
    saved_keys = []
    while True:
        try:
            value = next(it)
            if key(value) not in saved_keys:
                saved_keys.append(key(value))
                yield value
        except StopIteration:
            break
