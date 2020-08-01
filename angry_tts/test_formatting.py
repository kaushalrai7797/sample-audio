import soundfile
from gtts import gTTS

# import librosa
#
# y, s = librosa.load('tts_1.wav', sr=16000)
# print("new file created")
# print(y)
# print(s)
#
# data, samplerate = soundfile.read('tts_1.wav')
# soundfile.write('new.wav', data, samplerate, subtype='PCM_S8')


# generating a file using gtts
from scipy.io import wavfile
from pydub import AudioSegment
# text = "This is my text in the saving folder"
# tts = gTTS(text)
# tts.save('./sample.mp3')
# sound = AudioSegment.from_mp3("./sample.mp3")
# sound.export("./myfile.wav", format="wav")
fs, data = wavfile.read('/Users/kaushalrai/Desktop/angry_tts/tts_wav/tts_5.wav')
print("fs and data")
print(fs)
print(data)

# from scipy.io import wavfile
# fs, data = wavfile.read('/Users/kaushalrai/Desktop/tts_1.wav')
# print("fs and data")
# print(fs)
# print(data)





# def downsampleWav(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
#     if not os.path.exists(src):
#         print 'Source not found!'
#         return False
#
#     if not os.path.exists(os.path.dirname(dst)):
#         os.makedirs(os.path.dirname(dst))
#
#     try:
#         s_read = wave.open(src, 'r')
#         s_write = wave.open(dst, 'w')
#     except:
#         print 'Failed to open files!'
#         return False
#
#     n_frames = s_read.getnframes()
#     data = s_read.readframes(n_frames)
#
#     try:
#         converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
#         if outchannels == 1:
#             converted = audioop.tomono(converted[0], 2, 1, 0)
#     except:
#         print 'Failed to downsample wav'
#         return False
#
#     try:
#         s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
#         s_write.writeframes(converted)
#     except:
#         print 'Failed to write wav'
#         return False
#
#     try:
#         s_read.close()
#         s_write.close()
#     except:
#         print 'Failed to close wav files'
#         return False
#
#     return True
