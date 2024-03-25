range_check=range(0,121,20)
progress=0
Trailer=0
Retriever=0
Exclude=0
progresslist=[]
Trailerlist=[]
Retrieverlist=[]
Excludelist=[]
Text=[]
studentlist={}

def print_outcome(scorelist,name):
    for x in range(len(scorelist)):
        print(name,scorelist[x])
def append_outcome(scorelist,name):
    for x in range(len(scorelist)):
        Text.append((name+str(scorelist[x])))

while True:
    studentid=str(input("Enter student ID :"))
    try:
        pass1=int(input("Please enter your credits at pass :"))
        if pass1 not in range_check:
            print("Out Of range")
            continue
        defer=int(input("Please enter your credit at differ :"))
        if defer not in range_check:
            print("Out Of range")
            continue
        fail=int(input("Please enter your credit at fail :"))
        if fail not in range_check:
            print("Out Of range")
            continue
        
    except ValueError:
        print("Integer required")
        print("")
        continue
    total=pass1+defer+fail
    if total>120:
        print("Total Incorrect")
        
    elif pass1==100 and defer==20 and fail==0:
        print("progress(module trailer)")
        Trailer+=1
        Trailerlist.append((pass1,defer,fail))
        marks="Trailer - "+str(pass1)+","+str(defer)+","+str(fail)
        studentlist[studentid]=marks
        
    elif pass1==120 and defer==0 and fail==0:
        print("progress")
        progress+=1
        progresslist.append((pass1,defer,fail))
        marks="Progress - "+str(pass1)+","+str(defer)+","+str(fail)
        studentlist[studentid]=marks
        
    elif pass1==100 and defer==0 and fail==20:
        print("Progress (module trailer)")
    elif pass1>=0 and defer>=0 and fail>=80:
        print("Exclude")
        Exclude+=1
        Excludelist.append((pass1,defer,fail))
        marks="Exclude - "+str(pass1)+","+str(defer)+","+str(fail)
        studentlist[studentid]=marks
        
    else  :
        print("Do not progress-Module Retriever")
        Retriever+=1
        Retrieverlist.append((pass1,defer,fail))
        marks="Retriever - "+str(pass1)+","+str(defer)+","+str(fail)
        studentlist[studentid]=marks
    end_continue=str(input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:"))
    if end_continue!='q':
        continue
        

    progress_star = "*"*progress
    trailer_star = "*"*Trailer
    retreiver_star = "*"*Retriever
    exclude_star = "*"*Exclude

    total=progress+Trailer+Retriever+Exclude

    print(f"""
    -----------------------------------------------------------------------
    Histogram
    Progress {progress} : {progress_star}
    Trailer {Trailer} : {trailer_star}
    Retreiver {Retriever} : {retreiver_star}
    Exclude {Exclude} : {exclude_star}

    {total} outcomes in total
    ----------------------------------------------------------------------
    """)
    print("Enter 1 to View the outcomes in the list")
    print("Enter 2 to store and view View the outcomes in the text file")
    print("Enter 3 to get the dictionary ")

    while True:
        try:
             opt=int(input("Enter your option :"))
        except:
            continue
    
                            
        if opt==1:
            
                print_outcome(progresslist,"progress - ")
                print_outcome(Trailerlist,"Trailer - ")
                print_outcome(Retrieverlist,"Retriever - ")    
                print_outcome(Excludelist,"Exclude - ")
                continue
        if opt==2:
                append_outcome(progresslist,"progress - ")
                append_outcome(Trailerlist,"Trailer - ")
                append_outcome(Retrieverlist,"Retriever - ")    
                append_outcome(Excludelist,"Exclude - ")

                file=open('COURSE.txt','w')
                for outcome in Text:
                    course=file.write(outcome)
                    course=file.write('\n')
                    file.flush
                file.close()

                file=open('COURSE.txt','r')
                course=file.read()
                print(course)
                file.close()
                continue
        if opt==3:
               print(studentlist)
        
                
    
