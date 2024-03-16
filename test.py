import qrcode

# QRコードに含めるデータ
data = "https://www.google.co.jp/"

# QRコード生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# QRコードを画像として生成
img = qr.make_image(fill_color="black", back_color="white")

# 画像をファイルに保存
img.save("qr_code_example.png")
