# multilayer-perceptron

TODO Structure maybe :

```
mlp_project/
├── README.md
├── requirements.txt        # List dependencies (if any)
├── data/
│   ├── raw_data.csv        # Your original dataset
│   ├── train.csv           # (Generated) Training data
│   └── validation.csv      # (Generated) Validation data
├── mlp/                    # Package containing the core MLP code
│   ├── __init__.py
│   ├── network.py          # Implementation of the MLP (forward/backprop, weight updates, etc.)
│   ├── activations.py      # Activation functions and their derivatives
│   ├── loss.py             # Loss functions (and possibly metrics)
│   └── optimizers.py       # Optional: optimization routines if you want to extend beyond basic gradient descent
├── utils/
│   ├── __init__.py
│   └── data_utils.py       # Functions for loading, splitting, and preprocessing data
├── scripts/
│   ├── split_data.py       # Program to separate raw data into training and validation sets
│   ├── train.py            # Training program: loads training data, initializes the MLP, and runs training
│   └── predict.py          # Prediction program: loads a saved model and runs predictions on new data
└── main.py                 # Optional: single entry point that uses command-line options to select the phase (split, train, or predict)
```