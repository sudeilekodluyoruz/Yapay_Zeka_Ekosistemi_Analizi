"""Dünya Bankası WDI göstergelerini indirip tek bir CSV'ye çevirir.
Kullanım:  pip install requests pandas   ->   python wdi_indir.py
Çıktı:     wdi_gostergeler.csv  (ülke x yıl, 7 gösterge sütunu (nüfus eklendi))
"""
import requests
import pandas as pd

BASE = "https://api.worldbank.org/v2"
GOSTERGELER = {
    "GB.XPD.RSDV.GD.ZS": "arge_gsyh_yuzde",
    "SP.POP.SCIE.RD.P6": "arastirmaci_milyon_kisi",
    "IT.NET.USER.ZS": "internet_kullanim_yuzde",
    "IT.NET.BBND.P2": "genisband_100_kisi",
    "NY.GDP.PCAP.CD": "kisi_basi_gsyh_usd",
    "SE.TER.ENRR": "yuksekogretim_kayit_yuzde",
    "SP.POP.TOTL": "nufus",
}
YILLAR = "2015:2025"


def getir(url, params=None):
    """Tüm sayfaları dolaşıp kayıtları liste olarak döndürür."""
    kayitlar, sayfa = [], 1
    while True:
        r = requests.get(url, params={**(params or {}), "format": "json", "per_page": 1000, "page": sayfa}, timeout=60)
        r.raise_for_status()
        meta, veri = r.json()[0], r.json()[1] or []
        kayitlar += veri
        if sayfa >= int(meta["pages"]):
            return kayitlar
        sayfa += 1


# Bölge/gelir grubu gibi toplulaştırmaları dışarıda bırakmak için gerçek ülke listesi
ulkeler = {c["id"]: c["name"] for c in getir(f"{BASE}/country") if c["region"]["value"] != "Aggregates"}

satirlar = []
for kod, ad in GOSTERGELER.items():
    print("İndiriliyor:", kod)
    for d in getir(f"{BASE}/country/all/indicator/{kod}", {"date": YILLAR}):
        iso3 = d["countryiso3code"]
        if iso3 in ulkeler and d["value"] is not None:
            satirlar.append((iso3, ulkeler[iso3], int(d["date"]), ad, d["value"]))

df = pd.DataFrame(satirlar, columns=["iso3", "ulke", "yil", "gosterge", "deger"])
genis = df.pivot_table(index=["iso3", "ulke", "yil"], columns="gosterge", values="deger").reset_index()
genis.to_csv("wdi_gostergeler.csv", index=False, encoding="utf-8-sig")
print("Bitti:", genis.shape, "-> wdi_gostergeler.csv")
