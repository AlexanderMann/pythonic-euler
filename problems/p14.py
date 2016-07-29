
known_lengths = {}

# Collatz Generation iterative definition:
# n => n/2 (n is even)
# n => 3n + 1 (n is odd)

class CollatzIterator (object):
  def __init__(self, start):
    self.start = start
    self.last_val = 2 * start

  def __iter__(self):
    self.start = self.start
    self.last_val = 2 * self.start
    return self

  def next(self):
    if self.last_val == 1:
      raise StopIteration

    if self.last_val % 2 == 0:
      self.last_val = self.last_val / 2
    else:
      self.last_val = 3 * self.last_val + 1
    return self.last_val

  def __len__(self):
    if self.start in known_lengths:
      return known_lengths[self.start]

    l = 0
    for n in self:
      if n in known_lengths:
        l += known_lengths[n]
        break
      l += 1

    for n in self:
      if n in known_lengths:
        break
      known_lengths[n] = l
      l -= 1

    return known_lengths[self.start]

def longest_collatz_start_lt(n):
  # this is brute force, there has to be a better way
  longest_len = 0
  longest_start = None
  for start in xrange(n - 1, 0, -1):
    l = len(CollatzIterator(start))
    if l > longest_len:
      longest_len = l
      longest_start = start
  return longest_start

def sln():
  return longest_collatz_start_lt(1000000)

