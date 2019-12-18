from stacks_and_queues import Queue

class AnimalShelter:
    """Class with dog queue and cat queue"""
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def fifo_enqueue(self, animal):
        """Method that takes in an animal as an argument, and adds animal if cat or dog, to it's respective queues."""
        if animal == 'cat': 
            self.cat.enqueue(animal)
        if animal == 'dog':
            self.dog.enqueue(animal)

    def fifo_dequeue(self, preference):
        """Method that takes in a preference, where a cat or dog is selected, removed their respective queues, and returned"""
        if preference == 'cat':
            return self.cat.dequeue()
        if preference == 'dog':
            return self.dog.dequeue()
        else:
            return null

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.fifo_enqueue({'cat': 'Garfield'})
    shelter.fifo_enqueue({'dog': 'Pluto'})
    # shelter.fifo_enqueue({'dog': 'Pluto'})
    # shelter.fifo_enqueue({'dog': 'Pluto'})
    # shelter.fifo_enqueue('dog')
    # print(shelter.fifo_dequeue('cat'))
    print(shelter.dog.queue_info())
    print(shelter.cat.queue_info())
