animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    v = list(aDict.values())
    k = list(aDict.keys())
    return k[v.index(max(v))]

print (biggest(animals))
    
