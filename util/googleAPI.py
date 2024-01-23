import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key = API_KEY)


def get_safety_settings():
    safety_settings = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]

    return safety_settings

def paint_generation_config():
    generation_config = {
            "temperature" : 1.0,
            "top_p" : 1.0,
            "top_k" : 40,
        }
    
    return generation_config

def modify_sentiment(text_input, selected_tone, selected_sentiment, strength, text_length):
    model = genai.GenerativeModel("gemini-pro")
    
    messages = [
        {'role' : 'user',
         'parts': [f"""Keeping the same content, hange the sentiment of this text to both {selected_tone} while being
                   {selected_sentiment}, with strength {strength} which is on a scale from 0 to 10.
                   Keep the information as similar as possible, and keep it around {text_length}: {text_input}"""]}
    ]

    result = model.generate_content(messages, safety_settings=get_safety_settings())
    return result.text

def analyze_sentiment(context, text_input):
    model = genai.GenerativeModel("gemini-pro")
    
    messages = [
        {'role':'user',
         'parts':[f"""Analyze the sentiment of this text: {text_input} with this context: {context}. 
                  Try to dig out the deepest feeling the author is trying to convey.
                  If there are multiple possibilities, tell us all of them. If you think the context is not enough, 
                  simply say "More context is required." and we will provide more context for you."""]}
    ]
    
    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def analyze_suspicious_lines(age, text):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""{age} years old student wrote this essay. Bring suspicious lines that you think that are AI generated. 
                  Deeply consider that the student is {age} years old. AI generated text tends to use overly complicated terminology,
                  and tends to phrase out everything very long. Here is the text: {text}"""]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def ai_debate(topic, my_opinion, opponent_opinion, my_arguments, opponents_arguments):
    ai_model = genai.GenerativeModel("gemini-pro")

    if len(my_arguments) == 0:
        my_arguments = "no arguments yet"
    if len(opponents_arguments) == 0:
        opponents_arguments = "no arguments yet"
    
    messages = [
        {'role':'user',
        'parts':[f"""Keep your arguments under 100 words. Give one side of the argument only, in conversational.
        {topic} is the topic of the debate. You think {my_opinion}. You must use convincing arguments 
        to convince me that you are right. You have previously said {my_arguments} and I have previously said {opponents_arguments}. 
        Never repeat what we have said before, always try to think of new arguments. Try to use more conversational language, 
        such as "I disagree" or "That is a terrible idea". You don't have to use true facts and logic, only focus on convincing me that you are right."""]}
    ]

    result = ai_model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def ai_rebuttal(topic, my_opinion):
    ai_model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
        'parts':[f"""Keep your arguments under 100 words. Give one side of the argument only, in conversational.
        {topic} is the topic of the debate. You think {my_opinion}. You must use convincing arguments
        to convince me that you are right. You don't have to use true facts and logic, only focus on convincing me that you are right."""]}
    ]

    result = ai_model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def poem_analyzer(poem, age, language, formality, topic, paragraphs, length):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""{poem} is the poem. Write an essay about this poem, answering {topic}. The essay must be approximately {length} words long, 
        {paragraphs} paragraphs long, an introduction and a conclusion. In each paragraph you must focus on a single language feature, analyze it so that it answers the question
        The introduction should outline the main languages features used. The paragraph should be in this format. 1. Topic Sentence to introduce the language feature and general topic of the
        paragraph, 2. The actual quote of the language feature, 3. Explain the language feature, 4. Explain how the language feature answers the question, 5. Explain the social impact through the analysis
        It should be {formality} formal, which is on a scale from 0 to 1, 1 being the most formal.
        You are {age} years old and you must write an essay that is suitable for your age. You must write an essay in {language}, but when you give reference
        to the original text you must use the original language"""]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text


def determine_importance(input_dict):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
        'parts':[f"""{input_dict} are the news articles, paired between title and description. Determine the importance of each article.
                 It should be in this format:

                 Input: [dict(title, link, description), dict(title, link, description),dict(title, link, description),dict(title, link, description),dict(title, link, description)]
                 Output:5,2,3,1,9

                 The importance is on a scale from 0 to 10. 0 means not important and 10 means very important.
                 Only return the importance, nothing else"""]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def paint_captioning(image):
    model = genai.GenerativeModel("gemini-pro-vision", generation_config=paint_generation_config())

    messages = ["""This is a painting. Write a short caption on this painting, such as what you think it is.
                Also comment on how old you think the painter would be""", image]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def paint_analysis(image):
    model = genai.GenerativeModel("gemini-pro-vision", generation_config=paint_generation_config())

    messages = ["""This is a painting. Analyze this painting in depth. Talk about the emotions, the complexity of the line structures,
                symbolic meanings and the social impact of the painting. Talk about which artistic movement this painting belongs to.
                Focus on the symbolic meaning. Comment on how amazing the painting is""", image]
    
    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text



def image_captioning(image):
    model = genai.GenerativeModel("gemini-pro-vision")

    messages = ["Write a short caption on this picture. Make it as detailed as possible", image]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text
    
def image_questioning(image, question):
    model = genai.GenerativeModel("gemini-pro-vision")

    messages = [f"""Based on this picture, answer this question. If you think there is not enough information on the
                image, then say so. The question is : {question}""", image]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def video_captioning(frame_caption_list):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""There is a  video, and you must summarize the contents of the video. I do not have the video,
                  but I have the captions of the video frame, every few seconds. Your role is to analyze the captions,
                  and try to extract what happens in the video. It will not be enough to simply list what is present in the
                  video. You must analyze the captions, and figure out what is the main idea of the video. The captions are
                  {frame_caption_list}

                Try to be as detailed as possible. It will help if you try to figure the relationship between each adjacent frame captions"""]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def video_questioning(frame_caption_list, question):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""There is a  video, and you must answer this question. I do not have the video,
                  but I have the captions of the video frame that tries to answer the question with that frame
                  , every few seconds. Your role is to analyze the captions, and try to extract the answer the the question. The captions are
                  {frame_caption_list}

                Try to be as detailed as possible. It will help if you try to figure the relationship between each adjacent frame captions.
                The question is : {question}"""]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def get_word_embedding(word):
    return genai.embed_content(
        model = 'models/embedding-001',
        content = word,
        task_type = 'clustering'
    )['embedding']

def get_sentence(language, level, num_sentences):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""I am learning {language} at {level} level. I want to practice my sentence translation.
                  Give me {num_sentences} sentences in {language} that I can translate to English. The sentence should be around 20 words long
                  and should be {level} level. All {num_sentences} sentences should be completely different context, and beneficial for learning.
                  The output should be in this format : 
                  1. Sentence 1
                  2. Sentence 2 (If more than one sentence)
                  3. Sentence 3 (If more than two sentences)
                  4. Sentence 4 (If more than three sentences)
                  and so on.
                  NEVER provide the english translation of the sentence, never provide more sentences than the number of sentences requested.
                  """]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def evaluate_translation(sentences, translations, language, level):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""I am learning {language} at {level} level. I want to practice my sentence translation.
                  I have translated these sentence : {sentences} into {translations}. The numbers will be corresponding
                  How well did I do? Considering my level, for each of my translation, rate my translation on a scale from 0 to 10. 
                  0 means completely wrong, and 10 means completely correct.

                  If I am more fluent in this language, you must be more strict on me. Be as strict as possible.
                  Also, if the translation is not yet perfect, for each translation, tell me which part of the translation is wrong, 
                  and how I can improve it. Finally, for each sentence, provide me with a good translation of the sentence in English, so that I can learn from it. 
                  
                  The output format should be:
                  Sentence 1 : 
                  1. Rating : 5 / 10
                  2. Feedback : The translation is wrong because ...
                  3. Good translation : The good translation in English is ...

                  Sentence 2 :
                  1. Rating : 10 / 10
                  2. Feedback : The translation is good because ...
                  3. Good translation : The good translation in English is ...
                  """]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def get_words(language, level, num_words):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""I am learning {language} at {level} level. I want to practice my vocabulary.
                  Give me {num_words} words in {language} that I can translate to English. The words should be at {level} level, and
                  must be a single word. It should be a good word for a person at {level} level to learn.
                  All {num_words} words should be completely different context, and beneficial for learning.
                  The output should be in this format : 
                  1. Word 1
                  2. Word 2 (If more than one word)
                  3. Word 3 (If more than two words)
                  4. Word 4 (If more than three words)
                  and so on.
                  NEVER provide the english translation of the word, never provide more words than the number of words requested.
                  """]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def evaulate_words(words, answers, language, level):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""I am learning {language} at {level} level. I want to practice my vocabulary.
                  I have translated these words : {words} into {answers}. The numbers will be corresponding
                  How well did I do? Considering my level, for each of my translation, rate my translation on a scale from 0 to 10. 
                  0 means completely wrong, and 10 means completely correct.

                  If I am more fluent in this language, you must be more strict on me. Be as strict as possible.
                  Also, if the translation is not yet perfect, for each translation, tell me which part of the translation is wrong, 
                  and how I can improve it. Finally, for each word, provide me with a good translation of the word in English, 
                  so that I can learn from it. The provided translation should be as advanced as possible. Even if the translation is correct,
                  if there is a more advanced translation, you should provide it.

                  The output format should be:
                  Word 1 : 
                  1. Correct / Incorrect
                  2. Feedback : The translation is wrong because ...
                  3. Suggestion : (Better translation for the word)

                  Word 2 :
                  1. Correct / Incorrect
                  2. Feedback : The translation is wrong because ...
                  3. Suggestion : (Better translation for the word)
                  """]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def translate_code(input_code, input_language, output_language):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""I am a programmer who is working on old legacy code. I want to translate this code from
                  {input_language} to {output_language}. I want to keep the behaviour of the code as similar as possible.
                  The Code is : {input_code} in {input_language}. I want to translate it to {output_language}.
                  Keep the behaviour of the code as similar as possible. The output should be in this format : 
                  This is the translated result. <Short description of the behaviour of the code>
                  <Output code>
                  """]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def solve_algorithm(question, input_language):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""I am a programmer who is working on an algorithm problem. I want to solve this problem in {input_language}.
                  The question is : {question}. The problem is complicated, but it gives number of expected inputs and output
                  examples. Focus on fully understanding the problem by understanding the expected inputs and outputs.
                  The output should be in this format : 
                  This is the solution. <Short description of the behaviour of the code>
                  <Output code>
                  """]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def create_prompt(input_problem):
    model = genai.GenerativeModel("gemini-pro")

    messages = [
        {'role':'user',
         'parts':[f"""I am a programmer who is using Gemini pro to solve a problem. However, I don't have enough time
                  to write a detailed prompt for this problem. The problem is:
                  {input_problem}
                
                  Make a Gemini-pro prompt for this problem. Make it so that it is very detailed, explains the problem and
                  depth, and give examples of expected inputs and outputs. Explain the role of the AI model, such as a profressional
                  translator if the task is related to translating a language.

                  The output should be in this format
                  I am a <role> who is interested in solving <input_problem>
                  Solve this problem by <description and example of the problem>
                  """]}
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text