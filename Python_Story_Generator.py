import random
from colorama import Fore, Style

def generate_story():
    # Get user inputs
    place = input("Enter the name of a place: ")
    action = input("Enter an action: ")
    character = input("Enter a character: ")
    emotion = input("Enter an emotion: ")
    genre = input("Enter a genre (e.g., fantasy, sci-fi, mystery): ")
    mood = input("Enter a mood (e.g., happy, mysterious, adventurous): ")
    
    # Additional user-provided words
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")
    word3 = input("Enter another word: ")
    word4 = input("Enter another word: ")

    # Lists of possible story elements
    story_beginning = [f"{Fore.RED}Once upon a time in", f"In a faraway land called", "Deep within the heart of"]
    story_middle = [f"{Fore.YELLOW}a brave", "an adventurous", "a curious"]
    story_ending = [f"{Fore.LIGHTBLUE_EX}went on a journey.", "discovered a hidden treasure.", "made unexpected friends."]
    
    # Customized story elements
    story_genre = [f"{Fore.LIME}In the mystical realm of {genre},", f"Amidst the futuristic world of {genre},"]
    story_mood = [f"{Fore.MAGENTA}in a {mood} atmosphere,", f"with a {mood} ambiance,"]
    story_words = [f"{word1} and {word2}", f"{word3} around every corner", f"whispering secrets of {word4}."]

    # Create a random story
    beginning = random.choice(story_beginning)
    middle = random.choice(story_middle)
    ending = random.choice(story_ending)
    genre_part = random.choice(story_genre)
    mood_part = random.choice(story_mood)
    words_part = random.choice(story_words)

    # Display the generated story
    print(f"\n{beginning} {place}, {character} {action} {emotion} with {middle} spirit and {ending}")
    print(f"{genre_part} {character} embarked on a journey {mood_part} {words_part}{Style.RESET_ALL}")

if __name__ == "__main__":
    generate_story()
