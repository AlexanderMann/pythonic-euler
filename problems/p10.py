
import math
import p7

def sln():
  p7.seed_known_primes_up_to(2000000)
  s = 0
  for n in p7.known_primes:
    if n > 2000000:
      break
    s += n
  return s
