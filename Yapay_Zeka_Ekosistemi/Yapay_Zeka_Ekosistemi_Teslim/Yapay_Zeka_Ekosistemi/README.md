# Yapay Zekâ Ekosistemi – Bitirme Projesi Teslim Paketi

Özel yapay zekâ yatırımı (CSET), büyük ölçekli yapay zekâ modelleri (Epoch AI) ve Dünya Bankası göstergeleri ile nüfus verisini birleştiren, Power BI raporlu ülke bazlı veri analizi.

| Klasör | İçerik |
|---|---|
| `1_Rapor` | Bitirme projesi raporu (PDF) |
| `2_Power_BI` | Power BI projesi (`.pbip`, yıldız şema: 3 olgu + 2 boyut tablosu, 36 ölçü, 4 rapor sayfası) ve manuel kurulum rehberi |
| `3_Veri` | Modelin 5 tablosu (CSV) ve veri sözlüğü |
| `4_Kod` | Python betikleri ve ham kaynak dosyaları |

## Power BI dosyasını açma
1. Zip'i bir klasöre çıkar. 2. Power BI Desktop > Dosya > Aç > Raporlara gözat > dosya türünü "Tüm dosyalar" yap > `2_Power_BI/Yapay_Zeka_Ekosistemi/Yapay_Zeka_Ekosistemi.pbip`. 3. **Yenile**'ye bas (veri dosyanın içinde gömülü). 4. İstersen Dosya > Farklı kaydet ile `.pbix` yap.
Açılmazsa: `2_Power_BI/Manuel_Kurulum/Adimlar.md`.

Doğrulama (filtre yokken): Toplam Yatırım ≈ 1.725,8 milyar $; Yatırım Alan Ülke Sayısı 107; ABD Payı %62,0; İlk 10 Ülke Payı %89,6; Büyük Model Üreten Ülke Sayısı 20; Dünya Kişi Başı Yatırım ≈ 28,8 $; Türkiye Kişi Başı Yatırım ≈ 1,53 $.

## Verileri ve sayıları yeniden üretme
```
cd 4_Kod
pip install pandas scipy numpy
python 01_hazirla_yildiz_sema.py     # ham_veri -> ../3_Veri
python 02_temel_bulgular.py          # rapordaki temel sayıları yazdırır
```
`00_wdi_indir.py`: Dünya Bankası verisini yeniden indirmek için (isteğe bağlı; internet gerekir).

Rapor PDF'indeki düzeltilmesi gereken noktalar için `Duzeltme_Notlari.md` dosyasına bakın.
