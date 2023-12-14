amount=int(input("Enter the number"))

if amount>=500:
    c500=amount//500
    amount=amount%c500
    print(f"500x{c500}={c500}")

elif amount>=200:
    c200=amount//200
    amount=amount%c200
    print(f"200x{c200}={c200}")

elif amount>=100:
    c100=amount//100
    amount=amount%c100
    print(f"100x{c100}={c100}")

elif amount>=50:
    c50=amount//50
    amount=amount%c50
    print(f"50x{c50}={c50}")

elif amount>=20:
    c20=amount//20
    amount=amount%c20
    print(f"{c20}")

elif amount>=100:
    c10=amount//10
    amount=amount%10
    print(f"{c10}")

elif amount>=5:
    c5=amount//5
    amount=amount%c5
    print(f"{c5}")

elif amount>=2:
    c2=amount//2
    amount=amount%c2
    print(f"{c2}")

else:
    c1=amount
    print(f"{c1}")