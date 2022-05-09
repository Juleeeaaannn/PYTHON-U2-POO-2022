class Conjunto:
    __lista=[]
    def __init__(self,lista):
        self.__lista=lista
    def __add__ (self, otro):
        P= len(self.__lista)
        S= len(otro.__lista)
        j=0
        i=0
        conjunto= []
        while i < P and j < S:
            if self.__lista[i] < otro.__lista[j]:
                conjunto.append( self.__lista[i] )
                i+=1
            elif otro[j] < self.__lista[i]:
                conjunto.append( otro.__lista )
                j+=1
            else:
                conjunto.append( self.__lista[i] )
                i+=1
                j+=1
        if i < P:
            while i < P:
                conjunto.append( self.__lista[i] )
                i+=i
        elif j < S:
            while j < S:
                conjunto.append( otro.__lista[j] )
                j+=1
        return conjunto
    def __eq__ (self, otro):
        return self.__lista == otro.__lista
    def __sub__ (self, otro):
        conjunto=[]
        for i in self.__lista:
            if (i not in otro.__lista):
                conjunto.append(i)
        return conjunto