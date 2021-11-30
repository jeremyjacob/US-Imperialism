import re

new = []
with open("World - Copy.svg", "r") as file:
    data = file.readlines()
    for i, line in enumerate(data):
        if ("#7f7f85" in line.lower() or '"#e3f3f0"' in line.lower()
                or '"#000"' in line.lower() or '"#fff"' in line.lower()
                or '"#00abd4"' in line.lower()):
            new.append(line)
            continue
        newline = re.sub('="#......"',
                         '="#e40000"',
                         str(line),
                         flags=re.IGNORECASE).lower()
        newline = newline.replace('"#7f7f85"', '"#fff"')
        newline = newline.replace('"#e3f3f0"', '"#111111"')
        new.append(newline)

with open("World.svg", "w") as file:
    file.writelines(new)
