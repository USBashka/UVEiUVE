def to_rgba(color: list):
    return list(map(lambda x: int(255*x), color))


def main():
    print(to_rgba((1, 1, 1, 1)))
    print(to_rgba((0, 0, 0, 0)))
    print(to_rgba((0.1432, 0.9999, 1, 0.125)))

if __name__ == "__main__":
    main()
