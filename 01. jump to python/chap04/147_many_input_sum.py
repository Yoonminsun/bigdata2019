def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

tu = list(map(int,input().split())) # 공백기준으로 split하여 int 타입으로 리스트를 만들어 맵핑, 리스트 생성
# tu = tuple(tu) 리스트를 튜플로 바꾸고 싶은 경우
print(tu) # 리스트,튜플 모두 *args에 들어갈 수 있으므로 리스트 그래도 사용 가능
print(sum(*tu)) # 리스트,튜플을 넣을시 *을 붙여 언패킹(unpacking) 한다