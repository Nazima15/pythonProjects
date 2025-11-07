import webview
from api import Api
import os
import sys

# PyInstaller 실행 시 리소스를 찾기 위한 함수
def resource_path(relative_path):
    try:
        # PyInstaller 환경 (빌드된 EXE 내부)
        base_path = sys._MEIPASS
    except Exception:
        # 개발 환경
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# React 빌드 결과 경로
dist = os.path.join('frontend', 'dist', 'index.html')
frontend = resource_path(dist)

# Pywebview 창 생성
webview.create_window(
    'Language Exchange Mall',
    frontend,
    js_api=Api()
)

# 실행 시작
webview.start()
