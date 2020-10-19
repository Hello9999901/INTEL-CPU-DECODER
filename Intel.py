import time
import re 


#INTRO
print ("\n")
print ("\n")
print ("\n")
print ("Hi there! I will help you decode your Intel Core(TM) CPU!")
print ("\n")
print("\n")
print("\n")
print("        ___")  
print("    ----    |")
print("   | intel /")
print("    \___  |")
print("        --")
print ("This is ONLY for Intel Core(TM) i series CPUs!")
print ("This does NOT include M series chips!")
print ("Apologizes for the inconvenience!")
val = input("By pressing enter, you agreee to continue")
while val == "YES":
    print ("OK! Let's Continue!")
    break
else:
    print (" ")


#ASK FOR CPU MODEL
cpu = input("Please enter your CPU name without Intel Core Prefix! AKA the Processor Number (No Spaces) Ex:i7-1065G7 \n Here:")
print ("OK, thanks! I will start decoding!")




#CPU BRAND
if cpu[0] == "m":
    cpubrand = "m"
elif cpu[0:1] == "m3":
    cpubrand = "m3"
elif cpu[0:1] == "m5":
    cpubrand = "m3"
elif cpu[0:1] == "m7":
    cpubrand = "m7"
else:
    cpubrand = str(cpu[0:2])

afterbrand = cpu[3:10]
sku = afterbrand.strip()

temp = re.findall(r'\d+', sku) 
skunum = list(map(int, temp)) 
skunum = str(skunum)
skunumnum = len(skunum)
print (len(skunum))


#CPU GENERATION
if cpubrand == "m":
    cpugen = cpu[2]
elif skunumnum == 5:
    cpugen = 1
else:
    cpugen = int(cpu[3])
    if int(cpu[3:5]) == 10:
        cpugen = 10
    else:
        cpugen = int(cpu[3])
        cpugen = int(cpugen)


#CPU SUFFIX
hasSE = "S" in cpu
hasK = "K" in cpu
hasF = "F" in cpu
hasT = "T" in cpu
hasH = "H" in cpu
hasKS = "KS" in cpu
hasHK = "HK" in cpu
hasG = "G" in cpu
hasHQ = "HQ" in cpu
hasT = "T" in cpu
hasC = "C" in cpu
hasR = "R" in cpu
hasMQ = "MQ" in cpu
hasMX = "MX" in cpu
hasS = "S" in cpu
hasU = "U" in cpu
hasY = "Y" in cpu
hasM = "M" in cpu

#10th GEN CPUs
if cpugen == 10:
    if hasG == True:
        suffix = "Improved On-Board Graphics"
    elif hasU == True:
        suffix = ("Ultra-Low Power")
    elif hasY == True:
        suffix = ("Extremely Low Power")
    elif hasHK == True:
        suffix = "High performance graphics, unlocked"
#OTHER CPUs
elif cpugen != 10:
    if hasK == True:
        suffix = "Unlocked"
    elif hasT == True:
        suffix = "Power-optimized lifestyle"
    elif hasF == True:
        suffix = "Requires discrete graphics"
    elif hasG == True:
        suffix = "Includes discrete graphics on package"
    elif hasU == True:
        suffix = "Ultra-low power"
    elif hasSE == True and cpugen > 5:
        suffix = "Special Edition"
    elif hasH == True:
        suffix = "High performance graphics"
    elif hasHK == True:
        suffix = "High performance graphics, unlocked"
    elif hasG == True:
        suffix = "Includes discrete graphics on package"
    elif hasU == True:
        suffix = "Ultra-low power"
    elif hasHQ == True:
        suffix = "High performance graphics, quad core"
    elif hasY == True:
        suffix = "Extremely low power"
    elif hasC == True:
        suffix = "Unlocked desktop processor based on the LGA 1150 package with high performance graphics"
    elif hasR == True:
        suffix = "Desktop processor based on BGA1364 (mobile) package with high performance graphics"
    elif hasS == True and cpugen < 5:
        suffix = "Performance-optimized lifestyle"
    elif hasM == True:
        suffix = "Mobile"
    elif hasMQ == True:
        suffix = "Quad-core mobile"
    elif hasMX == True:
        suffix = "Mobile extreme edition"
    elif hasKS == True:
        suffix = "Special Edition, Unlocked"
    else: 
        suffix = "Nothing"

#Generation Name
if cpugen == 1:
    cpuname = "Nehalem"
elif cpugen == 2:
    cpuname = "Sandy Bridge"
elif cpugen == 3:
    cpuname = "Ivy Bridge"
elif cpugen == 4:
    cpuname = "Haswell"
elif cpugen == 5:
    cpuname = "Broadwell"
elif cpugen == 6:
    cpuname = "Skylake"
elif cpugen == 7:
    cpuname = "Kaby Lake"
elif cpugen == 8:
    if hasY == True:
        cpuname = "Amber Lake"
    elif hasU == True:
        cpuname = "Either Kaby Lake Refresh or Whisky Lake"
    else:
        cpuname = "Coffee Lake"
elif cpugen == 9:
    if hasU == True:
        cpuname = "Cannon Lake"
    else:
        cpuname = "Coffe Lake Refresh"
elif cpugen == 10:
    if hasG == True:
        cpuname = "Ice Lake"
    elif hasY == True:
        cpuname = "Amber Lake Refresh"
    else:
        cpuname = "Comet Lake"
elif cpugen == 11:
    cpuname = "Tiger Lake"
else:
    cpuname = "undefined (sry!)"


if cpugen > 3:
    cpugen = str(cpugen)+"th"
elif cpugen == 3:
    cpugen = str(cpugen)+"rd"
elif cpugen == 2:
    cpugen = str(cpugen)+"nd"
elif cpugen == 1:
    cpugen = str(cpugen)+"st"
else:
    pass


print ("\n")
print ("\n")
print ("Your CPU is a(n):")
print ("Intel(TM) Core",cpubrand)
print (cpugen,"generation")
print ("Here is what the product line sufix means:", suffix)
print ("Also, the CPU Generation name is :",cpuname)
print ("\n")
