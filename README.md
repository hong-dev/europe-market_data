# Overview

- Hotel의 wifi를 사용하여 user가 smartphone으로 작동할 수 있는 Night Lamp

    ⇒ 유럽시장으로 진출하기 위한 시장 조사

### 1. CSV file

- includes `Country Code`, `Percentage of individuals online`, `Number of Bed-places`
- "Country code" should be distinct, should not be null

### The raw data (.tsz.gz ⇒ tsv file)

#### 1. TOUR_CAP_NAT
    - Number of establishments, bedrooms and bed-places
    - only use: accommod(BEDPL), unit(NR), nace_r2(I551), geo\time, 2016

#### 2. TIN00083
    - Individuals using mobile devices to access the internet on the move
    - only use: indic_is, ind_type(IND_TOTAL), unit, geo\time, 2016

### Special Values
  `:` missing data  
  `suffixed with b` should be used (remove the suffix)  
  `suffixed with u` unreliable ⇒ missing data  
  `suffixed with bu` missing data  
  country code `EA`, `EU27_2007`, `EU27_2020`, `EU28` missing data


### 2. Plots / Tables

- 1~3 visualizations

<br>

---

# Stack/Library

### python

- 모든 소스코드를 python으로 작성 (.py)

### pandas

- tsv, csv 파일 등 raw data 정보를 dataframe으로 만들어서 가공

### sklearn

- data를 특정 범위로 정규화 (MinMaxScaler)

### plotly

- dataframe을 plot과 table로 시각화
- interactive한 시각화를 지원하므로, local 웹 페이지에 띄워서 확인 가능


<br>

---
# Data Processing

#### 1. 두가지 tsv 파일을 불러와서 pandas로 만들기
    - 기본적으로는 '\t' 기준으로, 첫번째 column은 ',' 기준으로 separate
    - geo\time ⇒ Country Code (column명 수정)
    - 2016 ⇒ percentage of individuals online / number of bed-places (최종 csv column명으로 수정)
    
#### 2. 각각의 column들을 filtering하여 유효한 값들만 남기기
    - 숙박시설 수: accommod, unit, nace_r2
    - 모바일 사용자 % : ind_type
    
#### 3. 두 개의 pandas를 공통값인 Country Code 기준으로 merge
    - 필요한 column만 남기기 (3가지)
    - Country Code에서 missing data code는 삭제 (4가지)
    
#### 4. 유효한 data 값만 남기기
    - data값 중 마지막이 b인 것은 b를 지우고 숫자만 남기기
    - 숫자가 아닌 것들은 missing data 처리
    
#### 5. dataframe을 csv 파일로 export
    - Country Code, Percentage of individuals online, Number of Bed-places 3가지 column
    
<br>

---

# Visualization

### **1. Bar plot (bar_plot.png)**

*국가별로 숙박시설과 모바일 이용자를 각각 막대그래프로 표현 (총 39개국)*

    숙박시설과 모바일이용자 중 어느 한쪽만 높아서는 안 되고, 두 가지 조건 모두 필요하다.
    숙박시설 수로는 이탈리아가 압도적으로 높지만, 모바일 이용자 비율은 매우 낮다.
    
    따라서 두 가지 조건이 동시에 높은 영국, 스페인, 독일 순으로 진출을 고려해 볼 수 있다.
    (위의 3개국 다음으로 고려해 볼 수 있는 4번째 국가는, 프랑스이다.)

![bar_plot](https://user-images.githubusercontent.com/53142539/81948175-6aaabd00-963c-11ea-8ddc-4949b04a323d.png)

<br>

### **2. Table (table.png)**

***INDEX :** 국가*  
***COLUMNS :** 숙박시설,  모바일, 숙박시설 백분율, 모바일 백분율, 숙박시설 rank, 모바일 rank, 평균 rank*

    raw data를 표로 봤을 때는 값이 얼만큼 많고 적은 지 눈에 잘 들어오지 않아서,
    모바일과 숙박시설을 0~100 사이의 숫자로 정규화 하였다. ((Nor) Individuals online, (Nor) Bed-places)
    
    모바일과 숙박시설의 값이 높은 순서대로 순위를 매기고 ((Rank) Individuals online, (Rank) Bed-places),
    두 가지 순위의 평균 순위도 고려하였다. ((Rank) Avg Rank)
    
    Avg Rank로 sort 해봤을 때, 높은 rank 순으로 영국, 스페인, 독일이다.
    (위의 3개국 다음으로 고려해 볼 수 있는 4번째 국가는, 스웨덴이다.)

![table](https://user-images.githubusercontent.com/53142539/81948180-6bdbea00-963c-11ea-9073-0acf31d318d6.png)


### 3. Normalized Axes plot (normalized_plot.png)

*숙박시설과 모바일 이용자를 각각 0~100의 값으로 정규화해서, 총 200점 만점으로 점수 매기기*

    정규화 한 값의 합을 봤을 때도, 높은 순으로 영국, 스페인, 독일이다.
    (위의 3개국 다음으로 고려해 볼 수 있는 4번째 국가는, 이탈리아다.)

![normalized_plot](https://user-images.githubusercontent.com/53142539/81948188-6da5ad80-963c-11ea-95e7-62d8c2d21cf9.png)

<br>

---

# Conclusion

세 가지의 Visualization 방법을 비교했을 때, 진출 고려 순위가 모두 **영국, 스페인, 독일**이다.

그러나, 4번째부터 확연히 다른 결과가 도출되었다.

1번째 방법과 2,3번째 방법의 차이는 절대적 비교와 상대적 비교의 차이인데, 국가들 사이에서 순위를 정하거나 정규화를 했을 때는(상대적 비교), 그 값이 원본 값과는 전혀 다른 결과가 나올 수 있었다.

두 가지 종목 모두 독보적으로 높거나 낮으면 상관이 없겠지만, 한 분야에서만 높거나 낮으면 두 분야를 동시에 판단하게 되었을 때 정확한 결과를 도출하기가 어렵다.

여러가지 방향으로 생각해보려고 했지만, 결론은 절대적인 수치를 가지고(1번째 방법) 그 값으로 판단하는 것이 가장 신뢰할만한 것 같다는 생각이 들었다.
