from converter import to_rgba


class Object:
    def __init__(self):
        self.voxels = [[[]]]
        self.name = ""
        self.author = ""
        self.description = ""
        self.time = 0
        self.s = [0, 0, 0]

    def load(self, file):
        text = file.read()
        lines = text.split("\n")
        palette: dict = {}
        block = ""
        x = y = z = -1


        for line in lines:
            line = line.split('#')[0].strip()
            seq = line.split(' ')

            if not line:
                nline = True
                continue
            if line[-1] == ':':
                block = line[:-1]
                continue
            if block == "meta":
                # Заносим метаданные в свойства объекта
                if seq[0] == 'n':
                    self.name = line[2:]
                elif seq[0] == 'a':
                    self.author = line[2:]
                elif seq[0] == 'd':
                    self.description = line[2:]
                elif seq[0] == 't':
                    self.time = float(line[2:])
                elif seq[0] == 's':
                    self.size = list(map(int, (seq[1], seq[2], seq[3])))

            elif block == "pal":
                # Создаём палитру цветов в ассоциации с символами
                palette[seq[0]] = to_rgba(map(float, (seq[1], seq[2], seq[3], seq[4])))

            elif block == "pic":
                # Заносим воксели в список voxels с учётом цвета rgba
                if nline:
                    z += 1
                    y = -1
                    self.voxels.append([])
                self.voxels[z].append([])
                y += 1
                for x in line:
                    self.voxels[z][y].append(palette.get(x, 0))

            nline = False




def main():
    from datetime import datetime
    obj = Object()
    with open("test_pics/super_cube.tvp", 'r') as f:
        obj.load(f)

    print("==", obj.name, "==")
    print("by", obj.author)
    print("Создано", datetime.utcfromtimestamp(obj.time).strftime('%Y.%m.%d, в %H:%M:%S'))
    print()
    print(obj.description)
    print()
    print()
    for z in obj.voxels:
        for y in z:
            print('   \t'.join(map(str, y)))

if __name__ == "__main__":
    main()
