from cgi import print_arguments
import sounddevice
from scipy.io.wavfile import write
fs = 44100 # فرکانس
sec = int(input(":لطفا زمان را وارد کنید"))
print(".... در حال ضبط")
record_voice = sounddevice.rec( int (sec * fs ), samplerate= fs, channels= 2)
sounddevice.wait()
write("rec.wav", fs, record_voice)
print("ضبط تمام شد فایل خروجی را چک کنید")