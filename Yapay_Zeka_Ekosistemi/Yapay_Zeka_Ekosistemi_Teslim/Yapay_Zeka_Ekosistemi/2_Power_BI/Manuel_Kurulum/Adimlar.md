# Manuel kurulum (proje dosyası açılmazsa, yaklaşık 15 dakika)

1. Power BI Desktop > **Veri al > Metin/CSV** ile `3_Veri` klasöründeki 5 dosyayı yükle (Yükle): FactYatirim, FactModel, FactKalkinma, DimUlke, DimYil.
2. **Model görünümünde** şu 6 ilişkiyi kur (bire-çok, tek yön, etkin): DimUlke[ISO3] → FactYatirim[ISO3], FactModel[ISO3], FactKalkinma[ISO3]; DimYil[Yil] → FactYatirim[Yil], FactModel[Yil], FactKalkinma[Yil].
3. `DAX_Olculer.txt` dosyasındaki ölçüleri **Modelleme > Yeni ölçü** ile oluştur (köşeli parantez içindeki ad ölçü adı, eşitlikten sonrası formüldür).
4. Raporu `1_Rapor` içindeki PDF'te Şekil 15–18'e bakarak kur (Genel Bakış, Kişi Başı Analiz, Ülke Karşılaştırması, Türkiye Profili).
5. **Dosya > Farklı kaydet** ile `.pbix` yap.
