# importing module
import csv
# from gd import *
from xo import *
import traceback

def importCSV(filename="AEsales.csv", xoKeyForOutput = "mock.excels", saveToXO = True, display = True, maxDisplay = 6, pretty = True):
    dataTable = []
    print("\nImporting excel file",filename,"\n")
    maxL = 0
    with open(filename,'r') as data:
        tabsize = 27
        for line in csv.reader(data):
            dataTable.append(line)
            if display:
                if not pretty:
                    print(line[:maxDisplay])
                else:
                    for s in line:
                        if len(s) > maxL:
                            maxL = len(s)
                            # print("Max",maxL,s)
    if pretty and display:
        # tabsize = maxL
        clear = ""
        for c in range(tabsize):
            clear += " "
        nT = []
        for line in dataTable:
            nL = []
            for s in line:
                nL.append((s+clear)[:tabsize])
            nT.append(nL)

        c = 1
        for l in nT:
            print(l[:maxDisplay])
            if c - 10 > 0 and (c - 10) % 8 == 0 or c == 10:
                print("=====================================================================================================================================================================")

            c+=1
    if saveToXO:
        if filename.endswith(".csv"):
            filename = ".".join(filename.split(".")[:-1]) # to remove trailing .csv
        xo.GetXO(xoKeyForOutput, allow_creation=True)[filename] = dataTable
        return xoKeyForOutput+"."+filename
    return None

# #####################################
# #            TESTING
# #####################################
# filename ="mockExcel2020.csv"
# xoKeyForOutput = "mock.excels"
# ###################################
#
# keyResults = importCSV(filename = filename, xoKeyForOutput = xoKeyForOutput, display = True)
# print()
# print(filename,"is saved to ",keyResults)

# from excelReader import importCSV as i ; i()



#####################################
#       HOW TO IMPORT & USE
#####################################
# # TO Use this code somewhere else use -
# from excelReader import * ;

def getBlocks(table):
    blocks = []
    # TODO: AUTO LOAD KEYS & HEADER SIZE
    headerSize = 10
    keys = ["Customer","Customer PN","Po REF","From Stock", "Qty","Price","Discount","Final Price"]
    blockSize = len(keys)
    for col in range(len(table[0][1:])):
        # print("CCCCCCCCC")
        colID = col+1
        realLines = int((len(table)-headerSize)/blockSize)
        # print(realLines)
        tC = 0
        for thickLine in range(realLines):
            newBlock = {"valveID":table[0][col+1]}
            for i in range(blockSize):
                newBlock[keys[i]] = table[headerSize + thickLine*blockSize+i][colID]
            blocks.append(newBlock)
    return blocks

def filterBlocks(allBlocks):
    res = []
    for b in allBlocks:
        empty = True
        for d in b:
            if not b[d] == "" and "price" not in d.lower() and "valveid" not in d.lower():
                # print("DDDDDDDD",b[d], "price" not in d.lower(), d)
                empty = False
        if not empty:
            res.append(b)
    return res

filename ="AEsales.csv" ; xoSaveDir = "mock.excels"
display = True
keyResults = importCSV(filename = filename, xoKeyForOutput = xoSaveDir, display = display)
results = xo.GetXO(keyResults).value()
allBlocks = filterBlocks(getBlocks(results))
print(" ::: SAVING RESULTS IN :",keyResults)
xo.GetXO(keyResults, allow_creation=True).blocks = allBlocks

def calcSums():
    sumP = 0
    totalV = 0
    for b in allBlocks:
        try:
            # sumP += int(b["Final Price"].replace("₪","").replace(",",""))
            if "Final Price" in b and b["Final Price"] is not None and b["Final Price"] is not "":
                sumP += int(b["Final Price"].replace("₪","").replace(".","").replace(",","").strip())
            if "Qty" in b and b["Qty"] is not None and b["Qty"] is not "":
                totalV += int(b["Qty"])

        except:
            print("Failed to add with",b)
            if b is not None and "Qty" in b:
                print("[Qty]",b["Qty"])
            else:
                print("no [Qty]")
            traceback.print_exc()

    print()
    print()
    print()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    cb = 1
    for b in allBlocks:
        print(cb,"::::::::",b);cb+=1
    print()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Total Blocks", len(allBlocks), " TOTAL PRICE:",sumP, " TOTAL VALVES",totalV)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! All blocks are saved to xo."+keyResults)
    print()

calcSums()

print("To run with python interpreter use:")
print()
print("import excelReader")
print()


# xo.mock.excels.AEsales.show()
