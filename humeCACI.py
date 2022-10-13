# This program test python prints Hello, world!

#print('Hello, world!')

# python file for recieving fetather input

# idea of code from https://hackaday.io/project/165403/logs?sort=oldest

# To enable Python to interact with your radio, extract all the files from librtlsdr 
# directly into your Python folder.
# download from https://github.com/librtlsdr/librtlsdr
from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 70e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

print(sdr.read_samples(512))