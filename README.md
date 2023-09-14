<details >
<summary>Titanic From Disater_타이타닉 참사</summary>

### DDA 분석
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | ---|
|PassengerId| 유니크id | | unique id의 경우 데이터로 사용 불가 판단 | 
| survival | Survival | 0 = No, 1 = Yes | 범주형(명목형), 생존과 죽음의 두가지 종류이기 때문에 범주형으로 판단됨|
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형(순서형), 등급이 부여된 티켓이기 때문에 범주형으로 판단됨 |
| sex | Sex | | 범주형(명목형) |
| Age | Age in years | | 수치형(이산형) | 
| sibsp | # of siblings / spouses aboard the Titanic | | 범주형(순서형), 형제자매의 특정 수치이며 범주별 빈도를 분석해야 함  |
| parch | # of parents / children aboard the Titanic | |범주형(순서형), 범주형으로 빈도를 파악해야 함 |
| ticket | Ticket number | | 범주형(순서형) |
| fare | Passenger fare | | 수치형(이산형), 각 요금별 승객의 수를 파악하는데 사용할 수 있음 |
| cabin | Cabin number | | 범주형(순서형)|
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형(명목형) |


</details>


<details >
<summary>Type Of Contract Channel_계약 유형 채널</summary>
from dataset : https://blog.naver.com/data_station/222493245799

### DDA 분석
| Variable |Definition | Key | 데이터 분류   | 분석가 의견 |
|---|---|---|---|---|
| id | 각 레코드의 고유 식별자 |  | 범주형(명목형)  | unique id의 경우 데이터로 사용 불가 판단  |
| type_of_contract  | 계약 유형    | 렌탈, 멤버십 | 범주형(명목형) | 각 계약 유형사이의 순서의 정보가 없음으로 명목형 |
| type_of_contract2 | 다른 유형의 계약 |       |범주형(명목형) | 명확한 순서가 나타나있지 않기때문에 명목형|
| channel  | 계약을 획득한 경로  |       |범주형(명목형)| 서로 비교할 수 없는 의미적인 관계이기에 명목형|
| datetime          | 레코드의 날짜와 시간  |       | 수치형(연속형)| 날짜이기 때문에 연속형으로 판단됨 |
| Term              | 계약 기간 (달)   |       |수치형(연속형) |  |
| payment_type      | 지불 방식   |       | 범주형(명목형) |  |
| product           | 계약과 관련된 제품   | K1 ~ k6 |범주형(명목형)| 각 제품 유형은 서로 다른 범주로 분류, 서로 비교 할 수 없는 의미적 관계  |
| amount            | 계약과 관련된 금액  |       | 수치형(이산형) |   |
| state             | 계약의 주 또는 지역  |       |범주형(명목형) |   |
| overdue_count     | 계약이 연체된 횟수  |       | 수치형(이산형)| 연체된 횟수를 파악해야 함|
| overdue           | 현재 계약이 연체 중인지 여부 |  있음, 없음     | 범주형(명목형)|  연체 여부의 유무만을 나타내기 때문에 비교 가능한 의미적인 순서가 없음|
| credit rating     | 고객의 신용 등급  | 1.0 ~ 10.0      |범주형(명목형)| 데이터 확인결과 연산이 가능한 의미적인 순서가 아니기에 순서가 의미 없는 명목형 데이터|
| bank              | 계약과 연관된 은행 |       | 범주형(명목형)|   |
| cancellation      | 계약이 취소되었는지 여부  | 정상, 해약 | 범주형(명목형)| 취소 여부만을 나타내기 때문에 비교 가능한 의미적인 순서가 없음 |
| age               | 고객의 나이  |       | 수치형(이산형) |   |
| Mileage           | 계약과 연관된 주행 거리  |       | 수치형(연속형)| 주행거리는 연속적인 데이터를 갖음|


</details>

# 📈 Data analytics
- 데이터 분석을 위한 기본 개념 익히기 위한 공간


## 💻 셀레니움(Sellenium)
| 제목 | 작성소스 | 설명 |
|---|---|---|
| 기본 정보 | [begginers](./codes/gatheringdatas/seleriums/begginers.ipynb) | 웹페이지 창 닫고 열기, screenshot| |
| find| [find](./codes/gatheringdatas/seleriums/emartmalls_find.ipynb) | find, bundle lish  with for문 | find_elements_by_css_selector|
| Login| [Login](./codes/gatheringdatas/seleriums/github_events_except.ipynb) | 로그인 기능 구현  | |
| pagination| [pagination](./codes/gatheringdatas/seleriums/emartmalls_find_pagination.ipynb) | pagination 구현  | |
| 앱 리뷰(single) | [googlestore_healthcare](./codes/gatheringdatas/seleriums/googlestore_healthcare_single.ipynb) | single  | |
| 앱 리뷰(loops) | [loops](./codes/gatheringdatas/seleriums/googlestore_healthcare_loops.ipynb) | loops  | |
| 앱 리뷰 스크롤링| [loops_complete](./codes/gatheringdatas/seleriums/googlestore_healthcare_loops_complete.ipynb) | loops with for 문 | 각 제품(앱)에 들어가서 리뷰를 스크롤링 |
| pagedown| [pagedown](./codes/gatheringdatas/seleriums/begginers_pagedown.ipynb) | 마우스 스크롤 pagedown 기능 구현 |  |
| 스크룰링| [pagedown_스크룰링](./codes/gatheringdatas/seleriums/begginers_ready.ipynb) | 마우스 스크롤 기능 구현 | while문을 이용 |


## 💻 정규표현식 (Regex) 
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| Regex | [Regex](./codes/pandass/beginners.ipynb) | 정규표현식 예시 | |


## 💻 자연어 처리
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| wordcloud | [wordcloud](./codes/NLP/wordcloud_simple.ipynb) | 기본 자연어 처리 | | 
| wordcloud_regexp | [wordcloud_regexp](./codes/NLP/wordcloud_simple_regexp.ipynb) |Regex을 이용하여 글자 전처리 | | 
| wordcloud_regexp | [wordcloud_regexp](./codes/NLP/wordcloud_simple_regexp.ipynb) |Regex을 이용하여 글자 전처리 | | 
| 한글 형태소 분석기 | [morpheme_analyzer](./codes/NLP/morpheme_analyzer.ipynb) |한글 형태소 분석기 Okt | |
| withmecab | [withmecab](./codes/NLP/wordcloudwithmecab.ipynb) | withmecab | |
| tokenizers | [tokenizers](./codes/NLP/tokenizers.ipynb) | 불용어 처리 | 
| bestTopicnumber | [bestTopicnumber](./codes/NLP/LDA_gensim_bestTopicnumber.ipynb) | 최적의 토픽 단어 수 | 

## 💻 감성분석
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| sentiment_analyze_dictionary | [sentiment_analyze_dictionary](./codes/NLP/sentiment_analyze_dictionary.ipynb) | 감성 사전에 의한 감성 분석 | 
| sentiment_analyze_mechinelearing | [sentiment_analyze_mechinelearing](./codes/NLP/sentiment_analyze_mechinelearing.ipynb) | 머신러닝에 의한 감성 분석 | 
| LDA_gensim | [LDA_gensim](./codes/NLP/LDA_gensim.ipynb) | gensim 이용하여 LDA | 
| LDA_sklearn | [LDA_sklearn](./codes/NLP/LDA_sklearn.ipynb) | sklearn 이용하여 LDA | 

## 💻 MongoDB
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| commend | [commend](./codes/gatheringdatas/mongodb/commend.txt) | mongoDB의 명령어 정리 | |
| find| [findwithpandas](./codes/gatheringdatas/mongodb/findwithpandas.ipynb) | find with pandas | |
| insertMany |[insertManywithpandas](./codes/gatheringdatas/mongodb/insertManywithpandas.ipynb) | insertManywithpandas | |
| updates | [updates](./codes/gatheringdatas/mongodb/updates.py) | python으로 mongoDB update  | |
| updatewithpandas | [updatewithpandas](./codes/gatheringdatas/mongodb/updatewithpandas.ipynb) | update with pandas  | |


## 📋 QUEST 
<details >
<summary> QUEST 진행 사항</summary>


### 셀레니움(Sellenium) QUEST 
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| books_quest | [books_quest](./codes/gatheringdatas/seleriums/books_quest.ipynb) | 도서목록 제목만 스크래핑, csv로 저장  | |
| login_quest | [login_quest](./codes/gatheringdatas/seleriums/naver_login_quest.ipynb) | naver.com login, login 후 메일로 이동| |
| 스크롤랑 | [koreanz_xyz_quest](./codes/gatheringdatas/seleriums/koreanz_xyz_quest.ipynb) | 특정 페이지 1page ~ 10page까지 정보 수집| |

### 자연어 처리 QUEST 
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| mecab_quest | [mecab_quest](./codes/NLP/mecab_quest.ipynb) | 불용어 처리 | |

### 감성분석 QUEST 
| 제목 | 작성소스 | 설명 | 
|---|---|---|
| navermovierating | [navermovierating](./codes/NLP/navermovierating_mechinelearning_quest.ipynb) |  머신러닝 이용 감성 분석, 타 사이트 댓글 이용 성능 확인| 

</details>
