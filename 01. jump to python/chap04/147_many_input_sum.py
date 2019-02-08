def sum(*args): # *을 이용하여 시퀀스 패킹 매개변수 정의
    sum=0
    for i in args:
        sum+=i
    return sum

tu = list(map(int,input().split())) # 공백기준으로 split하여 int 타입으로 리스트를 만들어 맵핑, 리스트 생성
# list 대신 tuple로 하면 튜플로 입력
print(tu) # 리스트,튜플 모두 *args에 들어갈 수 있으므로 리스트 그래도 사용 가능
print(sum(*tu)) # 리스트,튜플을 넣을시 *을 붙여 시퀀스 타입의 패킹 변수를 전달한다
#시퀀스 자료형 : 여러 객체를 저장하는 자료형으로 순서를 가진다 (문자열,튜플,리스트)