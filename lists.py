import copy

def eggs(someParam):
    someParam.append('Hello')

spam = [1,2,3]
eggs(spam)

print(spam)


def eggs2(someParam):
    tempList = copy.deepcopy(someParam)
    tempList.append('hi')
    print(tempList)

eggs2(spam)

print(spam)
