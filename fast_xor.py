## The following function is performing xor function of consecutive numbers.
## It is using mathematical simplification and the results is O(1)
## It avoids recursion 

## Input arguments are the start value and the length

## For example fast_xor(102,5) returns the results of 102^103^104^105^106

def fast_xor(start_val,length):
    if start_val % 2 == 0:
        if length % 2 == 0:
        # even lenths are 1 and 0 intergchangeably
            return divmod(length,2)[0] % 2
        else:
            return (length + start_val -1  + divmod(length,2)[0] % 2)
    else:
        if length % 2 == 1:
        # even lenths are 1 and 0 intergchangeably
            return start_val - divmod(length,2)[0] % 2
            
        else:
            return fast_xor(start_val,length-1)^(start_val+length-1)
