temp = 10

if temp < 20:
    print("its cold\n"
          "wear jacket")

fund = 1000

if fund <= 1000:
    tex = "no fees applied"
else:
    text = "fees applied"
print(tex)

tex = "no fees applied" if fund <= 1000 else "fees applied"
print(tex)

conditon_1 = True
conditon_2 = True

if conditon_1 and conditon_2:
    print("True")
else:
    print("False")

conditon_3 = False
conditon_4 = True

if conditon_1 or conditon_2:
    print("True")
else:
    print("False")

if not conditon_3:
    print("True")