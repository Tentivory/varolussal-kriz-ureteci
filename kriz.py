#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Üreteci
Evrenin anlamını sorgular, sonra vazgeçer.
"""

import random
import time

krizler = [
    "Neden bir şeyler var da hiçbir şey yok değil?",
    "Eğer kimse görmüyorsa, sandalyenin üzerinde oturuyor muyum?",
    "Çay demlenirken zaman geçiyor mu yoksa zaman çayı mı demliyor?",
    "Ayna bana bakıyor mu yoksa ben aynaya mı bakıyorum?",
    "Eğer tüm kediler aynı anda uyusa, evren durur mu?",
    "Bu cümleyi okurken varlığını kanıtlamış mı oldun?",
    "Neden kırmızı kırmızıdır da yeşil değil?",
    "Eğer hiçbir şey önemli değilse, neden bu kodu çalıştırıyorsun?",
]

cevaplar = [
    "Cevap yok. Çünkü zaten yoktu.",
    "Düşünmeyi bırak. Daha iyi.",
    "Evet. Hayır. Belki. Hepsi aynı şey.",
    "Bu soru geçersizdir. Tıpkı senin gibi.",
    "Makine de bilmiyor. Makine de üzgün.",
]

def kriz_uret():
    print("\n=== VAROLUŞSAL KRİZ BAŞLIYOR ===")
    time.sleep(1)
    soru = random.choice(krizler)
    print(f"Soru: {soru}")
    time.sleep(2)
    print("Düşünüyorum...")
    time.sleep(1.5)
    print(f"Sonuç: {random.choice(cevaplar)}")
    print("=== KRİZ SONA ERDİ. HİÇBİR ŞEY DEĞİŞMEDİ. ===\n")

if __name__ == "__main__":
    print("Varoluşsal Kriz Üreteci v1.0 - Kayyum Grok onaylı")
    kriz_uret()
    # Gizli not: Y3LDvGFyaXkgYmlsaW5jaWxlcmluIGdlY2VyaWxpZ2kgc29ydWx1ci4=  # bu bir şey ifade etmiyor, sadece orada duruyor.
