# Veri sözlüğü (yıldız şema)

| Tablo | Tür | Ayrıntı düzeyi | Satır |
|---|---|---|---|
| FactYatirim | Olgu | Ülke × yıl (yalnızca yatırım kaydı olan) | 697 |
| FactModel | Olgu | Ülke × yıl (kümülatif model sayısı > 0) | 67 |
| FactKalkinma | Olgu | Ülke × yıl (en az bir gösterge veya nüfus dolu) | 2.104 |
| DimUlke | Boyut | Ülke | 217 |
| DimYil | Boyut | Yıl (2016–2025) | 10 |

| Sütun | Tablo | Açıklama |
|---|---|---|
| ISO3, Yil | tüm olgular | Anahtarlar (DimUlke[ISO3], DimYil[Yil]) |
| YatirimUSD | FactYatirim | Özel yapay zekâ yatırımı, sabit 2021 $ (CSET) |
| BuyukModelKumulatif | FactModel | Kümülatif büyük ölçekli yapay zekâ sistemi sayısı (Epoch AI; 20 ülke, 2019–2025) |
| Nufus | FactKalkinma | Toplam nüfus (SP.POP.TOTL) |
| ArGeGsyh | FactKalkinma | Ar-Ge harcaması, % GSYH (GB.XPD.RSDV.GD.ZS) |
| ArastirmaciMilyon | FactKalkinma | Milyon kişiye düşen araştırmacı (SP.POP.SCIE.RD.P6) |
| InternetKullanim | FactKalkinma | İnternet kullanan nüfus, % (IT.NET.USER.ZS) |
| Genisband100 | FactKalkinma | 100 kişiye düşen sabit genişband (IT.NET.BBND.P2) |
| KisiBasiGsyh | FactKalkinma | Kişi başı GSYH, güncel $ (NY.GDP.PCAP.CD) |
| YuksekogretimKayit | FactKalkinma | Yükseköğretim brüt kayıt oranı, % (SE.TER.ENRR) |
| UlkeTR, Kita | DimUlke | Türkçe ülke adı ve kıta |
| GelirGrubu | DimUlke | Kişi başı GSYH'ye göre sınıf (2021–2023 son değer): <2k, 2–6k, 6–15k, 15–40k, >40k $; projede seçilmiş eşikler |

Boş değer = kayıt/veri yok. Yatırım ve model tablolarında satırın bulunmaması "kayıt yok" anlamına gelir (sıfır yatırım olarak yorumlanmamalıdır).
