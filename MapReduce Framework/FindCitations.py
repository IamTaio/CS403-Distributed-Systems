from MapReduce import MapReduce

class FindCitations(MapReduce):
    def Map(self, parts):
        partial = {}
        for i in parts:
            if i[1] in partial:
                partial[i[1]] = partial[i[1]] + 1
            else:
                partial[i[1]] = 1
        return partial

    def Reduce(self, dicts):
        result = {}
        for x in dicts:
            for i in x:
                if i in result:
                    result[i] = result[i] + x[i]
                else:
                    result[i] = x[i]
        return result
    
