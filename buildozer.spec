[app]
title = Ada
package.name = adaai
package.domain = org.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,flask,groq,edge-tts,urllib3,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,WAKE_LOCK,RECEIVE_BOOT_COMPLETED

# Stable Android API version set karein taaki license error na aaye
android.api = 34
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1

