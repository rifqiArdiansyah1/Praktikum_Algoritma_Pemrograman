colorList = ["red", "green", "blue"]
codeList = ["#FF0000", "#008000", "#0000FF"]
colorDictionary = dict()
def joinColorDictionary(colorList, codeList):
    for i in range(0, len(colorList)):
        colorDictionary[colorList[i]] = codeList[i]
    return colorDictionary
print(joinColorDictionary(colorList, codeList))