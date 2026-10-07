<div align="center">

# 🔐 PC Lock Screen & Session Timer

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-41CD52?logo=qt&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)

**🇬🇧 English** · [🇹🇷 Türkçe](#-türkçe)

</div>

## 🇬🇧 Overview
A full-screen lock screen that starts with Windows and **asks for a password before the computer can be used**. After a successful login the user picks a session length (**unlimited, 30 minutes or 1 hour**) and the PC shuts down automatically when the time is up. This makes it useful as a simple screen-time / parental-control tool.

**Features**
- Always-on-top, full-screen window that can't be closed
- Password stored in obfuscated form (not as plain text)
- Timed sessions with automatic shutdown (`shutdown /s /t …`)
- Packaged as a Windows installer with PyInstaller

**Install**
1. Run `Güvenlik Sistemi Setup.exe`, **or** run `proje/main.py` manually (`pip install PyQt5`).
2. Put a shortcut to `main.exe` in `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`.
3. The default password is `admin`. Change it with `sifreleme.exe`, then delete or hide that file.

| File | Purpose |
|---|---|
| `proje/login.py` | Lock screen + password check |
| `proje/arayuz.py` | Session length selection + shutdown timer |
| `proje/*.ui` | Qt Designer layouts |

## 🇹🇷 Türkçe
Windows açılışında başlayan ve **bilgisayar kullanılmadan önce şifre isteyen** tam ekran bir kilit ekranı. Şifre doğru girildiğinde kullanıcı oturum süresini seçer (**süresiz, 30 dakika veya 1 saat**) ve süre dolunca bilgisayar otomatik olarak kapanır. Bu yönüyle basit bir ekran süresi ya da ebeveyn denetimi aracı olarak kullanılabilir.

**Kurulum**
1. `Güvenlik Sistemi Setup.exe` ile kurun **ya da** `proje/main.py` dosyasını elle çalıştırın (`pip install PyQt5`).
2. `main.exe` kısayolunu `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` klasörüne ekleyin.
3. Varsayılan şifre `admin`'dir. `sifreleme.exe` ile değiştirin, ardından dosyayı silin ya da saklayın.
