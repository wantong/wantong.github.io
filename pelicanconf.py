AUTHOR = 'winter'
SITENAME = "Sumarization"
SITEURL = "https://wantong.github.io"

SITETITLE = AUTHOR
SITESUBTITLE = u"concentrate"
SITEDESCRIPTION = "Tight your thought, fast your work flow"
SITELOGO = SITEURL + '/images/wantongtop.png'
FAVICON = SITEURL + '/images/web_icon_64x64.icon'
BROWSER_COLOR = '#333333'
RELATIVE_URLS = True

SOCIAL = (('envelope', 'mailto:guqian110@163.com'),
    ('github','https://github.com/wantong'),
        )

MENUITEMS = (('Authors', '/authors.html'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             )

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'          # é»˜è?¤è??è¨€è®¾ä¸ºä¸?æ–?
OG_LOCALE = 'zh_CN'          # Open Graph å…ƒæ•°æ?è¯?è¨€
LOCALE = 'zh_CN.UTF-8'       # æœ?åœ°åŒ–è®¾ç½®ï¼ˆç¡®ä¿ç³»ç»Ÿå·²å®‰è?…æ?¤è??è¨€åŒ…ï¼‰

BIND = "0.0.0.0"  # å…è?¸å?–éƒ¨è®¿é—®
PORT = 3588          # æŒ‡å®šç«?å?

THEME = 'Flex'
THEME_COLOR = 'light'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# pelicanconf.py


ROBOTS = "index, follow"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2025

STATIC_PATHS = ["extra/custom.css"]

# Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

MAIN_MENU = True
