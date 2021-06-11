# Engineering Economics Toolkit
# Powered by HSS
# Version: alpha
# Released on January 4,2021
# From now on, don't worry about finding EE factors! Here is EET.

Factors = ["F/P","P/F","P/A","F/A","A/P","A/F","A/G","P/G"]
Input = ""
SF1 = ["fp","pf","pa","fa","ap","af","ag","pg"]
SF2 = ["fp0","pf0","pa0","fa0","ap0","af0","ag0","pg0"]
history = []

def instructions():
    print("                                                       ")
    print(" ====================(Instructions)====================")
    print("|                                                      |")
    print("| Welcome! This is Engineering Economics Toolkit.      |")
    print("|                                                      |")
    print("|   Input Section:                                     |")
    print("|  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   |")
    print("| (Input:) is the gate for entering ordinary mathmatics|")
    print("| and EE factors to be calculated. Here is an example: |")
    print("|                                                      |")
    print("| Input:(2+3)*4 >>> (Enter) >>> Command: (Enter)       |")
    print("|                                                      |")
    print("| (2+3)*4                                              |")
    print("| Ans = 20                                             |")
    print("|                                                      |")
    print("| Supported operators are:                             |")
    print("| (+) addition, (-) subtraction, (*) multiplication and|")
    print("| (/)devision. Also (**) can raise powers and (//)     |")
    print("| returns integer dividor. e.g. 0.5**2=0.25 or 23//5=4 |") 
    print("|                                                      |")
    print("| Entered factors to (Input:) will be quantifed which  |")
    print("| are in the form shown below.                         |")
    print("|                                                      |")
    print("| ([factor],[interest rate],[number of periods])       |")
    print("|                                                      |")
    print("| Supported factors are:                               |")
    print("| F/P , P/F , P/A , F/A , A/P , A/F , A/G and P/G      |")
    print("| Note that these factors are for discrete cash flows. |")
    print("| For continuous cash flow, add a 0 to the end of name |")    
    print("| of factors. e.g. (P/F0,10%,10) is:                   |")
    print("| 'Continuous Compounding, Single sum, Present Worth'  |")
    print("| The geometric gradiant factor is also supported which|")
    print("| is in form (P/A1,i,j,n) where j is the common ratio. |")
    print("| Interest rate must be a percentage and persent sign  |")
    print("| is optional. For example:                            |")
    print("|                                                      |")
    print("| Input:(P/A,17,5) >>> (Enter) >>> Command: >>> (Enter)|")
    print("|                                                      |")
    print("| (P/A,17%,5)                                          |")
    print("| =(3.199346162729214)                                 |")
    print("| Ans = 3.199346162729214                              |")
    print("|                                                      |")
    print("|   An Easy Way (Only by a Num Pad):                   |")
    print("|  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   |")
    print("| As well, each factor can be called by its keyword    |")
    print("| using just a Num Pad! Here is some of the keywords:  |")
    print("|                                                      |")
    print("| [1]: F/P   [2]: P/F   [3]: P/A   [4]: F/A   [5]: A/P |")
    print("| [6]: A/F   [7]: A/G   [8]: P/G   [9]: P/A1           |")
    print("|                                                      |")
    print("| An Example for use of this method:                   |")
    print("|                                                      |")
    print("| Input: >>> (Enter) >>> Command:2 >>> (Enter) >>> 20  |")
    print("| >>> (Enter) >>> 3 >>> (Enter) >>> Input: (Enter)     |")
    print("| >>> Command: (Enter)                                 |")
    print("| (P/F,20%,3)                                          |")
    print("| =(0.5787037037037038)                                |")
    print("| Ans = 0.5787037037037038                             |")
    print("|                                                      |")
    print("| You can access to all keywords in help ([04]:help).  |")
    print("|                                                      |")
    print("|   Command Section:                                   |")
    print("|  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   |")
    print("| Press Enter at (Input:) to reach command section.    |")
    print("| (Command:) allows to pass program's keywords like:   |")
    print("| [h] or [03]:View History     [i] or [01]:Instructions|")
    print("| [t] or [02]:Tabulate Factors                         |")
    print("| Pressing Enter on keyboard also reveals the answer.  |")
    print("|______________________________________________________|")
    
def Dfactor(f,i,n): # A discrete cash flow factor is called.
    i = i/100   # conversion
    term = (1+i)**n # This term will be used in answers.
    if (f == "F/P"):
        return term
    elif (f == "P/F"):
        return 1/term
    elif (f == "A/P"):
        return (i*term)/(term-1)
    elif (f == "P/A"):
        return (term-1)/(i*term)
    elif (f == "F/A"):
        return (term-1)/i
    elif (f == "A/F"):
        return i/(term-1)
    elif (f == "A/G"):
        return (1/i)-(n/(term-1))
    elif (f == "P/G"):
        return ((term-1)/(i*i*term))-((n)/(i*term))
    
def Cfactor(f,i,n): # A continuous cash flow factor is called.
    i = i/100   
    e = 2.718281828 # defining Euler's number.
    term = e**(i*n)
    if (f == "F/P"):
        return term
    elif (f == "P/F"):
        return 1/term
    elif (f == "A/P"):
        return (term*((e**n)-1))/(term-1)
    elif (f == "P/A"):
        return (term-1)/(term*((e**n)-1))
    elif (f == "F/A"):
        return (term-1)/((e**i)-1)
    elif (f == "A/F"):
        return ((e**i)-1)/(term-1)
    elif (f == "A/G"):
        return (1/(e**i))-(n/(term-1))
    elif (f == "P/G"):
        return (term-1-(n*((e**i)-1)))/(term*(((e**i)-1))**2)
    
def GGfactor(i,j,n):    #A geometric gradiant factor is called.
    i = (i/100)
    j = (j/100)
    if (j == i):
        return n/(1+i)
    elif (j != i):
        return (1-((1+j)**n)*((1+i)**n))/(i-j)

def Error():    #While an error occurred
    print("\nSyntax Error: Enter a valid input.")
    print("[01]:Instructions")
    print("[04]:Help")

def table(i,s):
    List = ["F/P","P/F","A/F","F/A","A/P","P/A","P/G","A/G"]
    print("\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    if(s == "0"):   #Discrete Cash Flow Chosen
        print("  "+i+"%          Discrete Cash Flow: Compound Interest Factors ")
    if(s == "1"):   #Continuous Cash Flow Chosen
        print("  "+i+"%         Continuous Cash Flow: Compound Interest Factors ")
    print("____________________________________________________________________________")
    print("  Single Payments  |    Uniform Series Payments      | Arithmetic Gradients ")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("n   F/P      P/F      A/F      F/A      A/P      P/A      P/G      A/G      ")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    i = float(i)
    for n in range(1,51):
        print(n,end='')
        if (len(str(n)) == 1):
            print("   ",end='')
        elif (len(str(n)) == 2):
            print("  ",end='')
        for f in range (0,8):
            if(s == "0"):   
                term = str(round(Dfactor(List[f],i,n),5))
                if (len(term) >= 8):
                    term = term[:7]
                dif = 7-len(term)
                print(term,end='')
                spc = -2
                while(dif != spc):
                    spc += 1
                    print(' ',end='') # trailing blank area
            elif(s == "1"): 
                term = str(round(Cfactor(List[f],i,n),5))
                if (len(term) >= 8):
                    term = term[:7]
                dif = 7-len(term)
                print(term,end='')
                spc = -2
                while(dif != spc):
                    spc += 1
                    print(' ',end='') #trailing blank area
        print("\n")
        
def main(Input):    #Calculating Unit (The magic happens here!)
    global mark #Its value is 1 if a factor is quantified.
    mark = 0
    i = ""  #Interest rate
    n = ""  #Number of periods
    j = ""  #Common ratio
    for count in range(0,8):    #Section: Spot Continuous Factor
        try:
            while(Input.find(Factors[count]+"0") != -1): 
                Input = Input.replace("%","")   #ommit any % sign
                i , n = "" , "" #reset data
                y = Input.find(Factors[count]+"0")
                x = y+5     
                while(Input[x] != "," and len(Input) > x):   
                    i = i+Input[x]    #reading i
                    x += 1
                x = x+1 
                while(Input[x] != ")" and len(Input) > x):   
                    n = n+Input[x]    #reading n 
                    x += 1
                i , n = float(i) , float(n)
                Input = Input.replace(Input[y:x],str(Cfactor(Factors[count],i,n)))
                mark = 1 #mark 
        except(ValueError):
            Error()
            
    try:          
        while(Input.find("P/A1") != -1):    #Section: Find Geometric Factor  
            Input = Input.replace("%","")
            i , n , j= "" , "" , "" 
            y = Input.find("P/A1")
            x = y+5     
            while(Input[x] != "," and len(Input) > x):   
                i = i+Input[x]    #reading i
                x += 1
            x = x+1
            print(i)
            while(Input[x] != "," and len(Input) > x):   
                j = j+Input[x]    #reading j
                x += 1
            x = x+1
            while(Input[x] != ")" and len(Input) > x):   
                n = n+Input[x]    #reading n 
                x += 1
            i , j , n = float(i) , float(j) , float(n)
            Input = Input.replace(Input[y:x],str(GGfactor(i,j,n)))
            mark = 1 #mark 
    except(ValueError):
        Error()
        
    for count in range(0,8):    #Section: Find Discrete Factor 
        try:
            while(Input.find(Factors[count]) != -1):
                Input = Input.replace("%","") 
                i , n = "" , ""
                y = Input.find(Factors[count])
                x = y+4
                while(Input[x] != "," and len(Input) > x):   
                    i = i+Input[x]    #reading i
                    x += 1
                x = x+1
                while(Input[x] != ")" and len(Input) > x):    
                    n = n+Input[x]    #reading n
                    x += 1
                i , n = float(i) , float(n)
                Input = Input.replace(Input[y:x],str(Dfactor(Factors[count],i,n)))
                mark = 1 #mark 
        except(ValueError):
            Error()
                   
    for count in range(1,len(Input)):   #Secrion: Defining a(b) as a*b 
        while(Input[count] == "(") and (Input[count-1] in ["0","1","2","3","4","5","6","7","8","9"]):
            Input = Input[:count]+"*"+Input[count:]   

    return Input

def HELP(): #HELP
    print("                                                 ")
    print("======================(Help)=====================")
    print("                                                 ")
    print("Only pressing Enter button on keyboard will      ")
    print("reveal the answer.                               ")
    print("                                                 ")    
    print("Keywords For (Command:):                         ")
    print(" [fp]:F/P    [pf]:P/F    [pa]:P/A    [fa]:F/A    ")
    print(" [ap]:F/P    [af]:P/F    [ag]:P/A    [pg]:F/A    ")
    print(" [fp0]:F/P0  [pf0]:P/F0  [pa0]:P/A0  [fa0]:F/A0  ")
    print(" [ap0]:F/P0  [af0]:P/F0  [ag0]:P/A0  [pg0]:F/A0  ")
    print(" [pa1]:P/A1              [clr]:Clear Input       ")
    print(" [help]:Help             [i]:Instructions        ")
    print(" [h]:View History        [t]:Tabulate            ")
    print("                                                 ")
    print("Num pad keywords:                                ")
    print(" [1]:F/P     [2]:P/F     [3]:P/A     [4]:F/A     ")
    print(" [5]:A/P     [6]:A/F     [7]:A/G     [8]:P/G     ")
    print(" [9]:P/A1    [0]: Clear Input                    ")
    print(" [10]:F/P0   [20]:P/F0   [30]:P/A0   [40]:F/A0   ")
    print(" [50]:A/P0   [60]:A/F0   [70]:A/G0   [80]:P/G0   ")
    print(" [01]:Instructions       [02]:Tabulate           ")
    print(" [03]:View History       [04]:Help               ")
    print("                                                 ")
    print("Note that these keywords work for (Command:).    ")
    print("What is A/P or F/A0? Go to Instructions for more.")
    

          
while(1):   #Program Starting...
    Input = Input+input("\nInput:"+Input)
    print("[1]:F/P    [2]:P/F")
    print("[3]:P/A    [4]:F/A")
    print("[5]:A/P    [6]:A/F")
    print("[7]:A/G    [8]:P/G")
    print("[9]:P/A1   [0]:Clear")
    command = input("Command:")

    if (command == ""):   #Answer Output
        try:
            try:
                print(Input)
                Input = main(Input)
                if (mark == 1):
                    print("="+Input) # Also print factors evaluated. 
                history.append(Input+"\n    Ans = "+str(eval(Input)))   #Add Answer To History 
                print("Ans = "+str(eval(Input)))
            except(SyntaxError):
                Error()
        except(NameError):
            Error() # Error occurred.
        Input = ""  # Clear Input
           
    elif (command in ["1","2","3","4","5","6","7","8"]):   #Discrete Factor
        Input = Input+"("+Factors[int(command)-1]+","
        i = input(Input)
        Input = Input+i+"%,"
        n = input(Input)
        Input = Input+n+")"
        figure = Input
        
    elif (command in SF1):  #Discrete Factor (method2)
        Input = Input+"("+Factors[SF1.index(command)]+","
        i = input(Input)
        Input = Input+i+"%,"
        n = input(Input)
        Input = Input+n+")"
        figure = Input
        
    elif (command in ["10","20","30","40","50","60","70","80"]):   #Countinuous Factor
        Input = Input+"("+Factors[int(command[0])-1]+"0,"
        i = input(Input)
        Input = Input+i+"%,"
        n = input(Input)
        Input = Input+n+")"

    elif (command in SF2):  #Countinuous Factor (method2)
        Input = Input+"("+Factors[SF2.index(command)]+"0,"
        i = input(Input)
        Input = Input+i+"%,"
        n = input(Input)
        Input = Input+n+")"
        figure = Input

    elif (command in ["9","pa1"]):  #Geometric Gradiant Factor
        Input = Input+"(P/A1,"
        i = input(Input)
        Input = Input+i+"%,"
        j = input(Input)
        Input = Input+j+"%,"
        n = input(Input)
        Input = Input+n+")"
        
    elif (command in ["01","i","I"]):   #Instructions 
        instructions()
        
    elif (command in ["02","t","T"]):   #Tabulating
        i = input("Interest Rate:")
        i = (i.replace("%",""))         
        print("[0]:Discrete Cash Flow")
        print("[1]:Continuous Cash Flow")
        s = input("Selection:")
        table(i,s)
        
    elif (command in ["03","h","H"]):   #Calling History
        print("\nHistory:")
        print("¯¯¯¯¯¯¯")
        for count in range(0,len(history)):
            print(history[count])
            
    elif (command in ["0","clr"]): #Clearing Input
        Input = ""  #Clear Input
        
    elif (command in ["help","04"]):    #Help
        HELP() 
    
