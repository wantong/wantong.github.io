AUTHOR = 'winter'
SITENAME = "winter's knowledge share"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'          # 默认语言设为中文
OG_LOCALE = 'zh_CN'          # Open Graph 元数据语言
LOCALE = 'zh_CN.UTF-8'       # 本地化设置（确保系统已安装此语言包）

BIND = "0.0.0.0"  # 允许外部访问
PORT = 3588          # 指定端口

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# pelicanconf.py
