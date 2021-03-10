

if __name__ == '__main__':
    total=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score = [score, name]
        total.append(name_score)
    
    total.sort()
    grade=total[0][0]

    for i in range(1,len(total)):
        if grade < total[i][0]:
            grade=total[i][0]
            break
        
    for i in range (1, len(total)):
        if total[i][0]== grade:
            print(total[i][1])

            
