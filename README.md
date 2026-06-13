# AI Music Generator

A deep learning project for generating music using neural networks trained on the MAESTRO dataset.

## Project Structure

- `generate_music.ipynb` - Generate new music from trained model
- `train_model1.ipynb` - Train the neural network
- `preprocess.ipynb` - Preprocess MIDI files
- `music_gui.py` - GUI application for music generation
- `best_model.keras` - Best trained model
- `music_model.h5` - Trained model (HDF5 format)
- `generated_music.mid` - Example generated MIDI file
- `network_input.npy` - Preprocessed input data
- `network_output.npy` - Preprocessed output data
- `notes.pkl` - Pickled notes dictionary
- `maestro-v3.0.0-midi/` - MAESTRO dataset

## Requirements

- Python 3.x
- TensorFlow/Keras
- Music21
- NumPy
- Pandas

## Installation

```bash
pip install tensorflow music21 numpy pandas
```

## Usage

Run the GUI application:
```bash
python music_gui.py
```

Or use the Jupyter notebooks for training and generation.

## Note


## Output Images ##

https://github.com/Saravanabalaji2007/Ai-Music-Generator/blob/fe9d9f51806a215715f78d5b0fadc5ccc063600d/ai%20music%20pic1.jpeg

https://github.com/Saravanabalaji2007/Ai-Music-Generator/blob/fe9d9f51806a215715f78d5b0fadc5ccc063600d/ai%20music%20pic2.jpeg



Large files (*.npy, *.h5, *.keras) are tracked with Git LFS for version control.
