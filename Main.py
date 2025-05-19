# - 작은 크기의 영단어 검색 창. 최우선 프로세스 고정, selenium 사용, tkinter로 가벼운 GUI,
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# - 크롬 드라이버 백그라운드 실행
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options) #백그라운드에 웹 드라이버 실행. 훗.

root = tk.Tk()
root.title("성현성현 영사전")
root.geometry("350x250")
root.resizable(False, False)
root.attributes('-topmost', True) #최우선 고정

search = tk.Text(root, height=1, width=20)
search.pack(pady=10)

label = tk.Label(root, text="안녕 난 성현이라고 해.", wraplength=300) #wraplength는 텍스트 줄바꿈 제한.
label.pack()

log = []
def watch_log():
    if not log:
        return "검색 기록이 없습니다."
    log_text = "\n".join(log)
    return log_text

def search_word(word):
    if not word:
        return "Please enter a word."
    if len(word) > 20:
        return "Word is too long."
    if not word.isalpha():
        return "Please enter a valid word."
    if word.isupper():
        word = word.lower()

    driver.get(f"https://dict.naver.com/search.dict?query={word}")
    meaning = driver.find_element(By.CLASS_NAME, 'addition_info').text
    driver.implicitly_wait(1)
    if len(log) > 5:
        log.pop(0)
    log.append(word)

    return meaning

def preview(meaning):
    label.config(text=meaning)
    label.update()
    search.delete("1.0", tk.END)

SearchBtn = tk.Button(root, text="Search", command=lambda: preview(search_word(search.get("1.0", tk.END).strip())))
SearchBtn.pack(pady=10)

Searched_log = tk.Button(root, text="log", command=lambda: preview(watch_log()))
Searched_log.place(x=320, y=210)

root.mainloop()