class HashMap:

    def __init__(self, size):
        self.size = size
        self.bucket = [None] * self.size

    def __str__(self):
        return self.bucket

    def hash(self, key):
        hashed_chars = 0

        for char in str(key):
            hashed_chars += ord(char) * 599

        return hashed_chars % self.size

    def add(self, key, value):
        hash_key = self.hash(key)
        key_value = [key, value]

        if self.bucket[hash_key] is None:
            self.bucket[hash_key] = list([key_value])
            return True

        else:

            for pair in self.bucket[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True

            self.bucket[hash_key].append(key_value)
            return True

    def contains(self, key):
        hash_key = self.hash(key)

        if self.get(hash_key):
            return True

        return False

    def get(self, key):
        hash_key = self.hash(key)

        if self.bucket[hash_key] is not None:
            for pair in self.bucket[hash_key]:
                if pair[0] == key:
                    return pair[1]

        return None

    def print(self):
        if self.bucket is not None:
            for item in self.bucket:
                print(str(item))


if __name__ == "__main__":
    h = HashMap(20)
    h.add('foo', 420)
    h.add('bar', 69)
    h.add('foobar', 1986)
    h.add('hello world', 33)
    print(h.get('foo'))
    print(h.get('wadido'))
    print(h.contains('fire'))
    # print(h.print())