import sys


data = []
while True:
    print("===========================")
    print("1. 데이터 추가")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("5. 데이터 확인")
    print("0. 종료")
    menu = int(sys.stdin.readline())
    if menu == 1:
        data.append([])
        print("===========================")
        print("학생의 학과를 입력하세요 : ", end = '')
        data[-1].append(sys.stdin.readline().rstrip())
        print("학생의 학번을 입력하세요 : ", end = '')
        data[-1].append(int(sys.stdin.readline()))
        print("학생의 이름을 입력하세요 : ", end = '')
        data[-1].append(sys.stdin.readline().rstrip())
        print("학생의 국어, 영어, 수학 점수를 입력하세요 : ", end = '')
        data[-1].extend(list(map(int, sys.stdin.readline().split())))
        data[-1].append(sum(data[-1][3:]))
        data[-1].append(data[-1][-1]/3)
        if data[-1][-1] >= 95:
            data[-1].append('A+')
        elif data[-1][-1] >= 90:
            data[-1].append('A0')
        elif data[-1][-1] >= 85:
            data[-1].append('B+')
        elif data[-1][-1] >= 80:
            data[-1].append('B0')
        elif data[-1][-1] >= 75:
            data[-1].append('C+')
        elif data[-1][-1] >= 70:
            data[-1].append('C0')
        elif data[-1][-1] >= 65:
            data[-1].append('D+')
        elif data[-1][-1] >= 60:
            data[-1].append('D0')
        else:
            data[-1].append('F')

    elif menu == 2:
        print("===========================")
        print("검색할 학생의 학번 혹은 이름을 입력하세요 : ", end = '')
        search = sys.stdin.readline().rstrip()
        temp = False
        try:
            search = int(search)
            for i in range(len(data)):
                if search == data[i][1]:
                    temp = True
                    print("학과 :",data[i][0],"학번 :",data[i][1],"이름 :",data[i][2], "국어 점수 :",data[i][3], "영어 점수 :", data[i][4], "수학 점수 :",data[i][5], "총점 :", data[i][6], "평균 :", data[i][7], "학점 :", data[i][8])
                    break
            if not temp:
                print("검색에 실패하였습니다.")
        except:
            for i in range(len(data)):
                if search == data[i][2]:
                    temp = True
                    print("학과 :",data[i][0],"학번 :",data[i][1],"이름 :",data[i][2], "국어 점수 :",data[i][3], "영어 점수 :", data[i][4], "수학 점수 :",data[i][5], "총점 :", data[i][6], "평균 :", data[i][7], "학점 :", data[i][8])
                    break
            if not temp:
                print("검색에 실패하였습니다.")
    elif menu == 3:
        print("===========================")
        print("삭제할 학생의 학번과 이름을 입력하세요 : ", end = '')
        search = sys.stdin.readline().split()
        search[0] = int(search[0])
        temp = False
        for i in range(len(data)):
            if search[0] == data[i][1]:
                if search[1] == data[i][2]:
                    temp = True
                    data.pop(i)
                    print("해당 학생의 정보를 삭제하였습니다.")
        if not temp:
            print("삭제에 실패하였습니다.")
    elif menu == 4:
        print("===========================")
        print("학과로 정렬하시겠습니까 학번으로 정렬하시겠습니까? : ", end = '')
        sort = sys.stdin.readline().rstrip()
        if sort == "학과":
            for i in range(len(data)):
                for j in range(i+1, len(data)):
                    if data[i][0] > data[j][0]:
                        data[i][0], data[j][0] = data[j][0], data[i][0]
            print("학과 순으로 데이터를 정렬하였습니다.")
        elif sort == "학번":
            for i in range(len(data)):
                for j in range(i+1, len(data)):
                    if data[i][1] > data[j][1]:
                        data[i][1], data[j][1] = data[j][1], data[i][1]
            print("학과 순으로 데이터를 정렬하였습니다.")
        else:
            print("잘못된 입력입니다.")
    elif menu == 5:
        print("===========================")
        for i in range(len(data)):
            print("학과 :",data[i][0],"학번 :",data[i][1],"이름 :",data[i][2], "국어 점수 :",data[i][3], "영어 점수 :", data[i][4], "수학 점수 :",data[i][5], "총점 :", data[i][6], "평균 :", data[i][7], "학점 :", data[i][8])
    elif menu == 0:
        print("===========================")
        break
    else:
        print("===========================")
        print("잘못된 입력입니다.")