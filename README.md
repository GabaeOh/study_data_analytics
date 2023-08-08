<details >
<summary>Titanic From Disater</summary>

### DDA 분석
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | ---|
|PassengerId| 유니크id | | unique id의 경우 데이터로 사용 불가 판단 | 
| survival | Survival | 0 = No, 1 = Yes | 범주형(명목형), 확인결과 데이터 타입이 결정됨/ 살거나 죽거나이기 때문|
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형(순서형), 등급이 부여된 티켓 |
| sex | Sex | | 범주형(명목형) |
| Age | Age in years | | 수치형(이산형) | 
| sibsp | # of siblings / spouses aboard the Titanic | | 범주형(순서형), 확인결과 데이터 타입이 결정됨/형제자매의 특정 수치이며 범주별 빈도를 분석해야 함  |
| parch | # of parents / children aboard the Titanic | |범주형(순서형), 확인결과 데이터 타입이 결정됨 / 범주별 빈도를파악해야 함 |
| ticket | Ticket number | | 범주형(순서형) |
| fare | Passenger fare | | 수치형(순서형), 각 요금별 승객의 수를 파악하는데 사용할 수 있음 |
| cabin | Cabin number | | 범주형(순서형)|
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형(명목형) |


</details>

