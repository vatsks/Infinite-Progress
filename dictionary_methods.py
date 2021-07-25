dict={
    "zehr":"a poison",
    "marks":[2,4,3],
    "value":{"player":"person 1"}#
}
print(list(dict.keys()))
print(dict.values())
print(dict)
anotherdict={
    "shreyush":"a friend"
}
dict.update(anotherdict)
print(dict)
print(dict.get("apple"))#as nothing is present in dictionary with apple