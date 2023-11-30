def echange_case(case):
    if len(case) > 0:
        case[0], case[-1] = case[-1], case[0]

ma_case = [1, 2, 3, 4, 5]
print("Avant l'échange :", ma_case)

echange_case(ma_case)

print("Après l'échange :", ma_case)
