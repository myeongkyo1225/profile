import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/myeongkyo_071225/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["purple", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "정명교")
write("description", "대륜중학교")
write("button", "인스타그램")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생년월일": "2007년 12월 ",
  "좋아하는 것": "놀기, 게임, 음식먹기",
  "싫어하는 것": "파인애플 요리, 생선, 분란",
  "진행중인 게임": "배틀그라운드, 로블록스, 클래시로얄"
}
information(informations)
