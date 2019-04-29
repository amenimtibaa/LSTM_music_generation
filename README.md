# LSTM_music_generation

This project allows you to train a long short-term memory neural network on google TPU to generate midi music files that make use of a single instrument (piano) 

## Getting Started

These instructions will get you a copy of the project up and running:

* Clone the repository 
``` git clone --recursive https://github.com/amenimtibaa/LSTM_music_generation.git```
* Run **extract_notes.py** on your local IDE - the notes will be extracted from the *input_music* folder that contains MIDI piano music of classical composers (Beethoven, Mozart, Bach, Chopin)-
the goal was to see what would be a mix of great musicians composition. 
* Put the notes files in your drive ( or use the one you cloned ) .
* Open **LSTM_music_generation.ipynb** on then click on *open on colab* you will be transferred to Colaboratory which is a Jupyter notebook environment that requires no configuration and runs entirely in the cloud.
* Once on colab go to Execution => modify the execution type
* Set type of execution to Python3 and hardware accelerator to TPU ( to make the most of resources provided by colab ) 
* Go to execution => execute everything
