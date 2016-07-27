
import math
import p7

triangle_numbers = [1, 3, 6, 10, 15, 21, 28]
_known_factorizations = {}

def known_factorizations(n):
  """Returns either a known factorization
  for a number, or False if none exists.
  """
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

def seed_triangle_numbers_up_to_len(n):
  """Insert triangle numbers into triangle_numbers till
  it is of len at least n
  """
  idx = len(triangle_numbers)
  if n < idx:
    return
  while idx < (2 * n):
    idx += 1
    triangle_numbers.append(triangle_numbers[-1] + idx)

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
  last_triangle_number = 0
  idx = 0
  while True:
    seed_triangle_numbers_up_to_len(idx + 1)
    if last_triangle_number != triangle_numbers[-1]:
      last_triangle_number = triangle_numbers[-1]
      p7.seed_known_primes_up_to(last_triangle_number)
    if len(factors(triangle_numbers[idx])) > n:
      return triangle_numbers[idx]
    idx += 1

def sln():
  p7.seed_known_primes_up_to(80000000)
  return first_triangle_number_to_have_gt_n_factors(500)
