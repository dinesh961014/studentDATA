LOCALHOST = http://127.0.0.1:8080

GETREQUEST :
    URL = LOCALHOST+/getData/iD=<int:number>/
        eg : http://127.0.0.1:8080/getData/iD=2/


POSTREQUEST:
    
    URL = LOCALHOST+/Update/
        eg : http://127.0.0.1:8080/Update/

    Input    
        input : body/raw/JSON
        :-input json must contain iD field and any one of other field
        eg input : {
                        "iD": 3,
                        "firstName" : "Ram",
                        "lastName" : "KUM",
                        "email" : "Krish@gmail.com",
                        "age" : 24,
                        "phoneNumber" : 9894211245
                    }





PUTREQUEST:
    
    URL = LOCALHOST+/Takeinputs/
    eg : http://127.0.0.1:8080/Takeinputs/
    Input
        input : body/raw/JSON
        :-input json must contain ALL field and except lastName which is optional
        eg input : {
                        
                        "firstName" : "Ram",
                        "lastName" : "KUM",
                        "email" : "Krish@gmail.com",
                        "age" : 24,
                        "phoneNumber" : 9894211245
                    }



PUTREQUEST:
    
    URL = LOCALHOST+/DeleteValues/
    eg : http://127.0.0.1:8080/DeleteValues/
    Input
        input : body/raw/JSON
        :-input json must contain iD and  phoneNumber field 
        eg input : {
                        
                        "iD": 3,
                        "phoneNumber" : 9894211245
                    }


*Note*
-Validation is done for each and every field
-This API perform get data, put some new data , del existing data and update existing data operations.