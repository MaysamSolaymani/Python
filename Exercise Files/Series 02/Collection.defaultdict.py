from collections import defaultdict
import pdb
'''for item, value in defaultdict.__dict__.items():
    print(item, value)'''
d = {}
print(d)
d = defaultdict(lambda: 0)
print(d['one'])
print(d)
d['twenty'] = 20
print(d)
print(d.items())
pdb.set_trace() #start pdb trace online and quite with insert 'q'


