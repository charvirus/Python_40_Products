def space_location(text):
    result = []
    if text:
        yield 0
    for index, letter in enumerate(address, 1):
        if letter == ' ':
            yield index


address = '우리는 이터레이터를 테스트 하고 있습니다.'
it = space_location(address)
print(next(it))
print(next(it))

result = list(space_location(address))
print(result)