d1={}
print(type(d1))
d2={"milind":"pizza","badal":"momos",
    "milan":"chole bhature",
    "prachi":{"morning":"chai pratha","afternoon":"dal roti","evening":"chai","night":"paneer roti"}}

d2["debo"]="junk food"
d2["sanya"]= "samosa"
#del d2["debo"]
#d3=d2
#del d3["milind"]
d2.update({"leena":"kachori"})
#print(d2.keys())
print(d2.items())