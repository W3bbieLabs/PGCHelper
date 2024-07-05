import sys
def CLIUsage():
    print("\nUsage:")
    print("\tpgchelper <target-site> <tld> <target-element-class> <browser>")
    print("\tpgchelper https://site.com .com chrome randomize-button")
    print("------------------------------------------")
    print("\nBrowser Options:")
    print("- firefox")
    print("- edge")
    print("- chrome")
    print("- safari")
def CheckArguments()->bool or dict:
    try:
        EXPECTED_ARGUMENTS  = 5
        argumentsValid      = False
        validArgs           = bool()
        notEnoughArgs       = (len(sys.argv) != EXPECTED_ARGUMENTS)
        while (not argumentsValid):
            if (notEnoughArgs):
                print("Not enough supplied arguments.")
                CLIUsage()
                validArgs = False
                break
            else:
                url     = sys.argv[1]
                tld     = sys.argv[2]  
                browser = sys.argv[4]  
                element = sys.argv[3]
                if (CheckURLString(url, tld) and CheckBrowerArg()):
                    validArgs = True
                    return { "url": url, "tld": tld, "browser":browser, "element": element }
                    break
                else:
                    print("Cannot set target site and browser.")
                    validArgs = False; break
            return validArgs
    except Exception as error:
        print(error)
def CheckBrowerArg()-> bool:
    try:
        browserArgGood = False
        browserArg = sys.argv[4]
        browserList = ["chrome","firefox","edge","safari"]
        if (browserArg.lower() in browserList):
            print("Acceptable browser: ", browserArg.upper())
            browserArgGood = True
        return browserArgGood
    except Exception as error:
        print("Likely range error. Also, there could be a typo. Or maybe you are trying to use a non-supoorted browser.")
        CLIUsage()
def CheckURLString(url:str="https://pgc-members.xyz", tld:str=".xyz")->bool:
    httpsCheck  = (url.lower()[0:8] == "https://")
    httpCheck   = (url.lower()[0:7] == "http://")
    tldCheck    = url.lower().endswith(tld)
    urlValid    = bool()
    try:
        print(f"CHECKING {url}")
        allChecksFail = ( (not httpsCheck) and (not httpCheck) and (not tldCheck) )
        domainChecksFail = ( (not httpsCheck) and (not httpCheck) )
        tldCheckFails = (not tldCheck)
        if (  allChecksFail or domainChecksFail or tldCheckFails ):
            if (not httpCheck):
                print("Does not use http://")
            elif (not httpsCheck):
                print("Does not use https://")
            elif (not tldCheck):
                print("Does not end with .com (or equivalent)")
            urlValid = False
        else: # passes all checks must be valid url
            urlValid = True
        return urlValid
    except Exception as error:
        print(error)
        return False