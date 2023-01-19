debtor = 0
for cred in -1140, -1440, 1824, 1833, -2803, 2870, 6684, -7039, 8376, 8818:
    if cred % 2 == 0 and cred >= 0:
        print(cred, " - должник")
        debtor += 1

print ('Всего должников - ', debtor)