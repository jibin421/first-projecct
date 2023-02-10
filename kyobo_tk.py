# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:09:15 2022

@author: ITWILL
"""
- 교보문고 <트렌드코리아2023> 리뷰분석
- json 형식

from fake_useragent import UserAgent
import urllib.request as req
from urllib.request import urlopen
import json
import time


url = "https://product.kyobobook.co.kr/api/review/list?page=1&pageLimit=2700&reviewSort=001&revwPatrCode=000&saleCmdtid=S000061863239"

ua = UserAgent()
headers = {'User-Agent':ua.random,
           'referer': 'https://product.kyobobook.co.kr/detail/S000061863239'} 

res = urlopen(req.Request(url,headers=headers)).read().decode('utf-8')  #request 한 내용을 read하되, utf-8로 decode해줘

kyobo_tk = DataFrame(json.loads(res)['data'])
kyobo_tk.info()
kyobo_tk['reviewWrite']




# json을 통해서 데이터 추출
kyobo_tk = DataFrame()
failed_url = []

headers = {'User-Agent':ua.random,
           'referer': 'https://product.kyobobook.co.kr/detail/S000061863239'}

for i in range(1,122):
    try:
        url = "https://product.kyobobook.co.kr/api/review/list?page="+str(i)+"&pageLimit=10&reviewSort=001&revwPatrCode=000&saleCmdtid=S000061863239"
        kyobo = urlopen(req.Request(url,headers=headers)).read().decode('utf-8')
        
        kyobo_tk = pd.concat([kyobo_tk,DataFrame(json.loads(kyobo)['data'])],ignore_index=True)
        time.sleep(2)
    except:
        failed_url.append(url)
        time.sleep(2)

kyobo_tk
kyobo_tk.info()
kyobo_tk.select('reviewList > reveCntt')


kyobo_re = kyobo_tk['reviewList']
kyobo_re.info()
len(kyobo_re)

kyobo_re[0]['revwCntt']
kyobo_re[1]['revwCntt']
kyobo_re[10]['revwCntt']
kyobo_re[152]['revwCntt']
kyobo_re[152]['revwCntt']
kyobo_re[1204]['revwCntt']

# review만 추출하기
review = []
for i in range(0,len(kyobo_re)):
    review.append(kyobo_re[i]['revwCntt'])
review
len(review)

import pickle
# review 저장
file = open("c:/project/PYTHON/kyobo_review_tk.txt","wb")  #wb : write모드인데 바이너리 형태
pickle.dump(review,file)
file.close()

# review 읽어오기
file = open("c:/project/PYTHON/kyobo_review_tk.txt","rb")
review = pickle.load(file)
file.close()
review

s = 
type(review)
review.strip()
str_review = str(review)
str_review
str_review.strip()
list(str_review)
df_review = DataFrame(review)

x = DataFrame(review)
x
x.apply(lambda x: re)
# review 전처리하기 
import re

s = '@@@'.join(review)
s.split('@@@')

xx = DataFrame(s.split('@@@'))
xx[0].apply(lambda x : re.sub('\W','',x))

type(xx)

xx.info()


# '@@@'.join(review).split('@@@')

s.find("트렌드른")
s = s.replace("트랜드릀","트렌드를")
s = s.replace("트랜드를","트렌드를")
s = s.replace("트렌드른","트렌드를")
s.replace("투렌드|트랜드","트렌드")

re.findall("[&A-Za-z;]+",s)
s = s.replace("VR판교랜드","브이알판교랜드")
s = s.replace("OO페이를","삼성페이를")
s = s.replace("X세대로","엑스세대로")
s = s.replace("e북","이북")
s = s.replace("Food입니다","푸드입니다")
s = s.replace("SNS를","에스엔에스를")
s = s.replace("MZ세대들의","엠제트세대들의")
s = s.replace("MZ","엠제트")
s = s.replace("Customer","고객")
s = s.replace("Experience","경험")
s = s.replace("Best of best","베스트")
s = s.replace("Meta","메타")
s = s.replace("commerce","무역")
s = s.replace("CPS","씨피에스")
s = s.replace("Chipotle","치폴레")
s = s.replace("BNPL","무이자 할부 결제 서비스")

s = re.sub("[&A-Za-z;]+","",s)

# 공백제거
re.findall("[\n]",s)
s = re.sub("[\n|\r]"," ",s)
s = re.sub("\u200b  \u200b","",s)
re.findall("\u200b", s)
s


s = s.replace("브이알판교랜드","VR판교랜드")
s = s.replace("엑스세대로","X세대로")
s = s.replace("이북","e북")
s = s.replace("에스엔에스를","SNS를")
s = s.replace("엠제트세대들의","MZ세대들의")
s = s.replace("엠제트","MZ")
s = s.replace("씨피에스","CPS")
s = s.replace("무이자 할부 결제 서비스","무이자 할부 결제 서비스(BNPL)")

s = s.replace("굿굿굿입니다","굿입니다")
s = re.sub("좋아묭좋아예이낙ㄴ븐|조아요|좋아요좋아요","좋아요",s)
s = s.replace("아주어뉴좋아요","아주 좋아요")
s = s.replace("도움으","도움이")
s = s.replace("아주조금","아주 조금")
s = s.replace("미리볼수있어","미리 볼 수 있어")
s = s.replace("좋네요도움이되요","좋네요 도움이 돼요")
s = s.replace("매 년","매년")
s


s = s.replace("엿 볼 수 있어요","엿볼 수 있어요")
s = s.replace("ㄱ","추천드려요")
s = s.replace("껏도","것도")
s = s.replace("세성이","세상이")
s = s.replace("삶살아가면","삶 살아가면")
s = s.replace("ㅊ최고에요^^","최고예요")
s = s.replace("최신뉴스를제공","최신뉴스를 제공")
s = s.replace("엄청좋아하네요","엄청 좋아하네요")
s = s.replace("ㅏㅏㅏ","")
s = s.replace("넘넘","너무너무")
s = s.replace("알수 잇어","알 수 있어")
s = s.replace("굿굿","굿")
s = s.replace("이해할수있었어요","이해할 수 있었어요")
s = s.replace("내용도좋고매번구배합니다좋음낸뇨많이있네요 ㅎㅎ","내용도 좋고 매번 구매합니다 좋은 내용 많이 있네요")
s = s.replace("귱금하네요","궁금하네요")
s = s.replace("맥락을살피기","맥락을 살피기")
s = s.replace("책한권읽어요","책 한권 읽어요")
s = s.replace("좋은책입니다","좋은 책입니다")
s = s.replace("잘읽었어요","잘 읽었어요")
s = s.replace("알우있게되어","알 수 있게되어")
s = s.replace("굿굿이군요","굿이군요")
s = s.replace("새로운시각에서","새로운 시각에서")
s = s.replace("재미있을줄","재미있을 줄")
s = s.replace("알수 있어서","알 수 있어서")
s = re.sub("최고최고|최고닝ㅎ","최고",s)
s = s.replace("읽게습니다","읽겠습니다")
s = s.replace("책내주셍","책 내주세요")
s = s.replace("재미있게읽었어요","재미있게 읽었어요")
s = s.replace("트렌드코리아","트렌드 코리아")
s = s.replace("예측할수있어서","예측할 수 있어서")
s = s.replace("꼭읽어보고싶네요~ ㅎ","꼭 읽어보고 싶네요")
s = s.replace("매해감사한마음으로읽는책","매해 감사한 마음으로 읽는 책")
s = s.replace("읽기쉬워","읽기 쉬워")
s = s.replace("좋은정보","좋은 정보")
s = s.replace("읽어보고싶었어요","읽어보고 싶었어요")
s = s.replace("너무재밋고좋아요배송굿","너무 재밌고 좋아요 배송 굿")
s = s.replace("도움이많이되었습니다","도움이 많이 되었습니다")
s = s.replace("좋습니다주변사람들과같이읽고싶네요","좋습니다 주변 사람들과 같이 읽고 싶네요")
s = s.replace("도움이되네요","도움이 되네요")
s = s.replace("트렌트가","트렌드가")
s = s.replace("될거같아요","될 거 같아요")
s = s.replace("좋은책에여","좋은책입니다")
s = s.replace("좋아요추천해요","좋아요 추천해요")
s = s.replace("아주우좋습니다아아아","아주 좋습니다")
s = s.replace("미리알수","미리 알 수")
s = s.replace("속속","쏙쏙")
s = s.replace("너무유익한책이네요","너무 유익한 책이네요")
s = s.replace("예측하는것은","예측하는 것은")
s = s.replace("준비하기위해","준비하기 위해")
s = s.replace("읽을수있어서","읽을 수 있어서")
s = s.replace("걍그럼ㅠㅠㅠㅠㅠㅠㅠ\n","그냥 그럼")
s = s.replace("한해를","한 해를")
s = s.replace("되는책입니딘","되는 책입니다")
s = s.replace("트랜드에맞는","트렌드에 맞는")
s = s.replace("매년초에","매년 초에")
s = s.replace("책나올때마다","책 나올 때마다")
s = s.replace("23년도에","2023년도에")
s = s.replace("현상황파삭에","현재 상황 파악에")
s = s.replace("편하구여","편하구요")
s = s.replace("읽어볼만합니다","읽어볼 만합니다")
s = s.replace("좋은정보알게되어","좋은 정보 알게 되어")
s = s.replace("여러가지로도움","여러 가지로 도움")
s = s.replace("세월흐르는걸","세월이 흐르는걸")
s = s.replace("추천함니다","추천합니다")
s = s.replace("흡인력을","흡입력을")
s = s.replace("치폴레(치폴레)","Chipotle(치폴레)")
s = s.replace("[죽간]","")
s = s.replace("절","잘")
s = s.replace("한해동안의트렌드를","한 해 동안의 트렌드를")
s = s.replace("그해의","그 해의")
s = s.replace("빨랐써요","빨랐어요")
s = s.replace("구입요","구입했습니다")
s = s.replace("감사 합니다.","감사합니다.")
s = s.replace("큰줄기를","큰 줄기를")
s = s.replace("소비트렌드","소비 트렌드")
s = s.replace("트렌드관련","트렌드 관련")
s = s.replace("있지한서도","있지만서도")
s = re.sub("알수있어서","알 수 있어서",s)
s = s.replace("트코는","트렌드 코리아는")
s = s.replace("익을께요","읽을께요")
s = s.replace("나오는.","나오는")
s = re.sub("트랜드","트렌드",s)
s = s.replace("읽어야해여","읽어야 합니다")

s = re.sub("알수 있어","알 수 있어",s)
s = s.replace("트코","트렌드 코리아")
s = re.sub("(-15-)|(-91-)|(-193-)|(-265-)|(-279-)|32|34|33|35|36","",s)
s = s.replace("전원일기 는","전원일기는")
s = s.replace("1854~1866년으","1854년~1866년생으로")
s = s.replace("로런던에서","런던에서")
s = s.replace("개끗한","깨끗한")
s = s.replace("돗시르","도시를")
s = s.replace("이재원 씨는","이재원씨는")
s = s.replace("채과","책과")
s = s.replace("고객경험 ,고객 경험","고객경험(Customer Experience)")
s = s.replace("386 세대를","386세대를")
s = s.replace(" MZ 에게"," MZ에게")
s = s.replace("까페와","카페와")
s = s.replace("MZ 세대에서","MZ세대에서")
s = s.replace("책선물잘했습니다","책 선물 잘했습니다")
s = s.replace("년초마다","연초마다")
s = s.replace("서있는것같다는","서있는 것 같다는")
s = s.replace("재밌게봤스비다","재밌게 봤습니다")
s = s.replace("어떤일들이","어떤 일들이")
s = s.replace("트랜드는","트렌드는")
s = s.replace("알수 있는","알 수 있는")
s = s.replace("항상재밌게보고있어요","항상 재밌게 보고 있어요")
s = s.replace("버라볼","바라볼")
s = s.replace("하는지에대한","하는지에 대한")
s = s.replace("1313433131","")
s = s.replace("매년구입합니다","매년 구입합니다")
s = s.replace("트랜드하게","트렌드하게")
s = s.replace("알려고해야하는","알려고 해야 하는")
s = s.replace("반성할수있는","반성할 수 있는")
s = s.replace("매년읽고있는","매년 읽고 있는")
s = s.replace("트랜드공부에좋습니다","트렌드 공부에 좋습니다")
s = s.replace("내용훌륭하고","내용 훌륭하고")
s = s.replace("찬찬히","천천히")
s = s.replace("와우인크레더블짱장장","좋아요")
s = s.replace("읽어봐야할","읽어봐야 할")
s = s.replace("보통에","보통의")
s = s.replace("한국사회 의","한국사회의")
s = s.replace("트랜드 입니다","트렌드입니다")
s = s.replace("이번에 도","이번에도")
s = s.replace("찐자아를","진짜 자아를")
s = s.replace("좋은말들이꽉참","좋은 말들이 가득 참")
s = s.replace("최곱니다","최고입니다")
s = s.replace("예전 만큼","예전만큼")
s = s.replace("트랜드가","트렌드가")
s = s.replace("매년트렌드를","매년 트렌드를")
s = s.replace("이해하기ㅅ","이해하기")
s = s.replace("이시기에","이 시기에")
s = s.replace("요새같ㅇ","요새같이")
s = s.replace("너무너무좋어요용ㅎㅎ","너무 좋아요")
s = s.replace("도음이","도움이")
s = s.replace("ㅇ돼요","돼요")
s = s.replace("읽어보고싶었던","읽어보고 싶었던")
s = s.replace("내요이","내용이")
s = s.replace("리츄얼","리츄얼(의식절차)")
s = s.replace("도움많이됐어요~좋아요","도움이 많이 됐어요 좋아요")
s = s.replace("읽을수","읽을 수")
s = s.replace("준책이예요","준 책이에요")
s = s.replace("독서 하기에","독서하기에")
s = s.replace("트렌드를이해하기억","트렌드를 이해하기에")
s = s.replace("트랜드에대한이하기좋음","트렌드에 대한 이해하기 좋아요")
s = s.replace("책내용이","책 내용이")
s = s.replace("트랜들","트렌드를")
s = s.replace("코리아으로보고싶다가요","코리아 좋아요")
s = s.replace("재미았어서","재미있어서")
s = s.replace("추천 합니다~","추천합니다")
s = s.replace("잘읽었습니다","잘 읽었습니다")
s = s.replace("좋은내용","좋은 내용")
s = s.replace("이시대를","이 시대를")
s = s.replace("열심이","열심히")
s = s.replace("트렌드에 대해","트렌드에대해")
s = s.replace("알수","알 수")

s = s.replace("마나볼께요","만나볼께요")
s = s.replace("유요ㅇ한 책 입니다","유용한 책입니다.")
s = re.sub("좋은책","좋은 책",s)
s = re.sub("좋을것","좋을 것",s)
s = s.replace("충춘이다","청춘이다")
s = s.replace("완전재밌어요","완전 재밌어요")
s = s.replace("어릴때부더","어릴때부터")
s = s.replace("너무너무유익합니다!","너무 유익합니다")
s = s.replace("리브ㅜ작성합니다구매해","리뷰 작성합니다 구매했어요")
s = s.replace("트렌트는","트렌드는")
s = s.replace("트랜드에","트렌드에")
s = s.replace("생각해볼","생각해 볼")
s = s.replace("내년팬도","내년판도")
s = s.replace("가대됩니다","기대됩니다")
s = re.sub("트랜드","트렌드",s)
s = re.sub("도움돼여|도움되요|도움돼요","도움 돼요",s)
s = s.replace("잘읽고있습니다","잘 읽고 있습니다")
s = s.replace("잘읽고있어요","잘 읽고 있어요")
s = re.sub("이책이","이 책이",s)
s = re.sub("되는것","되는 것",s)
s = s.replace("겉다","같다")
s = s.replace("최고에요","최고예요")
s = s.replace("가나드리오라다가니다로냐나니","가나다")
s = s.replace("읽어볼만한","읽어볼 만한")
s = s.replace("좋아용","좋아요")
s = s.replace("트렌드에대해","트렌드에 대해")
s = s.replace("이해하기쉬웠어요","이해하기 쉬웠어요")
s = s.replace("한번더읽어요","한번 더 읽어요")
s = s.replace("알수있고","알 수 있고")
s = s.replace("괜 ㅏㄴㅎ아요","괜찮아요")
s = s.replace("좋어요","좋아요")
s = s.replace("마움에","마음에")
s = s.replace("와 당ㅎ는","와닿는")
s = s.replace("읽을듯","읽을 듯")
s = s.replace("유익 하고","유익하고")
s = s.replace("준비할수","준비할 수")
s = s.replace("알수있었어요","알 수 있었어요")
s = s.replace("좋아요많은","좋아요 많은")
s = re.sub("소비트렌드","소비 트렌드",s)
s = re.sub("되요","돼요",s)
s = s.replace("있었습니대","있었습니다")
s = s.replace("잘읽혀져요","잘 읽혀요")
s = re.sub("알.수|알수","알 수",s)
s = s.replace("아는듯","아는 듯")
s = s.replace("모르는듯","모르는 듯")
s = s.replace("정리가되는","정리가 되는")
s = s.replace("몰랐던부분을","몰랐던 부분을")
s = s.replace("알수있어요","알 수 있어요")
s = s.replace("바라볼수있습니다","바라볼 수 있습니다")
s = s.replace("트렌드.요즘","트렌드 요즘")
s = s.replace("같은세상","같은 세상")
s = s.replace("다들읽으세요","다들 읽으세요")
s = s.replace("잘읽었는데","잘 읽었는데")
s = re.sub("큰도움","큰 도움",s)
s = s.replace("배워봐오","배워봐요")
s = s.replace("추천드령요","추천드려요")
s = s.replace("글 이라","글이라")
s = s.replace("도움이됩니다","도움이 됩니다")
s = s.replace("기대 됩니다","기대됩니다")
s = s.replace("투렌드","트렌드")
s = s.replace("따뜻한째ㅣ","따뜻한 책")
s = re.sub("이번 년도","이번 연도",s)
s = s.replace("여러번읽게되네요","여러 번 읽게 되네요")
s = s.replace("술술읽어져요","술술 읽어져요")
s = s.replace("좋은자료","좋은 자료")
s = re.sub("트랜드코리아","트렌드 코리아",s)
s = s.replace("잘보고있어요","잘 보고 있어요")

s = s.replace("책이에요^^도움되요","책이에요 도움 돼요")
s = s.replace("미리알 수 있어서","미리 알 수 있어서")
s = s.replace("걍그럼ㅠㅠㅠㅠㅠㅠㅠ","그냥 그럼")
s = s.replace("재미있어요.추천합니다","재미있어요 추천합니다")
s = s.replace("최고선물이에요","최고의 선물이에요")
s = s.replace("도움읻는책이예요","도움이 되는 책이예요")
s = s.replace("역시재밋어요매년사요","역시 재밌어요 매년 사요")
s = s.replace("트렌드.","트렌드")
s = re.sub("이책은","이 책은",s)
s = s.replace("사읽는책","사 읽는 책")
s = s.replace("큰도움이됩니다","큰 도움이 됩니다")
s = s.replace("좋고추천합니다","좋고 추천합니다")
s = s.replace("않아요!절대","않아요")
s = s.replace("속는셈치고","속는 셈 치고")
s = s.replace("불확실성 의","불확실성의")
s = s.replace("큰도움","큰 도움")
s = s.replace("산물로","선물로")
s = s.replace("있엇습니당","있었습니다")
s = s.replace("잘읽었습니다^^","잘 읽었습니다")
s = s.replace("인상적입니당","인상적입니다")
s = s.replace("뿐아니라","뿐만아니라")
s = s.replace("좋은책이네요~^^","좋은 책이네요")
s = s.replace("매년알","내년을")
s = s.replace("볼수","볼 수")
s = s.replace("안받으눙ㅎ","안받아지나요")
s = s.replace("트랜드코리아~","트렌드 코리아")
s = s.replace("도움이많이돱니다","도움이 많이 됩니다")
s = s.replace("추천하고샆습나다","추천하고 싶습니다")
s = s.replace("캐치하좋네요","캐치하고 좋네요")
s = s.replace("읽급니다","읽습니다")
s = s.replace("도움이,","도움이")
s = s.replace("종아ㅛ요","좋아요")
s = s.replace("캐치할수있습미다!","캐치할 수 있습니다")
s = s.replace("재밋이ㅛ습니다","재밌습니다")
s = s.replace("잘읽고","잘 읽고")
s = s.replace("매년읽고있어요","매년 읽고 있어요")
s = re.sub("이책의","이 책의",s)
s = s.replace("가장큰","가장 큰")
s = s.replace("포함하고있습니다","포함하고 있습니다")
s = s.replace("현재사용되는","현재 사용되는")
s = s.replace("잘알려주십니다","잘 알려주십니다")
s = s.replace("283페이지이하","")
s = s.replace("주가의흐름이","주가의 흐름이")
s = s.replace("바뀌는계기","바뀌는 계기")
s = s.replace("있다 라고","있다고")
s = s.replace("209페이지에","")
s = s.replace("테잎과서적을","테이프와 서적을")
s = s.replace("알리는일을","알리는 일을")
s = s.replace("버릴곳없이","버릴 곳 없이")
s = s.replace("183페이지이하","")
s = s.replace("노동시장의변화","노동시장의 변화")
s = s.replace("프리랜서시대","프리랜서 시대")
s = s.replace("저역시","저 역시")
s = s.replace("안봐도되는시리즈입니다","안 봐도 되는 시리즈입니다")
s = s.replace("계속나오는이유가뭘까","계속 나오는 이유가 뭘까")
s = re.sub("읽을수","읽을 수",s)
s = s.replace("너무너무나","너무")
s = s.replace("최고예요추천해요좋아요","최고예요 추천해요 좋아요")
s = s.replace("알수있어서","알 수 있어서")
s = s.replace("많이됐어요!","많이 됐어요")
s = s.replace("너무너무좋아요집중됩니다최고추천","너무 좋아요 집중됩니다 최고 추천")
s = s.replace("이달의책으로","이달의 책으로")
s = s.replace("역쉬,","역시")
s = s.replace("일상트렌드를","일상 트렌드를")
s = s.replace("알수있어서","알 수 있어서")
s = s.replace("뗄수가","뗄 수가")
s = s.replace("좋은내용 이에요.","좋은 내용이에요")
s = s.replace("대박나세요대박나세요대박나세요","대박나세요")
s = s.replace("대박나길바랍니다","대박나길 바랍니다")
s = s.replace("책내용이","책 내용이")
s = s.replace("좋은책 으로보고싶습니다","좋은 책으로 보고 싶습니다")
s = s.replace("정말정말","정말")
s = s.replace("15.16년도를","2015년, 2016년도를")
s = s.replace("있을때","있을 때")
s = s.replace("매년구먀하곴어요","매년 구매하고 있어요")
s = s.replace("아주맘에듭니다","아주 마음에 듭니다")
s = s.replace("읽기편해요","읽기 편해요")
s = s.replace("서저","서적")
s = s.replace("좋아요종아요좋아요아료","좋아요")
s = s.replace("기대됩니다.많은도움이","기대됩니다 많은 도움이")
s = s.replace("ㅎㅎㅎㅎ헤헤","")
s = s.replace("가타요","같아요")
s = s.replace("될것","될 것")
s = s.replace("좋어요~~~~","")
s = s.replace("도움이돼요","도움이 돼요")
s = s.replace("좋은책","좋은 책")
s = s.replace("죄는","되는")
s = s.replace("갓도","것도")
s = s.replace("리후레쉬","리프레시")
s = s.replace("너무좋아요","너무 좋아요")
s = s.replace("맘에들어요..","맘에 들어요")
s = s.replace("잘읽겠습닏ᆢ^^감사합니다","잘 읽겠습니다 감사합니다")
s = s.replace("도움이돼요","도움이 돼요")
s = s.replace("찐","진짜")
s = s.replace("알기쉽게","알기 쉽게")
s = s.replace("됩니더ㅜ좋아요","됩니다 좋아요")
s = s.replace("좋은것 같아요.","좋은 것 같아요")
s = s.replace("와닿고재미있어요","와닿고 재미있어요")
s = s.replace("드랜드","트렌드")
s = s.replace("유익해요.올해의","유익해요 올해의")
s = s.replace("도움이됩니다","도움이 됩니다")
s = s.replace("파악 하기","파악하기")
s = s.replace("보겄습니다","보겠습니다")
s = s.replace("알수있어서","알 수 있어서")
s = s.replace("감사합니다감사합니다","감사합니다")
s = s.replace("너무좋아요너무좋아요","너무 좋아요")
s = s.replace("시간날때마다..좋어요","시간 날 때마다 좋아요")
s = s.replace("조어ㅕ","")
s = s.replace("트랜드에","트렌드에")
s = s.replace("명퀘한","명쾌한")
s = s.replace("읽어보고싶어용ㅎㅎ","읽어보고 싶어요")
s = s.replace("좋아요너무너무너무너무","좋아요")
s = s.replace(" 믿고봅니다.~~","믿고 봅니다")
s = s.replace("되는걸까요??","되는 걸까요")
s = s.replace("읽고싶은책입니다.","읽고 싶은 책입니다")
s = s.replace("좋아요ㅎ유용한정보입니다","좋아요 유용한 정보입니다")
s = s.replace("필요할것","필요할 것")
s = s.replace("트코!!","트렌드 코리아")

# 특수문자 제거
s = re.sub("#557#56842","",s)
s = re.sub("[♡]","",s)
s = re.sub("[!^~,*?#\\$()]","",s)
s = re.sub("\.","",s)

# 년도 치환하기
s = re.sub("2023도|23년을|2023을|2023|2023과|23년","2023년",s)
s = re.sub("2023년년을|2023년년|23년|2023년년의","2023년",s)
re.findall("202023년",s)
s = re.sub("202023년","2023년",s)
re.findall("202023년",s)

s = re.sub("2022|2022를|2022의","2022년",s)
re.findall("2022년",s)
s = s.replace("2021도","2021년도")
re.findall("2021년",s)

s = s.replace("2023트렌드","2023년 트렌드")
re.findall("2023년 트렌드",s)

s = s.replace("2023년트렌드","2023년 트렌드")
re.findall("2023년 트렌드",s)

s = s.replace("23년인데","2023년인데")
re.findall("2023년인데",s)
s = s.replace("22년에","2022년에")
re.findall("2022년에",s)
s = s.replace("2022년년에","2022년의")
re.findall("2022년년에",s)

s = s.replace("2023년을잘준비해봐야겠어요^^","2023년을 잘 준비해 봐야겠어요")
re.findall("2023년",s)
s

re.findall("[0-9]+년",s)
s = s.replace("202022년","2022년")
re.findall("202022년",s)
s = s.replace("202023년","2023년")
re.findall("202023년",s)

re.findall("[0-9]+[가-힣]+",s)
s = s.replace("2022년년","2022년")
re.findall("2022년년",s)

s = s.replace("트랜드코리아2023년","트렌드 코리아 2023년")
s = s.replace("2023년준비하는시점에서","2023년 준비하는 시점에서")
s = s.replace("2023년에는모든","2023년에는 모든")
s = s.replace("2023년잘준비해봐야겠어요","2023년 잘 준비해봐야겠어요")
s = s.replace("22년것도","2022년 것도")

re.findall("[0-9]+[가-힣]+\s[가-힣]+",s)
s = s.replace("10가지평균","10가지 평균")
s = s.replace("10가지챕터가","10가지 챕터가")
s = s.replace("2023년 을","2023년을")

re.findall("[가-힣]+[0-9]+",s)
s = s.replace("년1866","년, 1866년")
s = s.replace("좋아요131131","좋아요")
s = s.replace("코리아2023","코리아 2023")
s = s.replace("트렌드코리아2023","트렌드 코리아 2023")
s = s.replace("선물이기바랍니다2023","선물이길 바랍니다 2023")

re.findall("[0-9]+\s[가-힣]+",s)
s = re.sub("1","1,",s)

re.findall("[0-9]+\,\s[가-힣]+",s)



# s 저장
file = open("c:/project/PYTHON/kyobo_review_tk_s.txt","wb")  #wb : write모드인데 바이너리 형태
pickle.dump(s,file)
file.close()




s = s.replace("트랜드코리아2023년","트렌드 코리아 2023년")
s = s.replace("2023년년을잘준비해봐야겠어요^^","2023년을 잘 준비해봐야겠어요")
s = s.replace("2023년년에는모든","2023년에는 모든")
s = s.replace("2023년트렌드","2023년 트렌드")
s = re.sub("2023년년도의","2023년도의",s)
s = re.sub("2023년년이","2023년이",s)
s = s.replace("2023년년도를","2023년도를")
s = s.replace("2022년년의","2022년의")
s = s.replace("2023년년도의","2023년도의")
s = s.replace("2023년년이","2023년이")
s = s.replace("코리아2023년","코리아 2023년")
s = s.replace("23년도를","2023년도를")
s = s.replace("23년에","2023년에")
s = s.replace("2022년년","2022년")
s = s.replace("2023년 을","2023년을")
s = s.replace("2023년년의","2023년의")
s = s.replace("2022년-23년","2022년, 2023년")

s = re.sub("2022년년","2022년",s)
s = s.replace("23년의ㅈ트렌드를","2023년의 트렌드를")
s = s.replace("2023년년트렌드","2023년 트렌드")
s = s.replace("2022년년도","2022년도")
s = s.replace("2023년년에는","2023년에는")
s = s.replace("코리아2023년","코리아 2023년")
s = re.sub("2023년년은","2023년은",s)
s = re.sub("2023년년을","2023년을",s)
s = s.replace("2023년년을준비하는시점에서","2023년을 준비하는 시점에서")
s = re.sub("23년도의","2023년도의",s)




s
s.replace("","")


s = s.replace("","")
s = s.replace("","")
s = s.replace("","")
s = s.replace("","")
s = s.replace("","")







&lsquo;손님&rsquo;


import re
re.findall("트랜드릀",str_review)
re.findall("트랜드릀",review)
re.findall("트랜드릀",df_review)
compile("트랜드릀",review).findall("트랜드릀")

review.replace("트랜드릀","트랜드를")

str(review).replace("트랜드릀","트랜드를")
review.contains("트렌드릀")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-list 형식에서의 한글 전처리를 하고싶은데 방법을 못찾겠음. 
일단 str형식으로 변경 후 전처리하기 

str_review = str_review.strip()
str_review.replace([])




