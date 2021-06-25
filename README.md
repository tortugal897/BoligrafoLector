# BoligrafoLector

This proyect is created with the aim for helping old, blind or illiterate people read a physical text.

This code uses a Raspberry Pi Zero in order to read and reproduce a physical text using free software.
It uses a camera module, a Raspberry Pi Zero, a ReSpeaker 2-Mics Pi HAT and a speaker.

The process is as it follows:
- The camera takes a picture
- OpenCV modifies it to improve the characteristics of the picture for ussing of and OCR.
- Tesseract OCR recognizes any text in the image.
- Pico TTS creates an audio file using the recognized text as its content.
- VLC media player reproduces the audio through the speakers
