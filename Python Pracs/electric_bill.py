rates = {1:(50,0.5), 2:(100,0.75), 3:(100,1.2), 4:1.5}

usage = int(input("Enter the consumption in units"))
bracket = 1
total = 0

while usage>0:
    try:
        total += min(usage,rates[bracket][0])*rates[bracket][1]
        usage -= rates[bracket][0]
        bracket += 1
        print(total,usage)
    except:
        total += usage*rates[bracket]
        print(total,usage)
        break

print(total*1.2)