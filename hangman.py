import random
# Function to select a random word from a list along with its hint
def select_random_word():
    word_list = [
        ("computer", "Electronic device for processing data."),
        ("phone", "Communication device used to make calls."),
        ("car", "Vehicle used for transportation."),
        ("coffee", "Popular beverage made from roasted beans."),
        ("book", "Written or printed work consisting of pages."),
        ("music", "Art form consisting of sound and silence."),
        ("house", "Building used as living space."),
        ("school", "Institution for educating children."),
        ("internet", "Global computer network."),
        ("pizza", "Italian dish consisting of dough and toppings."),
        ("guitar", "Musical instrument with strings."),
        ("keyboard", "Input device for computers."),
        ("bicycle", "Two-wheeled vehicle propelled by pedals."),
        ("television", "Electronic device for receiving broadcast signals."),
        ("restaurant", "Establishment where meals are served to customers."),
        ("dog", "Domesticated mammal often kept as a pet."),
        ("cat", "Small domesticated carnivorous mammal."),
        ("phone", "Communication device used to make calls."),
        ("pen", "Writing instrument."),
        ("pencil", "Writing instrument with a graphite core."),
        ("shoe", "Footwear worn to protect and comfort the foot."),
        ("table", "Furniture item with a flat top and one or more legs."),
        ("chair", "Furniture item for sitting."),
        ("bed", "Furniture item for sleeping."),
        ("lamp", "Lighting device."),
        ("window", "Opening in a wall for light and air."),
        ("door", "Moveable barrier used to open and close an entrance."),
        ("tree", "Large woody plant."),
        ("flower", "Reproductive structure of flowering plants."),
        ("book", "Written or printed work consisting of pages."),
        ("paper", "Thin material used for writing or printing."),
        ("cup", "Small open container used for drinking."),
        ("plate", "Shallow dish used for serving food."),
        ("spoon", "Utensil used for eating."),
        ("fork", "Utensil with prongs used for eating."),
        ("knife", "Utensil with a sharp blade used for cutting."),
        ("watch", "Timekeeping device worn on the wrist."),
        ("clock", "Timekeeping device."),
        ("bag", "Container used for carrying items."),
        ("hat", "Head covering."),
        ("jacket", "Garment worn on the upper body."),
        ("shirt", "Garment worn on the upper body."),
        ("pants", "Garment worn on the lower body."),
        ("socks", "Garment worn on the feet."),
        ("gloves", "Hand covering."),
        ("scarf", "Clothing item worn around the neck."),
        ("belt", "Accessory worn around the waist."),
        ("wallet", "Container for holding money and cards."),
        ("keys", "Metal instruments used for locking and unlocking doors."),
        ("ring", "Small circular band worn as jewelry."),
        ("bracelet", "Ornamental band worn around the wrist."),
        ("necklace", "Ornamental chain worn around the neck."),
        ("earrings", "Ornamental jewelry worn on the ears."),
        ("watch", "Timekeeping device worn on the wrist."),
        ("mirror", "Reflective surface."),
        ("brush", "Tool with bristles used for cleaning or grooming."),
        ("toothbrush", "Brush used for cleaning teeth."),
        ("toothpaste", "Dentifrice used with a toothbrush."),
        ("shampoo", "Hair cleansing product."),
        ("soap", "Cleaning agent used for washing."),
        ("towel", "Absorbent cloth used for drying."),
        ("shower", "Device for washing the body."),
        ("bathroom", "Room containing a bath or shower."),
        ("kitchen", "Room used for cooking."),
        ("living room", "Room in a house for relaxing."),
        ("bedroom", "Room used for sleeping."),
        ("dining room", "Room used for eating meals."),
        ("office", "Room used for work or study."),
        ("garage", "Building for housing vehicles."),
        ("garden", "Outdoor space for growing plants."),
        ("park", "Public open space for recreation."),
        ("restaurant", "Establishment where meals are served to customers."),
        ("cafe", "Small restaurant serving light meals and drinks."),
        ("bar", "Establishment serving alcoholic beverages."),
        ("supermarket", "Large retail store selling food and other goods."),
        ("pharmacy", "Store where medicinal drugs are dispensed."),
        ("hospital", "Institution providing medical treatment and care."),
        ("school", "Institution for educating children."),
        ("library", "Building containing a collection of books."),
        ("movie theater", "Place for watching films."),
        ("airport", "Facility for air travel."),
        ("train station", "Facility for railway transportation."),
        ("bus stop", "Designated place for boarding and alighting buses."),
        ("bank", "Financial institution."),
        ("post office", "Facility for sending and receiving mail."),
        ("police station", "Facility for law enforcement."),
        ("fire station", "Facility for firefighting."),
        ("museum", "Institution for preserving and exhibiting artifacts."),
        ("zoo", "Facility for exhibiting animals."),
        ("amusement park", "Venue for entertainment and attractions."),
        ("aquarium", "Facility for displaying aquatic animals and plants."),
        ("beach", "Shoreline area next to a body of water."),
        ("mountain", "Large landform rising above the surrounding land."),
        ("river", "Large natural flowing watercourse."),
        ("lake", "Large body of water surrounded by land."),
        ("ocean", "Vast body of saltwater."),
        ("forest", "Large area covered chiefly with trees."),
        ("desert", "Dry, barren area of land with little vegetation."),
        ("field", "Open land used for agriculture or sports."),
        ("gym", "Facility for physical exercise and fitness."),
        ("swimming pool", "Artificial facility for swimming."),
        ("playground", "Outdoor area for children to play."),
        ("parking lot", "Area for parking vehicles."),
        ("street", "Paved public thoroughfare."),
        ("sidewalk", "Paved footpath for pedestrians alongside a road."),
        ("traffic light", "Signal at intersections indicating when to stop and go."),
        ("stop sign", "Traffic sign indicating that drivers must stop."),
        ("crosswalk", "Marked pedestrian crossing on a road."),
        ("bridge", "Structure built to span a physical obstacle."),
        ("tunnel", "Underground passageway."),
        ("building", "Structure with a roof and walls."),
        ("house", "Building used as living space."),
        ("apartment", "Residential unit within a building."),
        ("skyscraper", "Tall building with multiple stories."),
        ("office building", "Building used for offices."),
        ("factory", "Building where goods are manufactured."),
        ("factory", "Building where goods are manufactured.")
    ]
    return random.choice(word_list) 
# Function to display the word with blanks for unrevealed letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word
 
# Function to play Hangman
def hangman():
    word_to_guess, hint = select_random_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0
 
    print("Welcome to Hangman!")
    print("Hint:", hint)
    print("Try to guess the word.")
    print(display_word(word_to_guess, guessed_letters))
 
    while attempts < max_attempts:
        guess = input("Enter the word or a letter: ").lower()
 
        if guess == word_to_guess:
            print("Congratulations! You guessed the word:", word_to_guess)
            break
 
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
 
        guessed_letters.append(guess)
 
        print(display_word(word_to_guess, guessed_letters))
 
        attempts += 1
        print("Incorrect guess! Attempts left:", max_attempts - attempts)
 
    if attempts == max_attempts:
        print("Sorry, you've run out of attempts. The word was:", word_to_guess)
 
if __name__ == "__main__":
    hangman()