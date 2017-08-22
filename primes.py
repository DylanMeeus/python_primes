""" prime generator """
import sys, os


def sundaran(limit):
    """ sundaran sieve the primes """

    possible_primes = {}
    for i in range(1,limit):
        for j in range(i,limit):
            num = i+j+(2*i*j)
            if(i+j+(2*i*j) < limit):
                possible_primes[num] = False
            else:
                break

    # skipped by sieve
    primes = [2,3,5]
    for i in range(3,limit):
        if not i in possible_primes:
            if(i*2+1 > limit):
                break
            primes.append(i*2+1)

    # don't print the list to not waste time in stdout
    print(len(primes))
    print(primes)




if __name__ == '__main__':
    limit = 1000
    sundaran(limit)