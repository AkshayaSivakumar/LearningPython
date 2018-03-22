import difflib

with open('F:\\Personal\\file1.txt', 'r') as text1:
    with open('F:\\Personal\\file2.txt', 'r') as text2:
        d = difflib.Differ()
        diff = list(d.compare(text1.readlines(), text2.readlines()))
        with open('diff.txt', 'w') as diff_file:
            _diff = ''.join(diff)
            diff_file.write(_diff)