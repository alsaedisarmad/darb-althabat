"""يبني index.html من src/lesson.html بدمج الخطوط والصور والصوت والفيديو داخله.

الاستخدام:
    python build.py            # يكتب index.html
    python build.py out.html   # يكتب إلى مسار آخر
"""
import base64
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

ASSETS = {
    "__F_KUFI__": ("fonts/ReemKufi[wght].ttf", "font/ttf"),
    "__F_TAJ_R__": ("fonts/Tajawal-Regular.ttf", "font/ttf"),
    "__F_TAJ_B__": ("fonts/Tajawal-Bold.ttf", "font/ttf"),
    "__F_TAJ_X__": ("fonts/Tajawal-ExtraBold.ttf", "font/ttf"),
    "__F_AMIRI__": ("fonts/AmiriQuran-Regular.ttf", "font/ttf"),
    "__LOGO__": ("assets/moe_mask.png", "image/png"),
    "__POSTER__": ("assets/poster.jpg", "image/jpeg"),
    "__VIDEO__": ("assets/path.mp4", "video/mp4"),
    "__AUDIO1__": ("assets/recite.m4a", "audio/mp4"),
    "__AUDIO2__": ("assets/recite114.m4a", "audio/mp4"),
}


def data_uri(path, mime):
    with open(os.path.join(ROOT, path), "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "index.html")
    with open(os.path.join(ROOT, "src", "lesson.html"), encoding="utf-8") as f:
        html = f.read()
    for key, (path, mime) in ASSETS.items():
        if key not in html:
            sys.exit("placeholder missing: " + key)
        html = html.replace(key, data_uri(path, mime))
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("built", out, len(html) // 1024, "KB")


if __name__ == "__main__":
    main()
