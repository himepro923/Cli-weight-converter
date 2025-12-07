wight = int(input('What is your wight: '))
kg_or_lbs = input("(K)g or (L)bs: ")

if kg_or_lbs == "l":
    print(wight * 0.453592)
elif kg_or_lbs == "k":
    print(wight * 2.20462)

