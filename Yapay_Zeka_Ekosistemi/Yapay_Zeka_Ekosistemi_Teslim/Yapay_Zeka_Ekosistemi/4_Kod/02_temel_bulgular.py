"""Rapordaki temel sayıları 3_Veri tablolarından yeniden üretir.
Çalıştır (4_Kod klasöründen):  pip install pandas scipy numpy  ->  python 02_temel_bulgular.py
"""
from pathlib import Path
import numpy as np, pandas as pd
from scipy import stats

V = Path("../3_Veri")
y, m, k, u = (pd.read_csv(V / f"{n}.csv") for n in ["FactYatirim", "FactModel", "FactKalkinma", "DimUlke"])

# 1) Yoğunlaşma
t = y.groupby("ISO3").YatirimUSD.sum().sort_values(ascending=False)
x = np.sort(t.values); n = len(x)
print(f"Toplam yatırım: {t.sum()/1e9:,.1f} milyar $ | yatırım kaydı olan ülke: {n}")
print(f"ABD payı: %{t['USA']/t.sum()*100:.1f} | ilk 10 payı: %{t.head(10).sum()/t.sum()*100:.1f} | Gini: {(2*np.arange(1,n+1)-n-1).dot(x)/(n*x.sum()):.3f}")

# 2) 2023 kesiti: göstergeler ile log10 yatırım / log10 kişi başı yatırım (Spearman)
c = y[y.Yil == 2023].merge(k[k.Yil == 2023], on=["ISO3", "Yil"])
c["pc"] = c.YatirimUSD / c.Nufus
GOST = ["ArGeGsyh", "ArastirmaciMilyon", "KisiBasiGsyh", "Genisband100", "InternetKullanim", "YuksekogretimKayit"]
print("\nGösterge                     n   rho(toplam)   rho(kişi başı)")
for g in GOST:
    s = c.dropna(subset=[g])
    print(f"{g:22s} {len(s):5d}   {stats.spearmanr(s[g], np.log10(s.YatirimUSD)).statistic:+.2f}         {stats.spearmanr(s[g], np.log10(s.pc)).statistic:+.2f}")

# 3) En küçük kareler modelleri (standartlaştırılmış katsayılar)
o = c.dropna(subset=["ArGeGsyh", "KisiBasiGsyh"]).copy()
o["ly"], o["lpc"] = np.log10(o.YatirimUSD), np.log10(o.pc)
o["lg"], o["lp"] = np.log10(o.KisiBasiGsyh), np.log10(o.Nufus)
def ols(dep, xs):
    z = lambda s: (s - s.mean()) / s.std()
    X = np.column_stack([np.ones(len(o))] + [z(o[v]).values for v in xs]); Y = z(o[dep]).values
    b = np.linalg.lstsq(X, Y, rcond=None)[0]; e = Y - X @ b
    return b[1:].round(2), round(1 - e @ e / (Y @ Y), 2)
print("\nM1 (log yatırım ~ Ar-Ge + log GSYH):        ", ols("ly", ["ArGeGsyh", "lg"]), f"n={len(o)}")
print("M2 (M1 + log nüfus):                         ", ols("ly", ["ArGeGsyh", "lg", "lp"]))
print("M3 (log kişi başı yatırım ~ Ar-Ge + log GSYH):", ols("lpc", ["ArGeGsyh", "lg"]))

# 4) Kişi başı yatırım (yıllık ortalama; Σ yatırım / Σ nüfus, yatırım kaydı olan yıllar)
j = y.merge(k[["ISO3", "Yil", "Nufus"]], on=["ISO3", "Yil"])
print(f"\nDünya kişi başı yatırım: {j.YatirimUSD.sum()/j.Nufus.sum():.2f} $")
a = j.groupby("ISO3").agg(inv=("YatirimUSD", "sum"), pop=("Nufus", "sum")); a["pc"] = a.inv / a["pop"]
a["pop23"] = k[k.Yil == 2023].set_index("ISO3").Nufus; a = a[a.pop23 >= 1e6].join(u.set_index("ISO3").UlkeTR).sort_values("pc", ascending=False)
print(a.head(5)[["UlkeTR", "pc"]].round(1).to_string(index=False))
print(f"Türkiye: {a.loc['TUR','pc']:.2f} $ (sıra {list(a.index).index('TUR')+1}/{len(a)})")

# 5) Büyük modeller (2025)
print(f"\nBüyük model üreten ülke (2025): {(m[m.Yil==2025].BuyukModelKumulatif>0).sum()} | toplam kayıt: {m[m.Yil==2025].BuyukModelKumulatif.sum()}")
