import pandas as pd
import folium

# Load data hasil MapReduce
data = pd.read_csv('hasil_mapreduce.csv')

# Membuat peta
peta = folium.Map(location=[-7.978, 112.63], zoom_start=12)

# Menambahkan marker untuk setiap kelurahan
for index, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=row['jumlah_pendukung'] * 0.1,
        color='blue',
        fill=True,
        fill_opacity=0.6,
        popup=f"{row['kelurahan']}: {row['jumlah_pendukung']} pendukung"
    ).add_to(peta)

# Simpan peta ke file HTML
peta.save('peta_calon_pemilih.html')
