print("------------Operations on List-----------")
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print("----Access list elements using index------")
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
print("----Changing the values in a list------")
myFruitList[2] = "orange"
print(myFruitList)
print("------------Operations on Tuple-----------")
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print("----Access tuple elements using index------")
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print("----Changing the values in a tuple. Cannot change tuple elements .Convert tuple into list , make changes and then again convert into tuple------")
myFinalAnswerTuple=list(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
myFinalAnswerTuple[0]="Mango"
myFinalAnswerTuple=tuple(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple)
print("------------Operations on Dictionary-----------")
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print("----Access dictionary elements using keys , not values------")
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
print("----Changing dictionary elements using key------")
myFavoriteFruitDictionary["Akua"]="Mango"
print(myFavoriteFruitDictionary)
