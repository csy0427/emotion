import pyaudio
import wave
import os
import argparse
import io
import sys
#import msvcrt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"
reload(sys)
sys.setdefaultencoding('euc-kr')

res=''

def record_file(filename):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 5

    WAVE_OUTPUT_FILENAME = filename
    audio = pyaudio.PyAudio()

    # start Recording
    print('Start recording for %d seconds' % RECORD_SECONDS)
    stream = audio.open(format=pyaudio.paInt16,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=2,
                        frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    print('Finished recording')


# [START def_transcribe_file]
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    print('Transcribing audio')

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_sync_request]
    # [START migration_audio_config_file]
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ko-KR')
    # [END migration_audio_config_file]

    # [START migration_sync_response]
    response = client.recognize(config, audio)
    # [END migration_sync_request]
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        res=format(result.alternatives[0].transcript)
        print('Transcript: ' + res)
    # [END migration_sync_response]
# [END def_transcribe_file]

#transcribe_file('Audio.mp3')


def func():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    # args = parser.parse_args()
    wavpath = os.path.join("/Users/soo/Downloads/emotion",'speech.wav')
    # record_file(args.path)
    # transcribe_file(args.path)
    record_file(wavpath)
    transcribe_file(wavpath)
    return res

#func()