# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))

#output 2 because 20 and 20.0 we know set dont contain duplicate value.