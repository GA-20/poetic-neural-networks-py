# Poetic Neural Network

This is a project that uses a neural network to generate poetry. The neural network is trained on a dataset of poems and then generates new poems based on the patterns it has learned.

It's part my personal training in deep learning and part a fun project to see what kind of poetry a neural network can come up with.

The resource I used to train the neural network is the [NeuralNine](https://www.neuralnine.com/generating-texts-with-recurrent-neural-networks-in-python/)

The code is overcommented to help me understand what's going on and to help others who are learning about neural networks, so if you're an expert, I apologize for the verbosity.

## LSTM

![LSTM](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/LSTM_Cell.svg/1920px-LSTM_Cell.svg.png)

LSTMs are a special kind of neural network architecture called a recurrent neural network (RNN). RNNs are designed to handle sequential data, where the order of elements matters.

LSTM can potentially retain that context through its cell state and use it to make a more accurate prediction.

Since recurrent neural networks and LSTMs in particular have a short term memory, we can train it to “guess” the next letter based on the letters that came before. That leads to our network producing these texts. For this of course we will need some substantial training data.

## Text to numerical

We cannot just train a neural network on letters or sentences. We need to convert all of these values into numerical data.

So we have to come up with a system that allows us to convert the text into numbers, then predict specific numbers based on that data and then again convert the resulting numbers back into text.

### Text Preprocessing

Text processing can include many transformations of text, such as:

- Remove unnecessary characters like punctuation marks, symbols, or special characters (depending on needs).
- Convert text to lowercase for consistency.
- Stemming or lemmatization to reduce words to their root form.

In this exercise, the lowercase technique is the only one used.

### Text Tokenization

Break down the text into smaller units. This could be words, characters, or n-grams (sequences of n consecutive words). For this example the text size is reduced to avoid make the problem a bit complex at this point.

### Vocabulary Building

Create a dictionary (vocabulary) that maps each unique token (word, character, or n-gram) to a unique integer identifier. This allows the network to recognize different tokens.

## How to install

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```
