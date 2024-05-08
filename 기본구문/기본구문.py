# df.describe() # 컬럼별 대략적인 정보, 최소값,최대값, 평균 등 확인
# df.head() # 상단 5개 출력
# df.tail() # 하단 5개 출력
# df.info() # 컬럼별 타입,크기 정보
# df.values # rows데이터 배열로 출력
# df.index # index 정보
# df.columns # 컬럼 정보
# df.shape # 데이터 크기 정보(rows,columns)
# df['sw특기'].count() # Nan 데이터는 개수에 포함되지 않음
# df['국어'].sum() # 전체합계
# df['학교'].unique() # 중복제거
# df['학교'].nunique() # 중복제거 후 개수 출력
# df.iloc[0] # 0번째 rows 데이터 가져오기
# df.iloc[0].str # str타입으로 변경 
# df.iloc[0].str.replace(",","")  # 타입 변경 후 replace
# index_col = 0 첫번째 컬럼을 index로 지정
# skiprows : 상단부분제외
# nrows: 가져오기
# usecols : 특정컬럼부분 가져오기
### ex)
# df = pd.read_excel('20122022_출생.xlsx',skiprows=2,nrows=3,usecols='B:M',index_col=0)
# df.index.name = '제목'
# df.head(3)
###
# & = and , | = or