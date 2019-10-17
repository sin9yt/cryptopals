# python3 6.py

def compute_hamming(a,b):
    x=''
    y=''
    hamming_distance=0
    for i,j in zip(a,b):
        x ='{:08b}'.format(i)
        y ='{:08b}'.format(j)
        for k,l in zip(x,y):
            if k!=l:
                hamming_distance +=1
    return hamming_distance


def main():
    print(compute_hamming('this is a test'.encode(),'wokka wokka!!!'.encode()))

if __name__ == "__main__":
    main()