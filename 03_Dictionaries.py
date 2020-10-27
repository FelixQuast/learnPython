# Dictionaries

liste = [1,2,3]

print(liste[0])

dictionary = {"Key":"Wert", "Key2":"Wert2"}
print(dictionary)
print(dictionary["Key2"])

dictionary2 = {"K1":123, "K2":12.33, "K3":"String", "K4":[1,2,3,4]}
print(dictionary2)
print(dictionary2["K4"])
print(dictionary2["K4"][3])

dictionary3 = {1:1,2:"test", "drittens":[7,8,9]}
print(dictionary3[1])
print(dictionary3["drittens"])
print(dictionary3["drittens"][2])
print(dictionary3[2])
print(dictionary3[2].upper())


print("----------------------------------------------------------------")

print(dictionary3)
print(dictionary3[1])
print(dictionary3[1]-1)
print(dictionary3[1])
dictionary3[1] = dictionary3[1] +99999999
print(dictionary3)


d4 = {}
d4["tier"] = "Hund"
d4["alter"] = 12
print(d4)

dic_in_dic = {1 : "test1", 2 : {2.1 : "unter1", 2.2 : "unter2", 2.3 : "unter3"}, 3:"tests3"}

print(dic_in_dic)
print(dic_in_dic[1])
print(dic_in_dic[2])
print(dic_in_dic[2][2.3])

print(dic_in_dic.keys())
print(dic_in_dic.values())
print(dic_in_dic.items())
