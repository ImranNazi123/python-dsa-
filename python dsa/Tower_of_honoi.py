# disk number...
n=3

# source
src="a"
# helper
hlp="b"
# dest
dest="c"

def toh(n,src,hlp,dest):

    # bc
    if n==0:
        return


    # sub-problem....
    # n-1 src to hlp , with the help of dest
    toh(n-1,src,dest,hlp)
    print(f"move {n}th disk from {src} to {dest}")
    # nth-->src to dest with the help of hlp
    toh(n-1,hlp,src,dest)

toh(n,src,hlp,dest)