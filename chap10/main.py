import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller로 실행할 때
    except Exception:
        base_path = os.path.abspath(".")  # 일반 실행할 때
    return os.path.join(base_path, relative_path)

# 이미지 경로
path = resource_path(os.path.join("images", "cat.png"))

# 이미지 읽기
image = mpimg.imread(path)

# 이미지 표시
plt.imshow(image)
plt.axis('off')  # 축 숨기기
plt.show()
