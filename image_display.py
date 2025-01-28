import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def select_and_display_image():
    # ファイル選択ダイアログを開く
    filepath = filedialog.askopenfilename(
        title="画像を選択してください",
        filetypes=[("画像ファイル", "*.png;*.jpg;*.jpeg;*.bmp")]
    )

    if filepath:
        # 画像を表示
        image_window = tk.Toplevel(root)
        image_window.title("選択した画像")
        
        # 画像を表示するためにPillowを利用
        try:
            image = Image.open(filepath)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(image_window, image=photo)
            label.image = photo  # 参照を保持しないと画像が消える
            label.pack()
        except Exception as e:
            print(f"画像の表示中にエラーが発生しました: {e}")

# メインウィンドウ
root = tk.Tk()
root.title("画像選択アプリ")

# ボタンを作成
button = tk.Button(root, text="画像を選択", command=select_and_display_image)
button.pack(pady=20)

# アプリケーションの開始
root.mainloop()
