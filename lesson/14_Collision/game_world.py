
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[], []]

# collision information
# key 'boy:ball' string

collision_group = dict()

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            # 오브젝트를 충돌그룹에서도 지워야 한다.
            remove_collision_object(o)
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



def add_collision_pairs(a, b, group):
    if group not in collision_group:
        print('Add new group ', group)
        collision_group[group] = [ [], [] ] # list of list : list pair

    if a:
        if type(a) is list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)
    if b:
        if type(b) is list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)


def all_collision_pairs():
    for group, pairs in collision_group.items(): # key, value 를 둘 다 가져옴
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group


def remove_collision_object(o):
    for pairs in collision_group.values():#key는 필요없음
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

