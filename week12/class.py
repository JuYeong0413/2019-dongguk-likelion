class Post:
    def __init__(self, title, content, view_count):
        self.title = title
        self.content = content
        self.view_count = view_count

    # 클래스 메소드, 클래스 자체에서 실행
    def hello():
        print("모든 글들이 지워졌다.")

    # 인스턴스 메소드, 객체에서만 실행할 수 있다.
    def delete(self):
        print("{}글이 지워졌어요".format(self.title))


post = Post("간장게장 담그는 법", "양송이버섯을 간장에 절인다", 50)

my_num = 3
print(type(my_num))
print(type(post))
print(post.title)
print(post.content)

Post.hello()
post.delete()


class Noble(Post):
    def __init__(self, writer, title, content, view_count):
        self.writer = writer
        super().__init__(title, content, view_count)

    def delete(self):
        print("{}글이 지워졌어요ㅠㅠ".format(self.title))


noble = Noble("황순원", "소나기", "슬펐다", 100000)
print(noble.title)
noble.delete()

# 모듈 module은 파일 하나를 의미함
# 패키지 package는 모듈들이 모여있는 폴더
# 내가 패키지다. __init__.py 파일 이름만 의미가 있는 것, 여기에 뭘 쓰진 않는다
