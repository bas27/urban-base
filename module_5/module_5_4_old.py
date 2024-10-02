class Building:
    total = 0

    def __init__(self):
        Building.total += 1
        self.name = "Building " + str(Building.total)


for i in range(40):
    build_i = Building()
    print(f"Имя объекта: {build_i.name}, Total: {build_i.total}")
