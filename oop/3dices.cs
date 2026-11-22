import random 

def main():
    random_gen = random.Random()
    
    t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for j in range(100000):
        dice1= random_gen.randint(1,6)
        dice2= random_gen.randint(1,6)
        dice3 = random_gen.randint(1, 6)
        rst = dice1 + dice2 + dice3
        t[rst - 3] += 1
        
    for i in range(len(t)):
        print(i+3, t[i])
    

if __name__ == "__main__":
    main()