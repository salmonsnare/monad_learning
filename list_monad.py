import itertools

def identity(x):
    """
    恒等射
    """
    return x

def eta(x, mode):
    """
    リスト x の要素からシングルトンリストのリストをつくる操作。
    mode を identity の前に適用するならば first, 
    identity の後に適用するならば second とする。
    """
    if mode == "first":
        return [ [item] for item in x ]
    elif mode == "second":
        return [x]

def mu(x, mode):
    """
    リストのリストからリストをつくる操作。
    """
    if mode == "first":
        return [list(itertools.chain.from_iterable(item)) for item in x]
    elif mode == "second":
        return list(itertools.chain.from_iterable(x))

def main():
    x = ['p', 'q', 'r']

    print(identity(eta(x, "first")))
    print(mu(identity(eta(x, "first")), "second"))
    print(x == mu(identity(eta(x, "first")), "second"))

    print(eta(identity(x), "second"))
    print(mu(eta(identity(x), "second"), "second"))
    print(x == mu(eta(identity(x), "second"), "second"))

    y = [
            [
                ['p', 'q'], ['q', 'r']
            ], 
            [
                ['r', 'p'], ['p', 'q', 'r']
            ], 
        ]

    print(mu(identity(y), "second"))
    print(mu(mu(identity(y), "second"), "second"))

    print(identity(mu(y, "first")))
    print(mu(identity(mu(y, "first")), "second"))

    print(mu(mu(identity(y), "second"), "second") == mu(identity(mu(y, "first")), "second"))

if __name__ == "__main__":
    main()
