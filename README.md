# chk_device

- Installation
  - sudo apt-get install portaudio19-dev
  - pip install sounddevice
  - pip install soundfile
  - pip install scipy
    
- Test
  - python query_snd_devices.py
  - python recorder.py {DEV_ID} {MIC_CH}
  - python wave_play.py {DEV_ID} {FILE_NAME}
