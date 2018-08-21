import pickle

myMovie = {"Iron Man": 9.8, "Infinite War": 9.0}

# 딕셔너리를 피클 파일에 저장
pickle.dump(myMovie, open('rating.p','wb'))

# 피클 파일에 딕셔너리를 로딩
myMovie = pickle.load(open('rating.p','rb'))
print(myMovie)