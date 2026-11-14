import os
import zipfile
from PIL import Image, ImageDraw

def draw_monkey_icon(size: int) -> Image.Image:
    """
    使用 Pillow 繪製高解析度、可愛的「猴丸子」PWA 應用程式圖示
    若同目錄下存在「猴丸子.jpg」或「monkey.jpg」，則優先裁切縮放使用！
    """
    for custom_img in ["猴丸子.jpg", "monkey.jpg", "monkey.png"]:
        if os.path.exists(custom_img):
            with Image.open(custom_img) as img:
                img = img.convert("RGBA")
                min_side = min(img.width, img.height)
                left = (img.width - min_side) // 2
                top = (img.height - min_side) // 2
                cropped = img.crop((left, top, left + min_side, top + min_side))
                return cropped.resize((size, size), Image.Resampling.LANCZOS)

    # 若無外部照片，自動繪製可愛雪地小猴向量質感圖示
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    s = size / 512.0  # 縮放比例基準

    # 1. 溫暖木質圓角背景
    draw.rounded_rectangle([0, 0, size, size], radius=int(112 * s), fill="#8c5a3c")
    # 2. 雪藍背景圓
    draw.ellipse([40 * s, 40 * s, 472 * s, 472 * s], fill="#e0f2fe")
    # 3. 毛絨耳朵
    draw.ellipse([63 * s, 204 * s, 167 * s, 308 * s], fill="#a47551", outline="#7f5539", width=max(2, int(8 * s)))
    draw.ellipse([85 * s, 226 * s, 145 * s, 286 * s], fill="#f4a261")
    draw.ellipse([345 * s, 204 * s, 449 * s, 308 * s], fill="#a47551", outline="#7f5539", width=max(2, int(8 * s)))
    draw.ellipse([367 * s, 226 * s, 427 * s, 286 * s], fill="#f4a261")
    # 4. 圓滾滾頭部
    draw.ellipse([108 * s, 114 * s, 404 * s, 410 * s], fill="#a47551", outline="#7f5539", width=max(2, int(8 * s)))
    # 5. 粉嫩臉龐
    draw.ellipse([148 * s, 195 * s, 364 * s, 385 * s], fill="#ffd6ba")
    # 6. 紅撲撲臉頰
    draw.ellipse([152 * s, 268 * s, 214 * s, 316 * s], fill="#ff8fa3")
    draw.ellipse([298 * s, 268 * s, 360 * s, 316 * s], fill="#ff8fa3")
    # 7. 水汪汪大眼睛
    draw.ellipse([182 * s, 226 * s, 230 * s, 274 * s], fill="#3d2314")
    draw.ellipse([190 * s, 234 * s, 208 * s, 252 * s], fill="#ffffff")
    draw.ellipse([282 * s, 226 * s, 330 * s, 274 * s], fill="#3d2314")
    draw.ellipse([290 * s, 234 * s, 308 * s, 252 * s], fill="#ffffff")
    # 8. 粉紅小鼻子與微笑弧線
    draw.ellipse([242 * s, 268 * s, 270 * s, 288 * s], fill="#f28482")
    draw.arc([224 * s, 284 * s, 288 * s, 326 * s], start=15, end=165, fill="#6d3b2e", width=max(2, int(8 * s)))

    return img

def main():
    os.makedirs("icons", exist_ok=True)
    icon_192_path = os.path.join("icons", "icon-192.png")
    icon_512_path = os.path.join("icons", "icon-512.png")

    print("🎨 正在生成 PWA 圖示...")
    draw_monkey_icon(192).save(icon_192_path, "PNG")
    draw_monkey_icon(512).save(icon_512_path, "PNG")
    print(f"✅ 已生成 {icon_192_path} 與 {icon_512_path}")

    zip_filename = "monkey_dango_pwa.zip"
    files_to_pack = [
        "index.html",
        "manifest.json",
        "sw.js",
        "gen_icons.py",
        icon_192_path,
        icon_512_path
    ]

    print(f"📦 正在打包專案為 {zip_filename} ...")
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in files_to_pack:
            if os.path.exists(file_path):
                zf.write(file_path, arcname=file_path)
                print(f"   + 已加入: {file_path}")
            else:
                print(f"   ! 找不到檔案 (請確認已儲存): {file_path}")

    print(f"\n🎉 完成！可直接將 {zip_filename} 解壓縮上傳至 GitHub Pages！")

if __name__ == "__main__":
    main()