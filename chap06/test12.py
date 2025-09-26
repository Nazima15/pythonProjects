import numpy as np

# 1️⃣ shuffle 예시
x = np.arange(1, 11)
np.random.seed(1)          # 재현 가능한 난수
np.random.shuffle(x)       # 원본 배열 섞기
print("shuffle:", x)

# 2️⃣ permutation 예시
y = np.arange(1, 11)
np.random.seed(1)
print("permutation:", np.random.permutation(y))  # 새 배열 반환
print("원본 y:", y)                               # 원본은 그대로

# 3️⃣ choice 예시 (중복 없이, 확률 지정)
fruits = ['apple', 'banana', 'cherries', 'durian', 'grapes', 
          'lemon', 'mango', 'orange', 'peach', 'pear']

# 확률 배열 길이 = 과일 수 10개
pb = [0.1, 0, 0.2, 0.5, 0.1, 0.05, 0.05, 0, 0, 0]

np.random.seed(1)
sample_fruits = np.random.choice(fruits, 3, replace=False, p=pb)
print("choice:", sample_fruits)
