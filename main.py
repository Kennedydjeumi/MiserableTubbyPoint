import random 
security="ABCDEFGHIJKLMNOPQRSTUVWXYZqazxswedcvfrwomantgbnhyujmkiolp)*&^%^$#@#$%$^%&^*&(*)(_)+_" + "hieei12345678" + " "
security=(list(security))
assign= security.copy()
random.shuffle(security)
random.shuffle(assign)
print(f"secuirty characters= {security}")
print(f"Assigned as well={assign}")
First_message=input("enter the message to be encrypted")
encrypt=""
for character in First_message:
  index = security.index(character)
  encrypt += assign[index]

print(f"encrypted  message{encrypt}")
