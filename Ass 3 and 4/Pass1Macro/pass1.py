f = open("input.txt", "r")
out = open("pass1_output.txt", "a+")
out.truncate(0)

MDT = [] # Macro Definition Table
MNT = [] # Macro Name Table
ALA = [] # Argument List Array
words = []
MNTC = 1
MDTC = 1
ALAC = 1
MacroDefOn = False
macroname = 0

for line in f:
    if "MACRO" in line:
        MacroDefOn = True
        macroname = 1
    elif "MEND" in line:
        MDT.append([MDTC, line])
        MDTC += 1
        MacroDefOn = False
    elif MacroDefOn:
        if macroname == 1:
            MDT.append([MDTC, line])
            line = line.replace(",", "")
            words = line.split()
            MNT.append([MNTC, words[0], MDTC])  #words[0] contains macro name
            MNTC += 1
            for i in range(1, len(words)):
                words[i].replace(",", "")
                ALA.append([ALAC, words[i]])
                ALAC += 1
            MDTC += 1
            macroname = 0
        else:
            for i in ALA:
                if i[1] in line:
                    line = line.replace(i[1], str(i[0]))
                    MDT.append([MDTC, line])
                    MDTC += 1
    else:
        out.write(line)

mdttab = open("mdt.txt", "w")
mnttab = open("mnt.txt", "w")
alatab = open("ala.txt", "w")

print("\n=======MDT=======\n")
for i in MDT:
    print(i)
    mdttab.write(str(i[0]) + "\t" + str(i[1]))
print("\n=======MNT=======\n")
for i in MNT:
    print(i)
    mnttab.write(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\n")
print("\n=======ALA=======\n")
for i in ALA:
    print(i)
    alatab.write(str(i[0]) + "\t" + str(i[1]) + "\n")