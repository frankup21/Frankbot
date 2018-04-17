import random
emoji = ["\U00002764", "\U0001F352", "\U0001F4B0", "\U0001F33B"]
c = [ [0, 1, 2, 3], [3, 0, 1, 2], [2, 3, 0, 1], [1, 2, 3, 0] ]
def slotmachine():
    col1 = random.randint(0, 3)
    col2 = random.randint(0, 3)
    col3 = random.randint(0, 3)

    output = '''
+--------------------+
|  {}  |  {}  |  {}  |
+------+------+------+
|  {}  |  {}  |  {}  |
+------+------+------+
|  {}  |  {}  |  {}  |
+--------------------+
|  {}  |  {}  |  {}  |
+--------------------+
    '''.format(emoji[c[col1][0]], emoji[c[col2][0]], emoji[c[col3][0]],
    emoji[c[col1][1]], emoji[c[col2][1]], emoji[c[col3][1]],
    emoji[c[col1][2]], emoji[c[col2][2]], emoji[c[col3][2]],
    emoji[c[col1][3]], emoji[c[col2][3]], emoji[c[col3][3]])

    return output
