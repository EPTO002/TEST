#MoneyConvert.py
Money=input()
if Money[:3]=="RMB":
    print("USD{:.2f}".format(eval(Money[3:])/6.78))
elif Money[:3]=="USD":
    print("RMB{:.2f}".format(eval(Money[3:])*6.78))
