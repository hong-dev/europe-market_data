# Overview

- Hotel의 wifi를 사용하여 user가 smartphone으로 작동할 수 있는 Night Lamp

    ⇒ 유럽시장으로 진출하기 위한 시장 조사

<br>

### 1. CSV file

- includes `Country Code`, `Percentage of individuals online`, `Number of Bed-places`
- "Country code" should be distinct, should not be null

<br>

#### The raw data (.tsz.gz ⇒ tsv file)
1. TOUR_CAP_NAT
  * Number of establishments, bedrooms and bed-places
  * only use: **accommod(BEDPL), unit(NR), nace_r2(I551), geo\time, 2016**

2. TIN00083
  * Individuals using mobile devices to access the internet on the move
  * only use: **indic_is, ind_type(IND_TOTAL), unit, geo\time, 2016**

<br>

#### Special Values
  `:` missing data  
  `suffixed with b` should be used (remove the suffix)  
  `suffixed with u` unreliable ⇒ missing data  
  `suffixed with bu` missing data  
  country code `EA`, `EU27_2007`, `EU27_2020`, `EU28` missing data

<br>

### 2. Plots / Tables

- 1~3 visualizations
