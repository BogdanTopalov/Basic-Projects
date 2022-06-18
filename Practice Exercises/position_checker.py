def check_position(pos):
    if pos.startswith('M'):
        return "\\t" + pos
    elif pos.startswith('D'):
        return "\\t\\t" + pos
    return pos


class LeafElement:

    def __init__(self, *args):
        self.position = check_position(args[0])

    def showDetails(self):
        print(self.position)


class CompositeElement:

    def __init__(self, *args):
        self.position = check_position(args[0])
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for c in self.children:
            c.showDetails()
