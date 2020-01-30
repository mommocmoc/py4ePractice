import re
text = '''
160666
텐바이텐
SMILE STRAP ver.1	
SMILE STRAP ver.1
01 ivory
2,900원	3	8,700원	출고완료
271554
텐바이텐
지브라 SK 사보+1 멀티펜 리필심	
지브라 SK 사보+1 멀티펜 리필심
레드
1,500원	1	1,500원	출고완료
271554
텐바이텐
지브라 SK 사보+1 멀티펜 리필심	
지브라 SK 사보+1 멀티펜 리필심
블루
1,500원	3	4,500원	출고완료
554875
텐바이텐
모니터 메모보드-30cm 세트	
모니터 메모보드-30cm 세트
8,000원
7,200원	1	7,200원	출고완료
856711
텐바이텐
5th limited edition MD노트 COTTON - S	
5th limited edition MD노트 COTTON - S
11,800원	1	11,800원	출고완료
856713
텐바이텐
5th limited edition MD노트 COTTON - M	
5th limited edition MD노트 COTTON - M
13,500원	1	13,500원	출고완료
1355929
텐바이텐
패턴페이퍼백 Ver.2	
패턴페이퍼백 Ver.2
Flamingo
2,500원	1	2,500원	출고완료
1355929
텐바이텐
패턴페이퍼백 Ver.2	
패턴페이퍼백 Ver.2
Winter fox
2,500원	1	2,500원	출고완료
1355929
텐바이텐
패턴페이퍼백 Ver.2	
패턴페이퍼백 Ver.2
Tulip
2,500원	1	2,500원	출고완료
1511330
텐바이텐
모리스 노크식 s 마일드라이너 형광펜	
모리스 노크식 s 마일드라이너 형광펜
민트
1,800원	1	1,800원	출고완료
1511330
텐바이텐
모리스 노크식 s 마일드라이너 형광펜	
모리스 노크식 s 마일드라이너 형광펜
그레이
1,800원	1	1,800원	출고완료
1666107
텐바이텐
Penco Knock Ballpoint Pen	
Penco Knock Ballpoint Pen
Black
3,500원
3,200원	1	3,200원	출고완료
1666107
텐바이텐
Penco Knock Ballpoint Pen	
Penco Knock Ballpoint Pen
Turquoise Blue
3,500원
3,200원	1	3,200원	출고완료
1666107
텐바이텐
Penco Knock Ballpoint Pen	
Penco Knock Ballpoint Pen
Blue
3,500원
3,200원	1	3,200원	출고완료
1666107
텐바이텐
Penco Knock Ballpoint Pen	
Penco Knock Ballpoint Pen
Wine
3,500원
3,200원	1	3,200원	출고완료
1666107
텐바이텐
Penco Knock Ballpoint Pen	
Penco Knock Ballpoint Pen
Green
3,500원
3,200원	1	3,200원	출고완료
1686621
텐바이텐
Desk Tray - S	
Desk Tray - S
Gray
12,000원
11,700원	2	23,400원	출고완료
1686621
텐바이텐
Desk Tray - S	
Desk Tray - S
Navy
12,000원
11,700원	2	23,400원	출고완료
1686621
텐바이텐
Desk Tray - S	
Desk Tray - S
Dark Green
12,000원
11,700원	1	11,700원	출고완료
1716832
텐바이텐
(NEW COLOR)파일롯 프릭션 볼노크 4컬러 멀티 젤잉크펜05	
(NEW COLOR)파일롯 프릭션 볼노크 4컬러 멀티 젤잉크펜05
라이트블루
16,900원	1	16,900원	출고완료
1770667
텐바이텐
클릭골드 패션 볼펜	
클릭골드 패션 볼펜
1.화이트
1,500원
1,100원	3	3,300원	출고완료
1770667
텐바이텐
클릭골드 패션 볼펜	
클릭골드 패션 볼펜
14.다크그린
1,500원
1,100원	1	1,100원	출고완료
1770667
텐바이텐
클릭골드 패션 볼펜	
클릭골드 패션 볼펜
17.로열블루
1,500원
1,100원	1	1,100원	출고완료
1920435
텐바이텐
MD 노트 커버 [紙] 10th Cordoba 브라운 (S)	
MD 노트 커버 [紙] 10th Cordoba 브라운 (S)
10,000원	1	10,000원	출고완료
1920475
텐바이텐
MD 노트 커버 [紙] 10th Cordoba 카멜 (M)	
MD 노트 커버 [紙] 10th Cordoba 카멜 (M)
12,000원	1	12,000원	출고완료
1924688
텐바이텐
[maeily] 페이퍼 백(10개 SET)	
[maeily] 페이퍼 백(10개 SET)
02_체크
2,500원	1	2,500원	출고완료
1994755
텐바이텐
CBB Paper pack 04	
CBB Paper pack 04
Bird
2,800원	2	5,600원	출고완료
1994755
텐바이텐
CBB Paper pack 04	
CBB Paper pack 04
Ribbon
2,800원	2	5,600원	출고완료
2026996
텐바이텐
Penco Blue Glue Pen	
Penco Blue Glue Pen
6,500원
5,700원	4	22,800원	출고완료
2026998
텐바이텐
Penco Coils Notebook - M	
Penco Coils Notebook - M
Natural
9,500원
8,050원	1	8,050원	출고완료
2026998
텐바이텐
Penco Coils Notebook - M	
Penco Coils Notebook - M
Red
9,500원
8,050원	1	8,050원	출고완료
2027280
텐바이텐
Penco Storage Container (4 ps -1 set)	
Penco Storage Container (4 ps -1 set)
WHITE
32,000원
21,950원	1	21,950원	출고완료
2123178
텐바이텐
Record of Life	
Record of Life
다크브라운(dark-brown
15,000원	1	15,000원	출고완료
2307997
텐바이텐
Carton Opener - Khaki	
Carton Opener - Khaki
12,000원	3	36,000원	출고완료
2397671
업체개별
A4 무무랩 L홀더 낱개_(1593629)	
A4 무무랩 L홀더 낱개_(1593629)
반투명
120원	10	1,200원	출고완료
2456307
업체개별
제브라 클립온 멀티펜 T 0.7mm 4색볼펜 + 0.5mm 샤프_(1640069)	
제브라 클립온 멀티펜 T 0.7mm 4색볼펜 + 0.5mm 샤프_(1640069)
퓨어그린
9,200원	1	9,200원	출고완료
2192479
업체개별
12색 따뜻한색 푸르른색 단색 마스킹 테이프_(1083464)	
12색 따뜻한색 푸르른색 단색 마스킹 테이프_(1083464)
12색 마스킹테이프:소형-푸르른색
9,600원	1	9,600원	출고완료
2031535
업체개별
그린 트와인끈	
그린 트와인끈
2,500원	1	2,500원	출고완료
1735724
업체개별
오트밀끈	
오트밀끈
2,500원	1	2,500원	출고완료
1670610
업체개별
고무줄 철팁 블랙(10개)	
고무줄 철팁 블랙(10개)
1,200원	1	1,200원	출고완료
1530814
업체개별
소프트커버 방수노트 S	
소프트커버 방수노트 S
옐로우 (374-M)
7,900원	1	7,900원	출고완료
'''
index = 0
indexs = list()
products = list()
prices = list()
quantities = list()
total = list()

text = text.split('\n')
number = 0
for line in text:
    index +=1
    if line.startswith("텐바이텐") > 0 :
        # print(index, line)
        number +=1
        print(number, text[index])
        products.append(text[index].rstrip('\t'))
        
    elif line.startswith("업체개별") > 0 :
        # print(text[index])
        number +=1
        print(number, text[index])
        products.append(text[index].rstrip('\t'))
index = 0

for line in text:    
    value = re.findall('([0-9,]*[0-9]+)원',line)
    if len(value)  < 2 : continue
    index += 1
    print(index, value)
    prices.append(value)
    p1=value[0].replace(",", "")
    p2=value[1].replace(",", "")
    quantity = int(p2)/int(p1)
    quantities.append(int(quantity))
    # print(quantities)
    # parsingValue = value[0].split('\t')
    # print(parsingValue[0])
#     index += 1
# print(products)
print(prices)
print(len(products),len(quantities), len(prices))
f = open('test.txt','w+')
for i in range(len(products)):
    txt = products[i]+" "+prices[i][0]+"*"+str(quantities[i])+"="+ prices[i][1]+"\n"
    f.write(txt)
