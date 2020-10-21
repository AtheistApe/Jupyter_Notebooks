# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[keylist[i]] for i in range(len(dct))]

def list2dict(L, keylist): return { keylist[i]:L[i] for i in range(len(L))}

def listrange2dict(L): return { i:L[i] for i in range(len(L)) }

def listrange2dict2(L): return list2dict(L, range(len(L)))