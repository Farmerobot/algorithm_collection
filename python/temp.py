def Kelvin(temp,unit):
    if unit=="Celsius":
        return format(round(temp-273.15,2), '.2f')
    if unit=="Kelvin":
        t=format(round(temp,2), '.2f')
        if float(t)<0:
            return "NO"
        else:
            return t
    if unit=="Fahrenheit":
        return format(round(1.8*(temp-273.15)+32,2), '.2f')

def Celsius(temp,unit):
    if unit=="Celsius":
        return format(round(temp,2), '.2f')
    if unit=="Kelvin":
        t=format(round(temp+273.15,2), '.2f')
        if float(t)<0:
            return "NO"
        else:
            return t
    if unit=="Fahrenheit":
        return format(round((temp*1.8)+32,2), '.2f')

def Fahrenheit(temp,unit):
    if unit=="Celsius":
        return format(round((temp-32)/1.8,2), '.2f')
    if unit=="Kelvin":
        t=format(round((5/9)*(temp-32)+273.15,2), '.2f')
        if float(t)<0:
            return "NO"
        else:
            return t
    if unit=="Fahrenheit":
        return format(round(temp,2), '.2f')

n=int(input())
i=1
res=[]

while i<=n:
    temp=input().split(" ")
    if temp[1]=="Celsius":
        t=Celsius(int(temp[0]),temp[2])
        res.append(t)
    elif temp[1]=="Kelvin":
        t=Kelvin(int(temp[0]),temp[2])
        res.append(t)
    elif temp[1]=="Fahrenheit":
        t=Fahrenheit(int(temp[0]),temp[2])
        res.append(t)
    
    i+=1

print(*res,sep="\n")