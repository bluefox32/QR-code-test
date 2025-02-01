import numpy as np
import matplotlib.pyplot as plt

# QRコードのサイズ（例：バージョン1, 21x21）
qr_size = 21

# QRコードマトリックスを作成（0: 白, 1: 黒）
qr_matrix = np.random.randint(0, 2, (qr_size, qr_size))

# 位置検出パターンを設置する関数
def add_position_patterns(matrix):
    """QRコードの位置検出パターン（3箇所）を配置"""
    def place_square(x, y):
        matrix[x:x+7, y:y+7] = 1  # 外枠
        matrix[x+1:x+6, y+1:y+6] = 0  # 内部白
        matrix[x+2:x+5, y+2:y+5] = 1  # 中心黒
    
    place_square(0, 0)  # 左上
    place_square(0, qr_size - 7)  # 右上
    place_square(qr_size - 7, 0)  # 左下
    return matrix

# マスクパターンを解除（例：マスクパターン1: (x + y) % 2）
def remove_mask_pattern(matrix):
    """マスクパターンを解除して元データを復元"""
    unmasked_matrix = matrix.copy()
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if (x + y) % 2 == 0:  # マスクパターン1の条件
                unmasked_matrix[x, y] = 1 - matrix[x, y]  # 反転
    return unmasked_matrix

# 位置検出パターンを追加
qr_matrix = add_position_patterns(qr_matrix)

# マスクパターンを解除
unmasked_qr = remove_mask_pattern(qr_matrix)

# QRコードの表示
plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plt.imshow(qr_matrix, cmap='gray')
plt.title("QR Code with Position Patterns")

plt.subplot(1, 2, 2)
plt.imshow(unmasked_qr, cmap='gray')
plt.title("QR Code after Mask Removal")

plt.show()