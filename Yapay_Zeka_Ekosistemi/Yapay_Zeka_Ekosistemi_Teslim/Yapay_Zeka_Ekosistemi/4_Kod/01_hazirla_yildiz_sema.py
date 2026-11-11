"""Ham kaynaklardan yıldız şemalı veri modelini üretir.
Çalıştır (4_Kod klasöründen):  pip install pandas  ->  python 01_hazirla_yildiz_sema.py
Çıktı: ../3_Veri/  (3 olgu tablosu + 2 boyut tablosu)
"""
from pathlib import Path
import numpy as np, pandas as pd
from ulke_adlari import TR, KITA

HAM, CIKTI = Path("ham_veri"), Path("../3_Veri")
YILLAR = range(2016, 2026)
EPOCH_ISO3 = {"Australia": "AUS", "Bulgaria": "BGR", "Canada": "CAN", "China": "CHN", "Finland": "FIN", "France": "FRA",
              "Germany": "DEU", "Hong Kong": "HKG", "Israel": "ISR", "Japan": "JPN", "Poland": "POL", "Russia": "RUS",
              "Saudi Arabia": "SAU", "Singapore": "SGP", "South Korea": "KOR", "Switzerland": "CHE", "Ukraine": "UKR",
              "United Arab Emirates": "ARE", "United Kingdom": "GBR", "United States": "USA"}

# --- Dünya Bankası göstergeleri + nüfus  ->  FactKalkinma
wdi = pd.read_csv(HAM / "wdi_gostergeler.csv")
nufus = pd.read_csv(HAM / "nufus.csv", keep_default_na=False)
nufus = nufus[nufus.iso3.str.len() == 3]                     # bölge/gelir grubu toplulaştırmaları atılır
kal = wdi.merge(nufus.rename(columns={"nufus": "Nufus"}), on=["iso3", "yil"], how="left")
kal = kal.rename(columns={"iso3": "ISO3", "yil": "Yil", "arge_gsyh_yuzde": "ArGeGsyh", "arastirmaci_milyon_kisi": "ArastirmaciMilyon",
                          "internet_kullanim_yuzde": "InternetKullanim", "genisband_100_kisi": "Genisband100",
                          "kisi_basi_gsyh_usd": "KisiBasiGsyh", "yuksekogretim_kayit_yuzde": "YuksekogretimKayit"})
KOLON = ["ISO3", "Yil", "Nufus", "ArGeGsyh", "ArastirmaciMilyon", "InternetKullanim", "Genisband100", "KisiBasiGsyh", "YuksekogretimKayit"]
kal = kal[kal.Yil.isin(YILLAR)][KOLON]
kal = kal[kal[KOLON[2:]].notna().any(axis=1)].reset_index(drop=True)
ulkeler = set(kal.ISO3)

# --- CSET özel yatırım  ->  FactYatirim  (yalnızca kayıt bulunan ülke-yıllar)
cset = pd.read_csv(HAM / "private-investment-in-artificial-intelligence-cset.csv")
cset.columns = ["ulke", "ISO3", "Yil", "YatirimUSD"]
yat = cset[cset.ISO3.isin(ulkeler) & cset.Yil.isin(YILLAR) & (cset.YatirimUSD > 0)][["ISO3", "Yil", "YatirimUSD"]]
yat = yat.assign(YatirimUSD=yat.YatirimUSD.round(0).astype("int64")).sort_values(["ISO3", "Yil"]).reset_index(drop=True)

# --- Epoch AI büyük model sayısı  ->  FactModel  (kümülatif; yalnızca sayısı > 0 olan ülke-yıllar)
ep = pd.read_csv(HAM / "cumulative-number-of-large-scale-ai-systems-by-country.csv")
ep.columns = ["ulke", "kod", "Yil", "say"]
ep = ep[ep.ulke.isin(EPOCH_ISO3)].assign(ISO3=lambda x: x.ulke.map(EPOCH_ISO3))
w = ep.pivot_table(index="ISO3", columns="Yil", values="say").reindex(columns=range(2019, 2026)).ffill(axis=1).fillna(0)
mod = w.stack().rename("BuyukModelKumulatif").reset_index()
mod = mod[mod.BuyukModelKumulatif > 0].astype({"BuyukModelKumulatif": "int64"}).sort_values(["ISO3", "Yil"]).reset_index(drop=True)

# --- Boyutlar
ad = wdi.drop_duplicates("iso3").set_index("iso3").ulke
ul = pd.DataFrame({"ISO3": sorted(ulkeler)})
ul["UlkeTR"] = [TR.get(i, ad[i]) for i in ul.ISO3]
ul["Kita"] = ul.ISO3.map(KITA)
gsyh = kal[kal.Yil.isin([2021, 2022, 2023])].sort_values("Yil").groupby("ISO3").KisiBasiGsyh.apply(lambda s: s.dropna().iloc[-1] if s.notna().any() else np.nan)
etiket = ["1) <2 bin $", "2) 2–6 bin $", "3) 6–15 bin $", "4) 15–40 bin $", "5) >40 bin $"]
ul["GelirGrubu"] = pd.cut(ul.ISO3.map(gsyh), [0, 2000, 6000, 15000, 40000, 1e9], labels=etiket, right=False).astype(object).fillna("Bilinmiyor")
yil = pd.DataFrame({"Yil": list(YILLAR)})

CIKTI.mkdir(exist_ok=True)
for ad_, df in {"FactYatirim": yat, "FactModel": mod, "FactKalkinma": kal, "DimUlke": ul, "DimYil": yil}.items():
    df.to_csv(CIKTI / f"{ad_}.csv", index=False, encoding="utf-8-sig"); print(f"{ad_:13s} {df.shape}")
