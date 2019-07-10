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


class Novel(Post):
    def __init__(self, writer, title, content, view_count):
        self.writer = writer
        super().__init__(title, content, view_count)
