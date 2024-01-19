import util.googleAPI as lms
import tqdm

with open("const/word_list.txt", "r") as f:
    # Read through all the word, and get the word embedding
    # Save the word embedding into the const/word_embeddings.csv, first column is the word, second column is the embedding

    word_with_embedding = {}
    for i in tqdm.tqdm(range(6801)):
        word = f.readline().strip()
        if not word:
            break
        embedding = lms.get_word_embedding(word)
        word_with_embedding[word] = embedding
    
    f.close()

with open("const/word_embeddings.csv", "w") as f:
    for word, embedding in word_with_embedding.items():
        f.write(f"{word},{embedding}\n")

    f.close()