x=int(input("Enter the larger jug's vol."))
y=int(input("Enter the smaller jug's vol."))
z=int(input("Enter the final vol. of larger jug's vol."))
if(z==y):
    print("\n0 , ",y,"\n")
    print("\n",y,", 0\n")
else:    
    m=x
    n=y
    print("\n0 , 0\n")
    while(x!=z):
        y=0
        print("\n",x," , ",y,"\n")
        x=x-n
        y=n
        print("\n",x," , ",y,"\n")
        y=0
        print("\n",x," , ",y,"\n")
        y=x
        x=0
        print("\n",x," , ",y,"\n")
        x=m
        print("\n",x," , ",y,"\n")
        x=x-(n-y)
        y=n
        print("\n",x," , ",y,"\n")
    
    
