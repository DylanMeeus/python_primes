""" prime generator """
import sys, os


def eratosthenes(limit):
    """ sieve of Eratosthenes """
    possible_primes = {}

    for i in range(2,limit):
        possible_primes[i] = True

    sqrtlimit = int(limit ** (1 / 2))
    print(sqrtlimit)
    for i in range(2, sqrtlimit+1):
        if possible_primes[i]:
            j = int(i**2)
            x = 0
            while j < limit:
                # -2 to correct for array index
                possible_primes[j] = False
                j = int((i**2) + (x*i))
                x += 1

    primes = []
    for i in range(2,limit):
        if possible_primes[i]:
            primes.append(i)


    print("last prime " + str(primes[-1:]))

def sundaram(limit):
    """ sundaran sieve the primes """

    possible_primes = {}
    for i in range(1,limit):
        for j in range(i,limit):
            num = i+j+(2*i*j)
            if(i+j+(2*i*j) < limit):
                possible_primes[num] = False
            else:
                break

    primes = [2]
    for i in range(1,limit):
        if not i in possible_primes:
            if(i*2+1 > limit):
                break
            primes.append(i*2+1)

    # don't print the list to not waste time in stdout
    print(len(primes))
    print(primes)




if __name__ == '__main__':
    limit = 20000000
    eratosthenes(limit)