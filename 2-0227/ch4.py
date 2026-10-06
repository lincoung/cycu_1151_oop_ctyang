string1 = "I'm a lumberjack, and I'm okey"
string2 = "I sleep all night and I work all day"


def find_i_positions(text):
    positions = [index for index, char in enumerate(text) if char == 'I']
    return positions, len(positions)


positions1, count1 = find_i_positions(string1)
positions2, count2 = find_i_positions(string2)

print(f"string1 的 'I' 位置：{positions1}")
print(f"string1 的 'I' 數量：{count1}")
print(f"string2 的 'I' 位置：{positions2}")
print(f"string2 的 'I' 數量：{count2}")