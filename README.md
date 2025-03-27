# PitchDetect

This is a Python program that can guess musical notes based on microphone input. The program uses the PyAudio library to record audio from the microphone, and then uses the Fast Fourier Transform (FFT) to calculate the frequency of the signal. It then maps that frequency to a musical note using the formula for calculating the frequency of a note relative to A440.

## Installation

To use this program, you'll need to install the following dependencies:

- Python 3.6 or higher
- NumPy
- PyAudio

You can install NumPy and PyAudio using pip:
`pip install numpy`
`pip install pyaudio`

## Usage

To run the program, simply run the `main.py` file:

`python main.py`

The program will continuously record audio from the microphone and print out the musical note corresponding to the input.

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and improvements to documentation.


The program will continuously record audio from the microphone and print out the musical note corresponding to the input.

## License

This project is licensed under the GNU 3.0 License. See the `LICENSE` file for details.
