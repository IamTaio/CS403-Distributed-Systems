from MapReduce import MapReduce

class FindCyclicReferences(MapReduce):
    def Map(self, parts):
        partial = {}
        for i in parts:
            if i[0] <= i[1]:
                temptuple = tuple(i)
            else:
                temptuple = (i[1],i[0])
            temptuple = str(temptuple)
            if temptuple not in partial:
                partial[temptuple] = 1
            else:
                partial[temptuple] = partial[temptuple] + 1

        return partial

    def Reduce(self, dicts):
        collected = {}
        result = {}
        for x in dicts:
            for i in x:
                if i not in result:
                    if x[i] > 1:
                        result[i] = 1
                        collected[i] = x[i]
                    elif i not in collected:
                        collected[i] = x[i]
                    else:
                        collected[i] = collected[i] + 1
                        result[i] = 1

        return result

