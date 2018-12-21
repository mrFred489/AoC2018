starting = True
reg0 = 0
reg1 = 0
reg2 = 0
reg3 = 0
reg4 = 0
reg5 = 0
reg1s = []
prev_reg1 = 0
print(reg1, reg2, reg3, reg4, reg5)
while True:
    if starting:
        reg5 = reg1 | 65536
        reg1 = 8586263
        starting = False
    reg2 = reg5 & 255
    reg1 += reg2
    reg1 &= 16777215
    reg1 *= 65899
    reg1 &= 16777215
    print("line 20", reg1, reg2, reg3, reg4, reg5)
    if 256 > reg5:
        print(reg1, reg2, reg3, reg4, reg5)
        # jump to ip=28
        if reg1 in reg1s:
            print(reg1s[-5:],
                  reg1,
                  reg1s[reg1s.index(reg1)-1],
                  reg1s[reg1s.index(reg1)-3: reg1s.index(reg1)+3])
            print("done", prev_reg1)
            break
        else:
            prev_reg1 = reg1
            reg1s.append(reg1)
        if reg1 == reg0:
            break
        else:
            starting = True
            continue
    reg2 = 0  # ip = 17
    while not reg3 > reg5:
        # print("line 35", reg1, reg2, reg3, reg4, reg5)

        reg3 = reg2 + 1
        reg3 *= 256
        reg2 += 1
    
    # print("line 45", reg1, reg2, reg3, reg4, reg5)
    # break
    reg2 -= 1
    reg5 = reg2

# 10508527
# 13151574

