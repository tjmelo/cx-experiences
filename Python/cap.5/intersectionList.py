def IntersectionList (l1, l2):
    '''
    - Returns the intersection of two given lists
    '''
    resultList = []
     
    for element in l1:
        if element in l2:
            resultList.append(element)
    
    return resultList


getIntersection = IntersectionList([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
print(getIntersection)
