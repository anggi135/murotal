import requests
import os
def get_surah_by_number(surah_number, edition):
    url = f'http://api.alquran.cloud/v1/surah/{surah_number}/{edition}'
    response = requests.get(url)
    if response.status_code == 200:
        surah_data = response.json()['data']
        return surah_data
    else:
        print("Failed to fetch surah")
        return None
def play_audio(url):
    os.system(f"mpv {url}")
surah_number = input("Masukkan nomor surah: ")
edition = input("Masukkan edisi Al-Quran (contoh: en.asad): ")

selected_surah = get_surah_by_number(surah_number, edition)

if selected_surah:
    print(f"Memainkan murotal Surah {selected_surah['englishName']}...")
    for ayah in selected_surah['ayahs']:
        audio_url = ayah['audio']
        if audio_url:
            play_audio(audio_url)
else:
    print("Surah tidak ditemukan atau terjadi kesalahan dalam pengambilan data.")
