import json

def readRnaTrans():
    f = open('rnalook', 'r')   #Small example dataset  from text
    
    cnt=0
    for line in f:
        cnt+=1
        if cnt==1:
            string1=line.rstrip() # get rid of cr
        elif cnt==2:
            string2=line.rstrip() # get rid of cr
        else:
            print("File is not in the form of 2 strings, exit")
            exit()

    print("Read ",cnt," Datapoints")
    return string1

def readDna():
    f = open('t2.txt', 'r')   #Small example dataset  from text
    
    cnt=0
    for line in f:
        cnt+=1
        if cnt==1:
            string1=line.rstrip() # get rid of cr
        elif cnt==2:
            string2=line.rstrip() # get rid of cr
        else:
            print("File is not in the form of 2 strings, exit")
            exit()

    print("Read ",cnt," Datapoints")
    return string1


print("Starting")
json_string = readRnaTrans()
lookupRna=json.loads(json_string)

DNAstring=readDna()
print("Translating ",DNAstring)
Dlength=len(DNAstring)
protein=""
for codon in range(0,Dlength,3):
    triplet=DNAstring[codon:codon+3]
    aa=lookupRna[triplet]
    if aa=='Stop':
        print("Found a stop, break")
        break
    protein+=aa

print(protein)
