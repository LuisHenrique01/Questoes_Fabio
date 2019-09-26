def main():
    tabuada()

def tabuada():
    for i in range(1, 11):
        print('--------- %i ---------'%i)
        for j in range(1, 11):
            print('%i * %i = %i'%(i, j, i*j))
            

if __name__ == '__main__':
    main()