def cartesianProduct(start, array, partial, results):
    if len(partial) == len(array):
        results.append(partial)
        return results
    for element in array[start]:
        cartesianProduct(start+1, array, partial+[element], results)

def divList (i,j, w):
    newList = []
    while j <= len(w):
        newList.append(w[i:j])
        i += 1
        j += 1
    return newList

def CYK(w, rules, memo):
    for i in range(len(w)):
        if w[i] in rules:
            memo[0][i] = rules[w[i]]
    for i in range(1,len(w)):
        newList = divList(0,i+1,w)
        tree = []
        for word in newList:
            if len(word) <= 2:
                first = word[0:len(word)-1]
                second = word[len(word)-1]
                list = []
                if first in rules:
                    list.append(rules[first])
                if second in rules:
                    list.append(rules[second])
                cP = []
                cartesianProduct(0, list, [], cP)
                result = []
                for results in cP:
                    if "".join(results) in rules:
                        result += rules["".join(results)]
                if result:
                    rules[word] = result
                    tree.append(result)
                else:
                    tree.append([])
            else:
                first = word[0:len(word) - 1]
                second = word[len(word) - 1]
                third = word[0]
                forth = word[1:len(word)]
                list = []
                list2 = []
                if first in rules:
                    list.append(rules[first])
                if second in rules:
                    list.append(rules[second])
                if third in rules:
                    list2.append(rules[third])
                if forth in rules:
                    list2.append(rules[forth])
                cP = []
                cartesianProduct(0, list, [], cP)
                cP2 = []
                cartesianProduct(0, list2, [], cP2)
                result = []
                for results in cP:
                    if "".join(results) in rules:
                        result += rules["".join(results)]
                for results in cP2:
                    if "".join(results) in rules:
                        result += rules["".join(results)]
                if result:
                    rules[word] = result
                    tree.append(result)
                else:
                    tree.append([])
        memo[i] = tree
    if len(memo) == len(w) and memo[len(memo)-1] != [[]]:
        return True
    else:
        return False