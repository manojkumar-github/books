"""In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer.
The third of those implementations, from page 41, was the most efficient, but we noted that it did not yield the
factors in increasing order. Modify the generator so that it reports factors in increasing order, while maintaining
its general performance ad- vantages."""

def original_factor_fn(n):

    k = 1
    while k*k < n: # while k<sqrt(n)
        if n%k==0:
            yield(k)
            yield(n//k)
        k += 1
    if k*k == n:
        yield(k)


def factor_gen_fn_ordered(n):
    k = 1
    while k*k <=n:
        if n%k==0:
            yield(k)
        k +=1
    k -= 2
    while k>0:
        if n%k == 0:
            yield(n//k)
        k -= 1


gen_obj = original_factor_fn(16)
print (list(gen_obj))

new_gen_obj = factor_gen_fn_ordered(16)
print (list(new_gen_obj))
