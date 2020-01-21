class HashMap:

    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size
        self.index = -1

    def __str__(self):
        """
        Method from HashMap that prints indices, keys, and values in map
        In: None
        Out: string
        """ 
        if self.map is not None:
            for item in self.map:
                self.index += 1
                print(f'{self.index}: {str(item)}')

    def hash(self, key):
        """
        Method from HashMap that takes in a key
        In: string
        Out: Integer
        """
        hashed_chars = 0

        for char in str(key):
            hashed_chars += ord(char) * 599

        return hashed_chars % self.size

    def add(self, key, value):
        """
        Method from HashMap that takes in a key and value
        In: string and integer
        Out: adds key and value to an index in the map
        """        
        hash_key = self.hash(key)
        key_value = [key, value]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            return True

        else:

            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True

            self.map[hash_key].append(key_value)
            return True

    def contains(self, key):
        """
        Method from HashMap that takes in a key
        In: string
        Out: boolean
        """        
        hash_key = self.hash(key)

        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return True

        return False

    def get(self, key):
        """
        Method from HashMap that takes in a key
        In: string
        Out: string - returns value from map or None if does not exist
        """
        hash_key = self.hash(key)

        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]

        return None


if __name__ == "__main__":
    h = HashMap(10)
    h.add('foo', 420)
    h.add('bar', 69)
    h.add('foobar', 1986)
    h.add('hello world', 33)
    print(h.get('foo'))
    print(h.get('wadido'))
    print(h.contains('fire'))
    print(h.contains('foo'))
    h.__str__()