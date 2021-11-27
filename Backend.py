
from Constants import *
import pandas as pd
import json

def findLastIndex(str, x):
    index = -1
    for i in range(0, len(str)):
        if str[i] == x:
            index = i
    return index
def Validatekeys (listOfKeys):
    isPresent = True
    if len (listOfKeys) == 4:
        for key in listOfKeys:
            if not key in Mandatory_ATTRIBUTE :
                isPresent = False
                break
        if isPresent:
            return None
        else :
            return Error_WrongAttribute
    elif len (listOfKeys) == 5:
        for key in listOfKeys:
            if not key in Mandatory_ATTRIBUTE+ Optional_ATTRIBUTE :
                isPresent = False
                break
        if isPresent:
            return None
        else :
            return Error_WrongAttribute
    else :
        return Error_Length
    
def validateFields (no, inputData) :
    arr = ""
    if not (isinstance(inputData [FN], str)) :
        arr = "'"+FN+"'"
    if not (isinstance(inputData [EM], str) and (inputData [EM].count ( "@" ) == 1 ) and findLastIndex( inputData [EM], "@") > 3 and (findLastIndex( inputData [EM], "@")<findLastIndex( inputData [EM], ".")+3) and findLastIndex( inputData [EM], ".")+2 < len (inputData [EM])):
        arr = arr+" '"+EM+"'"
    if not ( isinstance(inputData [AG], int) and inputData [AG] >= 18) :
        arr = arr+" '"+AG+"'"
    if not ( isinstance(inputData [PN], int) and len (str(inputData [PN])) == 10) :
        arr = arr+" '"+PN+"'"
    if no == 5 :
        if not (isinstance(inputData [LN], str) or inputData [LN] == None) :
            arr = arr +" '"+LN+"'"
    return arr

def writeintoCSV (request_data):
    try :
        df = pd.read_csv(csvfile)
        column = df["iD"]
        max_value = column. max()
        #print(df.to_string())
        df.fillna('', inplace=True)
        
        df.loc[len (df)] = [max_value+1]+request_data#,"sham","","sham@ksm.com",21,9566887488]
        #print (df.to_string())
        df.to_csv(csvfile, index=False)
        return True,max_value+1
    except Exception as e :
        print ('error occured while writing data :'+ str(e))
        
    return False, 0


def process_Put_Data (request_data):
    
    listOfKeys = request_data.keys()
    lenofkeys = len (listOfKeys)
    atrVdty = Validatekeys (listOfKeys)
    
    if atrVdty == None:
        res = validateFields(lenofkeys, request_data)
        
        if res == "" :
            if lenofkeys == 5 :
                values = [request_data[FN],request_data[LN],request_data[EM],request_data[AG],request_data[PN]]
            else :
                values = [request_data[FN],"",request_data[EM],request_data[AG],request_data[PN]]
            res = writeintoCSV (values)
            if res [0]:
                Success [ID] = res[1]
                return Code,Success
            else:
                Error_AttributVALFailed ['error'] = "Coludn't register the data :"+ str(values)
                return ERR_Code, Error_AttributVALFailed
        else :
            Error_AttributVALFailed ['error'] = "One or more attributes failed validation :"+ res
            return ERR_Code, Error_AttributVALFailed
    else :
        return ERR_Code,atrVdty


def DelFromCSV (id,phno):
    try :
        df = pd.read_csv(csvfile)
        idx = None
        for index, row in df.iterrows():            
            if str(row [ID]) == str (id):
                if  str(row [PN]) == str (phno) :
                    idx = index

                    
                else :
                    return False, "Given PhoneNo didnt match"
            
        if idx != None :
            df = df.drop(idx)
            df.to_csv(csvfile, index=False)
            return True, ""
        else :
        
            return False,"No Such Unique ID"
    except Exception as e :
        print ('error occured while writing data :'+ str(e))
        
    return False,"Exception occured while deleting record"


def process_Del_Data (request_data):
    
    listOfKeys = request_data.keys()
    lenofkeys = len (listOfKeys)
    if lenofkeys == 2 :
        if (request_data [ID] !=None and request_data [ID] != "") and isinstance(request_data [ID], int) and  ( isinstance(request_data [PN], int) and len (str(request_data [PN])) == 10) :
            res = DelFromCSV (request_data [ID],request_data [PN])
            if res [0]:
                Success [ID] = res[1]
                return Code,Success
            else:
                Error_AttributVALFailed ['error'] = "Coludn't Delete the data :"+ res[1]
                return ERR_Code, Error_AttributVALFailed
        else:
            Error_AttributVALFailed ['error'] = "one or more invalid Parameter(s) check "+ID+" and/or "+PN 
            return ERR_Code, Error_AttributVALFailed
    else :
        return ERR_Code,Error_Length

def GetFromCSV (id):
    try :
        df = pd.read_csv(csvfile)
        df.fillna('', inplace=True)

        idx = None
        for index, row in df.iterrows():            
            if str(row [ID]) == str (id):
                idx = index
            
        if idx != None :
            row = df.loc [idx]
            outputdict = {ID:int (row[0]),FN:row[1],LN:row[2],EM:row[3],AG:int(row[4]),PN:int(row[5])}
            
            
            return True, outputdict
        else :
        
            return False,"No Such Unique ID"
    except Exception as e :
        print ('error occured while writing data :'+ str(e))
        
    return False,"Exception occured while Getting record"
def process_Get_Data (num):
    
    if (num !=None and num != "") and isinstance(num, int):
        res = GetFromCSV (num)
        if res [0]:
            
            return Code,res[1]
        else:
            Error_AttributVALFailed ['error'] = "Coludn't Delete the data :"+ res[1]
            return ERR_Code, Error_AttributVALFailed
    else:
        Error_AttributVALFailed ['error'] = "Invalid Parameter check "+ID 
        return ERR_Code, Error_AttributVALFailed

def validatePOSTFields (inputData) :
    arr = ""
    if ID in inputData.keys() and not  isinstance(inputData [ID], int)  :
        arr = arr+" '"+AG+"'"
    if FN in inputData.keys() and not (isinstance(inputData [FN], str)) :
        arr = "'"+FN+"'"
    if EM in inputData.keys() and not (isinstance(inputData [EM], str) and (inputData [EM].count ( "@" ) == 1 ) and findLastIndex( inputData [EM], "@") > 3 and (findLastIndex( inputData [EM], "@")<findLastIndex( inputData [EM], ".")+3) and findLastIndex( inputData [EM], ".")+2 < len (inputData [EM])):
        arr = arr+" '"+EM+"'"
    if AG in inputData.keys() and not ( isinstance(inputData [AG], int) and inputData [AG] >= 18) :
        arr = arr+" '"+AG+"'"
    if PN in inputData.keys() and not ( isinstance(inputData [PN], int) and len (str(inputData [PN])) == 10) :
        arr = arr+" '"+PN+"'"
    
    if LN in inputData.keys() and not (isinstance(inputData [LN], str) or inputData [LN] == None) :
        arr = arr +" '"+LN+"'"
    return arr
def ValidatePOSTkeys (listOfKeys):
    isPresent = True
    if len (listOfKeys) > 1:
        for key in listOfKeys:
            if not key in Mandatory_ATTRIBUTE+ Optional_ATTRIBUTE +Req_ATTRIBUTE :
                isPresent = False
                break
        if isPresent:
            return None
        else :
            return Error_WrongAttribute

    else :
        return Error_Length
def modifyintoCSV (inputDict,listOfKeys):
    try :
        df = pd.read_csv(csvfile)
        idx = None
        for index, row in df.iterrows():            
            if str(row [ID]) == str (inputDict [ID]):
                idx = index
                """if  str(row [PN]) == str (phno) :
                    idx = index

                    
                else :
                    return False, "Given PhoneNo didnt match"""
            
        if idx != None :
            
            oldRec = df.loc[idx] 
            for each in listOfKeys:
                ind = dictTOidx [each]
                print (inputDict[each])
                oldRec [ind] = inputDict[each]
            print (oldRec)
            df.loc[idx]= oldRec       
            df.to_csv(csvfile, index=False)
            return True, ""
        else :
        
            return False,"No Such Unique ID"
    except Exception as e :
        print ('error occured while modifying data :'+ str(e))
        
    return False,"Exception occured while deleting record"
def process_Post_Data (request_data):
    
    listOfKeys = request_data.keys()
    lenofkeys = len (listOfKeys)
    atrVdty = ValidatePOSTkeys (listOfKeys)
    
    if atrVdty == None:
        res = validatePOSTFields( request_data)
        
        if res == "" :
            
            res = modifyintoCSV (request_data,listOfKeys)
            if res [0]:
                return Code,Success
            else:
                Error_AttributVALFailed ['error'] = "Coludn't modify the data :"+ str(request_data)
                return ERR_Code, Error_AttributVALFailed
        else :
            Error_AttributVALFailed ['error'] = "One or more attributes failed validation :"+ res
            return ERR_Code, Error_AttributVALFailed
    else :
        return ERR_Code,atrVdty