
import p7

def _longest_prime_sum(starting_idx, ending_idx, n):
  current_idx = starting_idx
  running_sum = 0
  longest_run_prime = 0
  longest_run = 0
  while current_idx <= ending_idx:
    running_sum += p7.known_primes[current_idx]
    if running_sum > n:
      break
    if p7.is_prime(running_sum):
      longest_run = current_idx - starting_idx + 1
      longest_run_prime = running_sum
    current_idx += 1

  return [longest_run, longest_run_prime]

def calculate_ending_idx(n):
  p7.seed_known_primes_up_to(n)
  ending_idx = 0
  for p in p7.known_primes:
    if p >= n:
      break
    ending_idx += 1
  return ending_idx

def longest_prime_sum_less_than(n):
  p7.seed_known_primes_up_to(n)
  ending_idx = calculate_ending_idx(n)

  greatest_prime_sum_len = 0
  greatest_prime_sum = 0
  current_idx = 0

  while current_idx <= ending_idx:
    (gpsl, gps) = _longest_prime_sum(current_idx, ending_idx, n)
    if gpsl > greatest_prime_sum_len:
      greatest_prime_sum_len = gpsl
      greatest_prime_sum = gps
    current_idx += 1
  return [greatest_prime_sum_len, greatest_prime_sum]

def sln():
  return longest_prime_sum_less_than(1000000)

