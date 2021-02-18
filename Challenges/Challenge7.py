import pickle
import ast
# Normal
# def saveDictionary(data,myFile):
#     myFile.write(str(data))
#     myFile.close()
#
# def retriveDictionary():
#     with open ("dataFile.txt","r") as f:
#         outData = f.read()
#     outData = ast.literal_eval(outData)
#     return outData


# Pickling
def saveDictionary(data,myFile):
    pickle.dump(str(data),myFile)
    myFile.close()
#
def retriveDictionary():
    with open('dataFile.txt','rb') as f:
        data = f.read()
    outData = pickle.loads(data)
    return outData

def main():
    myFile = open("dataFile.txt","wb+")
    keys = ["Name","Age","Height","Place"]
    values = ["Rohith",27,176,"Vadakara"]
    data = dict(zip(keys,values))
    saveDictionary(data,myFile)
    print(retriveDictionary())

if __name__ == '__main__':
    main()