ml=3
cl=3
mr=0
cr=0
while(ml!=0 and cl!=0):
    print("\n",ml,cl," , ",mr,cr,"\n")
    ml=ml-1
    cl=cl-1
    mr=mr+1
    cr=cr+1
    print("\n",ml,cl," , ",mr,cr,"\n")
    if(ml==0 and cl==0):
        import sys
        sys.exit(0)
    cl=cl+1
    cr=cr-1
    print("\n",ml,cl," , ",mr,cr,"\n")
    cl=cl-2
    cr=cr+2
    print("\n",ml,cl," , ",mr,cr,"\n")
    cl=cl+1
    cr=cr-1
