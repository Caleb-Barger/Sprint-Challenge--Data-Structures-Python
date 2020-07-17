class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        # check len of array

        self.data.append(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            self.append = self._full_append

    def _full_append(self, item):
        self.data[self.cur]=item
        self.cur=(self.cur + 1) % self.capacity
        

    def get(self):
        return self.data


# rb = RingBuffer(5)
# rb.append('a')
# rb.append('b')
# rb.append('c')
# rb.append('d')
# rb.append('e')
# rb.append('f')
# print(rb.get())


