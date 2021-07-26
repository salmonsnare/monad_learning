import itertools

def identity(x):
    """
    恒等射
    """
    return x


def eta(x, mode):
    """
    集合 x の要素からシングルトンセットをつくる操作。
    mode を identity の前に適用するならば first, 
    identity の後に適用するならば second とする。
    """
    if mode == "first":
        return [ list(item) for item in x ]
    elif mode == "second":
        return [x]


def mu(x, mode):
    """
    集合の集合から要素である集合について和集合をつくる操作。
    """
    ret = []
    if mode == "first":
        ret = [set_(list(itertools.chain.from_iterable(item))) for item in x]
    elif mode == "second":
        ret = list(itertools.chain.from_iterable(x))
    return set_(ret)


def set_(seq):
    # 参考: https://note.nkmk.me/python-list-unique-duplicate/
    seen = []
    return sorted([x for x in seq if x not in seen and not seen.append(x)])

def main():
    x = ['a', 'b']

    print(identity(eta(x, "first")))
    print(mu(identity(eta(x, "first")), "second"))
    print(x == mu(identity(eta(x, "first")), "second"))

    print(eta(identity(x), "second"))
    print(mu(eta(identity(x), "second"), "second"))
    print(x == mu(eta(identity(x), "second"), "second"))

    y = [
            [
                [], ['a']
            ], 
            [
                ['b'], ['a','b']
            ], 
    ]

    print(mu(identity(y), "second"))
    print(mu(mu(identity(y), "second"), "second"))

    print(identity(mu(y, "first")))
    
    print(mu(identity(mu(y, "first")), "second"))
    print(mu(mu(identity(y), "second"), "second") == mu(identity(mu(y, "first")), "second"))


if __name__ == "__main__":
    main()
