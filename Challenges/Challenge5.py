
def listItems(itemList,value):
    """This is not my idea."""
    indexList = []
    for i in range(len(itemList)):
        if itemList[i] == value:
            indexList.append([i])
            # print(indexList)
        elif isinstance(itemList[i],list):
            for index in listItems(itemList[i],value):
                indexList.append([i] + index)
    return indexList

def main():
    # itemList = [[1,2],[2,3]]
    itemList = [[[1,2,3],2,[1,3]],[1,2,3]]
    value  = int(input("Enter the value to be searched"))
    print(listItems(itemList,2))

if __name__ == '__main__':
    main()