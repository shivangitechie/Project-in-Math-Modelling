from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, MaxPooling1D, Flatten, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Initialize tokenizer
tokenizer = Tokenizer(num_words=5000)  # Keep top 5000 words
tokenizer.fit_on_texts([" ".join(lemmatized_words)])  # Train tokenizer on cleaned text

# Convert texts to sequences
sequences = tokenizer.texts_to_sequences([" ".join(lemmatized_words)])

# Pad sequences to ensure uniform input size
max_length = 100  # Choose max length based on dataset
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding="post")

print(padded_sequences.shape)  # (1, max_length)

# Define CNN model
model = Sequential([
    Embedding(input_dim=5000, output_dim=128, input_length=max_length),  # Word embeddings
    Conv1D(filters=64, kernel_size=3, activation="relu"),  # Convolution Layer
    MaxPooling1D(pool_size=2),  # Downsampling
    Flatten(),  # Flatten for Fully Connected Layer
    Dense(64, activation="relu"),  # Fully Connected Layer
    Dense(4, activation="softmax")  # 4 categories: Boom, Bust, Play with injury, Play meaningful minutes
])

# Compile model
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Show model summary
model.summary()
