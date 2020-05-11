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
# Data Processing

#### 1. 두가지 tsv 파일을 불러와서 pandas로 만든다.
    - 기본적으로는 '\t' 기준으로, 첫번째 column은 ',' 기준으로 separate 시킨다.
    - geo\time ⇒ Country Code로 column명을 바꾼다.
    - 2016 ⇒ percentage~ / number~ 로 최종 csv column명으로 바꾼다.
    
#### 2. 각각의 column들을 filtering하여 유효한 값들만 남긴다.
    - 숙박시설 수: accommod, unit, nace_r2
    - 모바일 사용자 % : ind_type
    
#### 3. 두 개의 pandas를 공통값인 Country Code 기준으로 합친다.
    - 필요한 column만 남긴다. (3가지)
    - Country Code에서 missing data code는 삭제한다. (4가지)
    
#### 4. 유효한 data 값만 남긴다.
    - data값 중 마지막이 b인 것은 b를 지우고 숫자만 남기기
    - 숫자가 아닌 것들은 missing data 처리(NaN)
    
#### 5. dataframe을 csv 파일로 export
    - Country Code, Percentage of individuals online, Number of Bed-places 3가지 column
