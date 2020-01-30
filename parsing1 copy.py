import re
text = '''
SMILE STRAP ver.1 2,900*3=8,700
지브라 SK 사보+1 멀티펜 리필심 1,500*1=1,500
지브라 SK 사보+1 멀티펜 리필심 1,500*3=4,500
모니터 메모보드-30cm 세트 7,200*1=7,200
5th limited edition MD노트 COTTON - S 11,800*1=11,800
5th limited edition MD노트 COTTON - M 13,500*1=13,500
패턴페이퍼백 Ver.2 2,500*1=2,500
패턴페이퍼백 Ver.2 2,500*1=2,500
패턴페이퍼백 Ver.2 2,500*1=2,500
모리스 노크식 s 마일드라이너 형광펜 1,800*1=1,800
모리스 노크식 s 마일드라이너 형광펜 1,800*1=1,800
Penco Knock Ballpoint Pen 3,200*1=3,200
Penco Knock Ballpoint Pen 3,200*1=3,200
Penco Knock Ballpoint Pen 3,200*1=3,200
Penco Knock Ballpoint Pen 3,200*1=3,200
Penco Knock Ballpoint Pen 3,200*1=3,200
Desk Tray - S 11,700*2=23,400
Desk Tray - S 11,700*2=23,400
Desk Tray - S 11,700*1=11,700
(NEW COLOR)파일롯 프릭션 볼노크 4컬러 멀티 젤잉크펜05 16,900*1=16,900
클릭골드 패션 볼펜 1,100*3=3,300
클릭골드 패션 볼펜 1,100*1=1,100
클릭골드 패션 볼펜 1,100*1=1,100
MD 노트 커버 [紙] 10th Cordoba 브라운 (S) 10,000*1=10,000
MD 노트 커버 [紙] 10th Cordoba 카멜 (M) 12,000*1=12,000
[maeily] 페이퍼 백(10개 SET) 2,500*1=2,500
CBB Paper pack 04 2,800*2=5,600
CBB Paper pack 04 2,800*2=5,600
Penco Blue Glue Pen 5,700*4=22,800
Penco Coils Notebook - M 8,050*1=8,050
Penco Coils Notebook - M 8,050*1=8,050
Penco Storage Container (4 ps -1 set) 21,950*1=21,950
Record of Life 15,000*1=15,000
Carton Opener - Khaki 12,000*3=36,000
A4 무무랩 L홀더 낱개_(1593629) 120*10=1,200
제브라 클립온 멀티펜 T 0.7mm 4색볼펜 + 0.5mm 샤프_(1640069) 9,200*1=9,200
12색 따뜻한색 푸르른색 단색 마스킹 테이프_(1083464) 9,600*1=9,600
그린 트와인끈 2,500*1=2,500
오트밀끈 2,500*1=2,500
고무줄 철팁 블랙(10개) 1,200*1=1,200
소프트커버 방수노트 S 7,900*1=7,900
배송비 10,000*1=10,000
'''
index = 0
indexs = list()
products = list()
prices = list()
quantities = list()
total = list()

# text = text.split('\n')
value = re.findall('=\s*([0-9,]+,*)',text)

for v in value:
    v = v.replace(",","")
    # print(v)
    prices.append(int(v))
number = 0
print(len(prices),sum(prices))



# number = 0
# for line in text:
    
# index = 0

# for line in text:    
#     value = re.findall('([0-9,]*[0-9]+)원',line)
#     if len(value)  < 2 : continue
#     index += 1
#     print(index, value)
#     prices.append(value)
#     p1=value[0].replace(",", "")
#     p2=value[1].replace(",", "")
#     quantity = int(p2)/int(p1)
#     quantities.append(int(quantity))
#     # print(quantities)
#     # parsingValue = value[0].split('\t')
#     # print(parsingValue[0])
# #     index += 1
# # print(products)
# print(prices)
# print(len(products),len(quantities), len(prices))
# f = open('test.txt','w+')
# for i in range(len(products)):
#     txt = products[i]+" "+prices[i][0]+"*"+str(quantities[i])+"="+ prices[i][1]+"\n"
#     f.write(txt)
