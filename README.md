# 🐒 猴丸子的雪地木屋解謎冒險

可愛的雪地木屋解謎小遊戲，支援 PWA（可安裝到手機主畫面）與手機／平板／電腦自適應。

## 檔案說明

| 檔案 | 用途 |
| --- | --- |
| `index.html` | 遊戲主程式 |
| `manifest.json` | PWA 設定 |
| `sw.js` | Service Worker（快取） |
| `icons/` | App 圖示 |
| `gen_icons.py` | 重新產生圖示的腳本（可選） |

## 上傳到 GitHub Pages

1. 在 GitHub 建立新的 repository（例如 `monkey-dango`），設為 Public
2. 把這個資料夾裡的**所有檔案**上傳到 repository 根目錄
3. 進入 **Settings → Pages**
4. Source 選 **Deploy from a branch**，Branch 選 `main`、資料夾選 `/ (root)`，按 Save
5. 等 1～2 分鐘，網址會是 `https://你的帳號.github.io/monkey-dango/`

## 換成自己的猴丸子照片（可選）

把照片命名為 `猴丸子.jpg` 或 `monkey.jpg` 放在同資料夾，執行：

```
python gen_icons.py
```

就會用照片重新產生 `icons/icon-192.png` 與 `icons/icon-512.png`。
