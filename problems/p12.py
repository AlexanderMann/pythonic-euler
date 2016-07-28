
import math
import p7

_known_factorizations = {}

def known_factorizations(n):
  """Returns either a known factorization
  for a number, or False if none exists.
  """
  if n == 0:
    raise Exception("0 has no known factors")
  if p7.is_prime(n):
    return {1: n}
  return _known_factorizations.get(n, False)

def _merge_factorizations(factor_pairs, lower_factor, upper_factor):
  """Merge factorizations in place.
  """
  known_fs = known_factorizations(upper_factor)
  for lf in known_fs:
    new_low_factor = lf * lower_factor
    new_upper_factor = known_fs[lf] * lower_factor

    factor_pairs[min(new_low_factor, known_fs[lf])] = max(new_low_factor, known_fs[lf])
    factor_pairs[min(new_upper_factor, lf)] = max(new_upper_factor, lf)

def factorize(n):
  """Returns a dictionary of factors where
  a key is the smaller (or equal to) half
  of the factor pair, and the value is the
  larger.
  Ex. factorize(10) =>
  {1: 10
   2: 5}
  """
  if known_factorizations(n):
    return known_factorizations(n)

  factors_pairs = {1: n}

  upper_bound = int(math.floor(math.sqrt(n)));
  p7.seed_known_primes_up_to(upper_bound);

  for lower_factor in p7.known_primes:
    if lower_factor > upper_bound:
      break
    (upper_factor, remainder) = divmod(n, lower_factor)
    if remainder == 0:
      factors_pairs[lower_factor] = upper_factor
      factorize(upper_factor)
      _merge_factorizations(factors_pairs, lower_factor, upper_factor)
      break

  _known_factorizations[n] = factors_pairs
  return factors_pairs

def factors(n):
  """Return just the factors of n, not the factor pairs
  """
  factors = set()
  factor_pairs = factorize(n)
  for factor in factor_pairs:
    factors.add(factor)
    factors.add(factor_pairs[factor])
  return factors

def first_triangle_number_to_have_gt_n_factors(n):
  # http://www.mathblog.dk/files/euler/Problem12.cs
  # https://en.wikipedia.org/wiki/Coprime_integers
  #
  # Summary of above sources:
  #
  # kth triangle number = SUM i to k i
  # = k (k + 1) / 2
  # => if k is even then k/2, (k + 1) are coprime
  # => if k is odd then (k + 1)/2, k are coprime
  #
  # since the kth triangle number has two coprime factors,
  # it must follow, that its number of divisors is the
  # number of divisors for each of its coprimes multiplied
  # by each other.

  # silly edge case, but this cleans up what follows dramatically
  if n == 0:
    return 1

  k = 2
  number_of_divisors = 0
  number_of_divisors1 = 2
  number_of_divisors2 = 1

  while number_of_divisors < n:
    if k % 2 == 0:
      number_of_divisors1 = len(factors(k + 1))
    else:
      number_of_divisors2 = len(factors((k + 1) / 2))

    number_of_divisors = number_of_divisors1 * number_of_divisors2
    k += 1

  return k * (k - 1) / 2

def sln():
  return first_triangle_number_to_have_gt_n_factors(500)
