
let rec rabbitPairs n k = 

    match n with
        | 0 | 1 | 2 -> 1
        | _ -> ((rabbitPairs (n-1) k) + (k * rabbitPairs (n-2) k))
        
assert (rabbitPairs 1 3 = 1)
assert (rabbitPairs 2 3 = 1)
assert (rabbitPairs 3 3 = 4)
assert (rabbitPairs 4 3 = 7)
assert (rabbitPairs 5 3 = 19)
