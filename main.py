import turtle # Importér turtle-grafikmodulet
import time # Importér time-modulet til forsinkelser
import random # Importér random-modulet til tilfældige tal

delay = 0.1 # Sæt forsinkelsen for spillets hastighed

# Score
score = 0 # Initialiser scoren
high_score = 0 # Initialiser højeste score

# Opsætning af skærmen
wn = turtle.Screen() # Opret et skærmobjekt
wn.title("Snake") # Sæt vinduets titel
wn.bgcolor("green") # Sæt baggrundsfarven til grøn
wn.setup(width=600, height=600) # Sæt vinduets dimensioner
wn.tracer(0) # Slå skærmopdateringer fra for glattere animation

# Slangehoved
head = turtle.Turtle() # Opret et turtle-objekt til slangens hoved
head.speed(0) # Sæt turtle-hastigheden til maksimal (ingen animationsforsinkelse)
head.shape("square") # Sæt turtle-formen til en firkant
head.color("black") # Sæt turtle-farven til sort
head.penup() # Deaktiver tegning, når turtle bevæger sig
head.goto(0,0) # Flyt turtle til midten af skærmen
head.direction = "stop" # Initialiser hovedets retning til stop

# Slangemad
food = turtle.Turtle() # Opret et turtle-objekt til maden
food.speed(0) # Sæt turtle-hastigheden til maksimal (ingen animationsforsinkelse)
food.shape("circle") # Sæt turtle-formen til en cirkel
food.color("red") # Sæt turtle-farven til rød
food.penup() # Deaktiver tegning, når turtle bevæger sig
food.goto(0,100) # Flyt maden til en startposition

segments = [] # Initialiser en tom liste til slangens kropssegmenter

# Pen
pen = turtle.Turtle() # Opret et turtle-objekt til at skrive scoren
pen.speed(0) # Sæt turtle-hastigheden til maksimal (ingen animationsforsinkelse)
pen.shape("square") # Sæt turtle-formen til en firkant (ikke synlig)
pen.color("white") # Sæt turtle-farven til hvid
pen.penup() # Deaktiver tegning, når turtle bevæger sig
pen.hideturtle() # Skjul turtle-ikonet
pen.goto(0, 260) # Flyt pennen til toppen af skærmen
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")) # Skriv den initiale score

# Funktioner
def go_up(): # Funktion til at sætte hovedets retning til op
    if head.direction != "down": # Forhindre slangen i at gå i modsat retning
        head.direction = "up" # Sæt retningen til op

def go_down(): # Funktion til at sætte hovedets retning til ned
    if head.direction != "up": # Forhindre slangen i at gå i modsat retning
        head.direction = "down" # Sæt retningen til ned

def go_left(): # Funktion til at sætte hovedets retning til venstre
    if head.direction != "right": # Forhindre slangen i at gå i modsat retning
        head.direction = "left" # Sæt retningen til venstre

def go_right(): # Funktion til at sætte hovedets retning til højre
    if head.direction != "left": # Forhindre slangen i at gå i modsat retning
        head.direction = "right" # Sæt retningen til højre

def move(): # Funktion til at bevæge slangens hoved i den nuværende retning
    if head.direction == "up": # Hvis retningen er op
        y = head.ycor() # Hent den nuværende y-koordinat
        head.sety(y + 20) # Flyt hovedet op med 20 enheder

    if head.direction == "down": # Hvis retningen er ned
        y = head.ycor() # Hent den nuværende y-koordinat
        head.sety(y - 20) # Flyt hovedet ned med 20 enheder

    if head.direction == "left": # Hvis retningen er venstre
        x = head.xcor() # Hent den nuværende x-koordinat
        head.setx(x - 20) # Flyt hovedet til venstre med 20 enheder

    if head.direction == "right": # Hvis retningen er højre
        x = head.xcor() # Hent den nuværende x-koordinat
        head.setx(x + 20) # Flyt hovedet til højre med 20 enheder

# Tastaturbindinger
wn.listen() # Lyt efter tastaturinput
wn.onkeypress(go_up, "w") # Kald funktionen go_up, når "w"-tasten trykkes
wn.onkeypress(go_down, "s") # Kald funktionen go_down, når "s"-tasten trykkes
wn.onkeypress(go_left, "a") # Kald funktionen go_left, når "a"-tasten trykkes
wn.onkeypress(go_right, "d") # Kald funktionen go_right, når "d"-tasten trykkes

# Hovedspilsløkke
while True: # Uendelig løkke til spillet
    wn.update() # Opdater skærmen

    # Tjek for en kollision med grænsen
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290: # Hvis hovedet rammer grænsen
        time.sleep(1) # Pause i 1 sekund
        head.goto(0,0) # Flyt hovedet til midten
        head.direction = "stop" # Stop hovedets bevægelse

        # Skjul segmenterne
        for segment in segments: # For hvert segment i kroppen
            segment.goto(1000, 1000) # Flyt det ud af skærmen
        
        # Ryd segmentlisten
        segments.clear() # Fjern alle segmenter fra listen

        # Nulstil scoren
        score = 0 # Nulstil scoren til 0

        # Nulstil forsinkelsen
        delay = 0.1 # Nulstil spillets hastighed

        pen.clear() # Ryd den tidligere score
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Skriv den opdaterede score

    # Tjek for en kollision med maden
    if head.distance(food) < 20: # Hvis afstanden mellem hovedet og maden er mindre end 20 enheder
        # Flyt maden til et tilfældigt sted
        x = random.randint(-290, 290) # Generér en tilfældig x-koordinat
        y = random.randint(-290, 290) # Generér en tilfældig y-koordinat
        food.goto(x,y) # Flyt maden til den tilfældige position

        # Tilføj et segment
        new_segment = turtle.Turtle() # Opret et nyt turtle-objekt til det nye segment
        new_segment.speed(0) # Sæt turtle-hastigheden til maksimal (ingen animationsforsinkelse)
        new_segment.shape("square") # Sæt turtle-formen til en firkant
        new_segment.color("grey") # Sæt turtle-farven til grå
        new_segment.penup() # Deaktiver tegning, når turtle bevæger sig
        segments.append(new_segment) # Tilføj det nye segment til segmentlisten

        # Forkort forsinkelsen
        delay -= 0.001 # Øg spillets hastighed

        # Øg scoren
        score += 10 # Øg scoren med 10 point

        if score > high_score: # Hvis den nuværende score er højere end højeste score
            high_score = score # Opdater højeste score
        
        pen.clear() # Ryd den tidligere score
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Skriv den opdaterede score

    # Flyt de bagerste segmenter først i omvendt rækkefølge
    for index in range(len(segments)-1, 0, -1): # Gennemgå segmenterne i omvendt rækkefølge
        x = segments[index-1].xcor() # Hent x-koordinaten for det forrige segment
        y = segments[index-1].ycor() # Hent y-koordinaten for det forrige segment
        segments[index].goto(x, y) # Flyt det nuværende segment til positionen for det forrige segment

        # Flyt segment 0 til hvor hovedet er
    if len(segments) > 0: # Hvis der er segmenter i listen
        x = head.xcor() # Hent hovedets x-koordinat
        y = head.ycor() # Hent hovedets y-koordinat
        segments[0].goto(x,y) # Flyt det første segment til hovedets position

    move() # Kald move-funktionen for at bevæge hovedet

    # Tjek for kollision mellem hovedet og kropssegmenterne
    for segment in segments: # For hvert segment i kroppen
        if segment.distance(head) < 20: # Hvis afstanden mellem hovedet og segmentet er mindre end 20 enheder
            time.sleep(1) # Pause i 1 sekund
            head.goto(0,0) # Flyt hovedet til midten
            head.direction = "stop" # Stop hovedets bevægelse
        
            # Skjul segmenterne
            for segment in segments: # For hvert segment i kroppen
                segment.goto(1000, 1000) # Flyt det ud af skærmen
        
            # Ryd segmentlisten
            segments.clear() # Fjern alle segmenter fra listen

            # Nulstil scoren
            score = 0 # Nulstil scoren til 0

            # Nulstil forsinkelsen
            delay = 0.1 # Nulstil spillets hastighed
        
            # Opdater scorevisningen
            pen.clear() # Ryd den tidligere score
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Skriv den opdaterede score

    time.sleep(delay) # Vent i den angivne forsinkelsestid

wn.mainloop() # Hold vinduet åbent

