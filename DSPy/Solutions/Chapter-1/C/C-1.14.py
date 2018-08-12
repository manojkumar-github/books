"""
Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of
numbers in the sequence whose product is odd.
"""

def distint_oddnumbers_product_pair_in_sequence(aseq):

    odd_num_lst = []
    for num in aseq:
        if num%2 !=0:
            odd_num_lst.append(num)
            if len(odd_num_lst) == 2:
                return True
    return False

print (distint_oddnumbers_product_pair_in_sequence([2,4,6,8,10]))
print (distint_oddnumbers_product_pair_in_sequence([2,4,3,8,10]))
print (distint_oddnumbers_product_pair_in_sequence([2,1,6,3,10]))
print (distint_oddnumbers_product_pair_in_sequence((2,1,6,3,10)))
print (distint_oddnumbers_product_pair_in_sequence([]))




