letter='''Dear <|NAME|>,
You are selected

date:<|DATE|>
'''
name=input("entr ur name")
date=input("enter date")
lettter=letter.replace("<|NAME|>",name)
lettter=letter.replace("<|DATE|>",date)
print(letter)