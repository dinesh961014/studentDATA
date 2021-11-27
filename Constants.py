ID= "iD"
FN = 'firstName'
LN = 'lastName'
EM = 'email'
AG = 'age'
PN = 'phoneNumber'
csvfile = "data.csv"

dictTOidx = { ID : 0 ,FN : 1 ,LN : 2 ,EM :3 ,AG : 4 ,PN : 5 }

Mandatory_ATTRIBUTE = [FN,EM,AG,PN]
Optional_ATTRIBUTE = [LN]
Req_ATTRIBUTE = [ID]

Success = { "Response" : "SUCCESS"}
Code = 200
ERR_Code = 401
Error_Length = { "error" : "Mandatory Attribute missing error"}
Error_WrongAttribute = { "error" : "Invalid attribute error"}
Error_AttributVALFailed = { "error" : ""}