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


def left_join(h1, h2):

    for bucket in h1.map:

      if bucket:

        for pair in bucket:
            
            if h2.contains(pair[0]):
                pair.append(h2.get(pair[0]))

            if not h2.contains(pair[0]):
                pair.append('None')

    return h1.map


if __name__ == "__main__":
    h1 = HashMap(5)
    h1.add('fond', 'enamored')
    h1.add('wrath', 'anger')
    h1.add('diligent', 'employed')
    h1.add('outift', 'garb')
    h1.add('guide', 'usher')
    h2 = HashMap(5)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')   
    print(left_join(h1, h2))