import streamlit as st

# Fungsi untuk menghitung total konsumsi bahan bakar
def hitung_total_konsumsi_bahan_bakar(jarak_tempuh, rata_rata_konsumsi, pulang_pergi):
    total_jarak = 2 * jarak_tempuh if pulang_pergi else jarak_tempuh
    return total_jarak / rata_rata_konsumsi

# Fungsi untuk menghitung estimasi harga bensin
def hitung_estimasi_harga(total_konsumsi_bahan_bakar, harga_bensin):
    return total_konsumsi_bahan_bakar * harga_bensin

# Fungsi untuk menghitung total biaya taksi
def hitung_total_ongkos_taksi(jarak_tempuh, ongkos_taksi_per_km, pulang_pergi):
    total_jarak = 2 * jarak_tempuh if pulang_pergi else jarak_tempuh
    return total_jarak * ongkos_taksi_per_km

# Fungsi untuk menampilkan garis pemisah
def print_separator():
    st.write("---")

def main():
    st.title("Estimasi Biaya Perjalanan")
    st.image("https://cdn.pixabay.com/photo/2017/06/20/10/32/taxi-2424787_960_720.png", width=200)  # Menampilkan logo bawaan Streamlit dengan lebar 200 pixel
    st.write("### Masukkan detail perjalanan Anda:")

    kendaraan = {
        'jarak_tempuh': st.number_input("Jarak tempuh (km):", min_value=0.1, step=0.1),
        'rata_rata_konsumsi': st.number_input("Rata-rata konsumsi bahan bakar (km/l):", min_value=0.1, step=0.1),
        'harga_bensin': st.number_input("Harga bensin per liter (Rp):", min_value=0.1, step=0.1),
        'biaya_tol': st.number_input("Biaya tol (Rp):", min_value=0),
        'pulang_pergi_bahan_bakar': st.radio("Perjalanan pulang pergi untuk bahan bakar?", ("Tidak", "Ya")) == "Ya"
    }

    print_separator()

    total_konsumsi_bahan_bakar = hitung_total_konsumsi_bahan_bakar(kendaraan['jarak_tempuh'], kendaraan['rata_rata_konsumsi'], kendaraan['pulang_pergi_bahan_bakar'])
    estimasi_harga_bensin = hitung_estimasi_harga(total_konsumsi_bahan_bakar, kendaraan['harga_bensin'])
    konsumsi_per_km = 1.0 / kendaraan['rata_rata_konsumsi']
    harga_per_km = estimasi_harga_bensin / (2 * kendaraan['jarak_tempuh'] if kendaraan['pulang_pergi_bahan_bakar'] else kendaraan['jarak_tempuh'])

    st.write(f"**Jarak Tempuh:** {kendaraan['jarak_tempuh']} km")
    st.write(f"**Total Konsumsi Bahan Bakar:** {total_konsumsi_bahan_bakar:.2f} liter")
    st.write(f"**Estimasi Harga Bensin:** Rp {estimasi_harga_bensin:.2f}")
    st.write(f"**Biaya Tol:** Rp {kendaraan['biaya_tol']:.2f}")
    st.write("**Konsumsi dan Harga Per Kilometer:**")
    st.write(f"1 km \t: {konsumsi_per_km:.2f} liter \t Rp {harga_per_km:.2f}")

    print_separator()

    kendaraan['ongkos_taksi_per_km'] = st.number_input("Ongkos taksi per km (Rp):", min_value=0.1, step=0.1)
    kendaraan['pulang_pergi_taksi'] = st.radio("Perjalanan pulang pergi untuk taksi?", ("Tidak", "Ya")) == "Ya"

    print_separator()

    total_ongkos_taksi = hitung_total_ongkos_taksi(kendaraan['jarak_tempuh'], kendaraan['ongkos_taksi_per_km'], kendaraan['pulang_pergi_taksi'])
    total_keseluruhan = estimasi_harga_bensin + total_ongkos_taksi + kendaraan['biaya_tol']

    st.write(f"**Total Ongkos Taksi:** Rp {total_ongkos_taksi:.2f}")
    st.write(f"**Total Keseluruhan (Bensin + Ongkos Taksi + Tol):** Rp {total_keseluruhan:.2f}")

    print_separator()

    diskon = st.number_input("Masukkan diskon (%):", min_value=0.0, max_value=100.0)
    st.write("---")

    total_setelah_diskon = total_keseluruhan - (total_keseluruhan * (diskon / 100.0))

    st.write(f"**Total setelah diskon:** Rp {total_setelah_diskon:.2f}")

if __name__ == "__main__":
    main()
