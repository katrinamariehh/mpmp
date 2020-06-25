results_set = set()
def triangle_loop(num1, num2, num3):
    if (num1 + num2 + num3) == 14:
        if len(results_set) == 0:
            print("starting numbers can't add up to 14")
            return
    next_1 = abs(num1 - num2)
    next_2 = abs(num2 - num3)
    next_3 = abs(num3 - num1)
    new_result = [next_1, next_2, next_3]
    print(new_result)
    # import pdb; pdb.set_trace()
    if frozenset((next_1, next_2, next_3)) in results_set:
        print("you found a loop")
        if next_1 + next_2 + next_3 == 14:
            print("you found it")
        return
    results_set.add(frozenset((next_1, next_2, next_3)))
    triangle_loop(next_1, next_2, next_3)
# difference needs to add to 14 in the loop but *not* when starting
# x, y, and z where the arragnement adds up to 14 and is stable
