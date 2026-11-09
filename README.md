# Yapay Zekâ Ekosistemi: Ülkeler, Yatırımlar ve Kalkınma Göstergeleri

Ülkelerin özel yapay zekâ yatırımlarını; büyük ölçekli yapay zekâ modelleri, nüfus, araştırma-geliştirme (Ar-Ge) ve ekonomik göstergelerle birlikte inceleyen veri analizi ve Power BI raporu.

**Proje türü:** Bitirme projesi  
**Rapor aracı:** Power BI Desktop — Power BI Project (`.pbip`)  
**Kapsam:** 2016–2025 yatırım ve kalkınma verileri; büyük model verisi 2019–2025  
**Ülke boyutu:** 217 ülke/bölge kaydı

> Raporun son tasarım değişiklikleri ve önemli veri kapsamı açıklamaları için [`Tasarim_Notlari.md`](Tasarim_Notlari.md) dosyasına bakın. Projenin yazılı raporu [`1_Rapor/Bitirme_Projesi_Yapay_Zeka_Ekosistemi.pdf`](1_Rapor/Bitirme_Projesi_Yapay_Zeka_Ekosistemi.pdf) konumundadır.

## Rapor sayfaları

1. **Genel Bakış** — küresel yapay zekâ yatırımlarının yıllara göre gelişimi, öne çıkan ülkeler, ABD'nin yatırım payı ve ülke bazında büyük model sayıları.
2. **Kişi Başı Analiz** — kişi başı yatırım, gelir grupları, Ar-Ge göstergeleri ve ülke sıralaması.
3. **Ülke Karşılaştırması** — ülke, yıl ve kıta filtreleriyle yatırım, Ar-Ge ve ekonomik göstergelerin karşılaştırılması.
4. **Türkiye Profili** — Türkiye'nin yatırım serisi, Ar-Ge ve kalkınma göstergeleri ile Dünya medyanı ve gelir grubundaki ülkelerle karşılaştırması.

## Veri kaynakları ve kapsam

| Kaynak | Kullanım | Kapsam / not |
|---|---|---|
| CSET | Özel yapay zekâ yatırımı | Ülke-yıl düzeyinde yatırım; sabit 2021 ABD doları. Yalnızca yatırım kaydı bulunan ülke-yıllar tabloda yer alır. |
| Epoch AI | Büyük ölçekli yapay zekâ sistemleri | 20 ülke için ülke bazında kümülatif model sayısı, 2019–2025. Ülke sayıları küresel toplam olarak yorumlanmamalıdır. |
| Dünya Bankası — World Development Indicators (WDI) | Nüfus, Ar-Ge, araştırmacı, internet, geniş bant, kişi başı GSYH ve yükseköğretim göstergeleri | Kaynak indirme betiği 2015–2025 dönemini ister; hazırlanan model tabloları 2016–2025 yıllarını kullanır. Gösterge bazında eksik değerler bulunabilir. |

Dahil edilen CSV'lerin sütunları ve ayrıntı düzeyleri [`3_Veri/Veri_Sozlugu.md`](3_Veri/Veri_Sozlugu.md) dosyasında açıklanır. Ham kaynak dosyaları [`4_Kod/ham_veri/`](4_Kod/ham_veri/) klasöründedir.

### Veri modelinin özeti

Proje, üç olgu ve iki boyut tablosundan oluşan yıldız şema kullanır. Paketteki mevcut veri kesitinin satır sayıları aşağıdadır; ham veriler yeniden indirildiğinde veya yeniden üretildiğinde değişebilir.

| Tablo | Ayrıntı düzeyi | Satır sayısı |
|---|---|---:|
| `FactYatirim` | Yalnızca yatırım kaydı bulunan ülke × yıl | 697 |
| `FactModel` | Kümülatif büyük model sayısı pozitif olan ülke × yıl | 67 |
| `FactKalkinma` | En az bir gösterge veya nüfus verisi bulunan ülke × yıl | 2.104 |
| `DimUlke` | Ülke | 217 |
| `DimYil` | Yıl (2016–2025) | 10 |

Power BI semantik modelinde 36 DAX ölçüsü bulunur. Raporun son tasarım düzenlemesinde semantik model ve ölçüler değiştirilmemiştir.

## Yöntem ve yorumlama notları

- **Eksik yatırım verisi sıfır değildir.** Yatırım tablosunda ülke-yıl satırının bulunmaması, o ülke-yıl için kaynakta kayıt olmadığını gösterir. Eksik değerler sıfır yatırım olarak kodlanmamalıdır.
- **Kişi başı yatırımın paydası sınırlı kapsamdadır.** Ölçü, yatırım toplamını yatırım kaydı bulunan ülke-yılların nüfusları toplamına böler. Bu nedenle değer, tüm ülkelerin veya tüm yılların nüfusuyla hesaplanan genel bir ortalama değildir.
- **Üst-10 kişi başı yatırım görseli** son seçili yılda nüfusu en az 1 milyon olan ülkeleri kapsar.
- **Gelir grupları Dünya Bankası'nın resmî gelir sınıfları değildir.** Projede kişi başı GSYH'nin 2021–2023 arasındaki son mevcut değerine uygulanan seçilmiş eşikler kullanılır: `<2 bin $`, `2–6 bin $`, `6–15 bin $`, `15–40 bin $` ve `>40 bin $`.
- **Büyük model değerleri ülke bazında kümülatiftir.** Ülkelerin model sayılarının toplamı küresel model toplamı olarak sunulmaz.
- **Türkiye–Dünya karşılaştırmasındaki göstergeler 2023'e sabitlenmiştir.** Yatırım grafiği ise yıllara göre gösterilir.

## Power BI raporunu açma

1. Depoyu klonlayın veya ZIP paketini çıkarın.
2. Power BI Desktop'ta `2_Power_BI/Yapay_Zeka_Ekosistemi/Yapay_Zeka_Ekosistemi.pbip` dosyasını açın.
3. Rapor sayfaları arasında Power BI sayfa sekmeleriyle gezinin. Veri/model kurulumu veya yenileme sorunu yaşarsanız [`2_Power_BI/Manuel_Kurulum/Adimlar.md`](2_Power_BI/Manuel_Kurulum/Adimlar.md) ve [`2_Power_BI/Manuel_Kurulum/DAX_Olculer.txt`](2_Power_BI/Manuel_Kurulum/DAX_Olculer.txt) dosyalarına başvurun.

PBIP dosyası, rapor ve semantik model tanımlarını ayrı klasörlerde tutar. CSV tablolarının dışa aktarılmış halleri ayrıca `3_Veri/` altında bulunur.

## Veriyi yeniden üretme

Python 3 ve aşağıdaki paketler gerekir:

```bash
pip install pandas numpy scipy requests
```

Hazır ham kaynak dosyalarından beş model tablosunu yeniden üretmek için:

```bash
cd 4_Kod
python 01_hazirla_yildiz_sema.py
```

Üretilen CSV dosyaları `../3_Veri/` klasörüne yazılır. Temel analiz ve kontrol sayılarını yeniden hesaplamak için:

```bash
python 02_temel_bulgular.py
```

Dünya Bankası göstergelerini yeniden indirmek isteğe bağlıdır ve internet bağlantısı gerektirir:

```bash
python 00_wdi_indir.py
```

İndirme betiği `wdi_gostergeler.csv` dosyasını çalıştırıldığı klasöre yazar. Veri hazırlama betiği bu dosyayı `4_Kod/ham_veri/wdi_gostergeler.csv` konumunda beklediğinden, yeniden üretimden önce dosyayı bu klasöre taşıyın. `nufus.csv`, CSET yatırımları ve Epoch AI model sayıları için paketteki `ham_veri/` dosyaları da gerekir.

Filtre uygulanmamış mevcut veri kesitinde temel kontrol değerleri yaklaşık olarak **1.725,8 milyar $ toplam yatırım**, **107 yatırım kaydı olan ülke**, **%62,0 ABD payı**, **%89,6 ilk 10 ülke payı**, **20 büyük model üreten ülke**, **28,8 $ dünya kişi başı yatırım** ve **1,53 $ Türkiye kişi başı yatırım** düzeyindedir. Bunlar raporun mevcut veri kesitini kontrol etmek içindir; veri güncellendiğinde değişebilir.

## Depo yapısı

```text
.
├── 1_Rapor/                         # Bitirme projesi PDF raporu
├── 2_Power_BI/
│   ├── Manuel_Kurulum/              # Kurulum adımları ve DAX ölçüleri
│   └── Yapay_Zeka_Ekosistemi/       # PBIP raporu ve semantik model
├── 3_Veri/                          # Power BI modeline ait beş CSV ve veri sözlüğü
├── 4_Kod/
│   ├── ham_veri/                    # Kaynak veri dosyaları
│   └── *.py                         # İndirme, hazırlama ve analiz betikleri
├── README.md
└── Tasarim_Notlari.md
```

## Lisans ve kaynak koşulları

Bu depoda bir `LICENSE` dosyası bulunmadığından proje kodu ve belgeleri için ayrıca bir açık kaynak lisansı belirtilmemiştir. Ham verilerin yeniden kullanımında ilgili kaynakların lisans ve atıf koşullarını kontrol edin.
