import math
from itertools import combinations


def apriori(trans, mins, iter):
    distinctSet = set()
    [distinctSet.add(j) for i in trans for j in list(combinations(i, iter))]
    distinctSet = sorted(list(distinctSet))  # Remove if you like
    distinctValue = {(''.join(i)): 0 for i in distinctSet}
    for j in list(map(lambda x: x.split(','), list({(','.join(i)): 0 for i in distinctSet}))):
        p = "".join(str(x) for x in j)
        for x in trans:
            distinctValue[p] = distinctValue[p] + all(ele in x for ele in j)
    NewdistinctValue = {key: val for key, val in distinctValue.items() if val >= math.ceil(mins * len(trans))}
    removeLetter = list(filter(lambda x: x not in list(NewdistinctValue.keys()), list(distinctValue.keys())))
    print("{} Iteration: L{} = {}.".format(iter, iter, NewdistinctValue))
    if NewdistinctValue:
        return apriori(remove_elem_nested_list(trans, removeLetter), mins, iter + 1)


def remove_elem_nested_list(dict_list, remove_Elems):
    if isinstance(dict_list, list):
        return [remove_elem_nested_list(item, remove_Elems) for item in dict_list if item not in remove_Elems]
    else:
        return dict_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    trans = [['A', 'B', 'C', 'D', 'E'],
             ['A', 'B', 'C', 'E'],
             ['A', 'B', 'D', 'E'],
             ['A', 'B', 'C', 'E'],
             ['A', 'B', 'C'],
             ['A', 'E']]

    apriori(trans, 0.65, 1)
