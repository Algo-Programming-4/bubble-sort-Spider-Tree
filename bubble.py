#Dimitri Workman
#Sept-30-2024
#Bubble Sort


def bubble(item):
    for i in range(len(item)-1):
        skip=True
        for j in range(len(item)-i-1):
            a=item[j]
            b=item[j+1]
            if a>b:
                item[j]=b
                item[j+1]=a
                skip=False
        if (skip):
           break
    return item

def main():
    apple=[1,3,4,2,5,6,1,8]
    print(bubble(apple))


#calls program
if __name__ =="__main__":
    main()
