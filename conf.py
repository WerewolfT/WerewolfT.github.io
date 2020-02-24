# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "WerewolfT/WerewolfT.github.io@master"
}

# For site
site_name = "子夜之歌"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2018-11-03T19:52+08:00"
author = "Tanner"
email = "alpha@tanner.pub"
author_homepage = "/"
description = "灵魂渴慕星空"
key_words = ["blog"]
language = 'english'

#external_links = [
#    {
#       "name": "Maverick",
#        "url": "https://github.com/AlanDecode/Maverick",
#        "brief": "🏄‍ Go My Own Way."
#    },
#    {
#        "name": "Triple NULL",
#        "url": "https://www.imalan.cn",
#        "brief": "Home page for AlanDecode."
#    }
#]

nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/_WTanner",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-telegram"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
