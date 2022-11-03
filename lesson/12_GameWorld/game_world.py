objects= [[],[]]

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(o, depth):
    objects[depth] += o

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()