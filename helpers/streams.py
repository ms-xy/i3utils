
class Stream():
    def hasNext(self):
        return self._hasNext()
    def next(self):
        return self._next()

class ListStream(Stream):
    def __init__ (self, _list):
        # copy, won't protect against race condition in threads, but will
        # prevent modifications to the original list affecting the Stream
        self._list = _list[:]
        self._index = 0
        self._max_index = len(self._list)

    def _hasNext(self):
        return self._index < self._max_index

    def _next(self):
        if self.hasNext():
            item = self._list[self._index]
            self._index = self._index + 1
            return item

    def toList(self):
        remaining = self._list[self._index:self._max_index]
        self._index = self._max_index
        return remaining
