# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

define t = Character("The TVs", callback=type_sound)
define f = Character("The Fish", callback=type_sound)
define d = Character("The Doors", callback=type_sound)

image subway = "images/Place1a.png"
image boringTV = "images/Place2a.png"
image wackyTV = "images/Place2b.png"
image tube1 = "images/Place3-1a.png"
image tube2 = "images/Place3-2a.png"
image tube3 = "images/Place3-3a.png"
image tunnel1 = "images/Place4-1a.png"
image tunnel2 = "images/Place4-2a.png"
image tunnel3 = "images/Place4-3a.png"
image fish = "images/Place5a.png"
image boringDoor1 = "images/Place6-1a.png"
image wackyDoor1 = "images/Place6-1b.png"
image boringDoor2 = "images/Place6-2a.png"
image wackyDoor2 = "images/Place6-2b.png"
image boringDoor3 = "images/Place6-3a.png"
image wackyDoor3 = "images/Place6-3b.png"
image boringInsideDoor = "images/Place7-1a.png"
image wackyInsideDoor = "images/Place7-1b.png"
image boringExit = "images/Place7-2a.png"
image wackyExit = "images/Place7-2b.png"
image boringRibbons = "images/Place7-3a.png"
image wackyRibbons = "images/Place7-3b.png"
image boring3doors = "images/Place8-1a.png"
image wacky3doors = "images/Place8-1b.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # use this to have background transitions:     
    # scene bg whitehouse
    # with Dissolve(.5)
    # pause .5
 
    # images directory to show it.
    scene expression "#000000" with dissolve
    pause 0.5
    scene subway with dissolve
    play music("general.mp3")

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    $ reject = 0

    # LOOP 1

    scene subway
    "The screech of subway brakes fades into the rustle of leaves. I step out. Cool air, green grass... The sky is so bright."

    scene boringTV
    t "look who it is! You made it! We have been waiting."
    t "feast upon our colors, soak in our light, spend as long as you would like!"
    menu:
        "The temptation is strong, what is beyond you?":
            $ reject += 1
        "Waiting? How do you know me?":
            $ reject += 2
        "I would like that, what is in the program?":
            $ reject += 0
    t "that does not matter, our glow is not eternal, so use it while you can."
    t "it may seem sad, but it’s ok, there is more to this place than just us."
    t "sitting in the same place too long can get boring. Can’t have that, can we?"
    menu:
        "I was bored since the start":
            $ reject += 2
        "That was fun, thank you!":
            $ reject += 0
        "Can’t argue with that, goodbye.":
            $ reject += 1

    scene tube1
    "Wow, it’s bleeding real, breathing petals into the soil. They smell like fresh rain and aromatics. The colors look so vivid."
    scene tube2
    pause 1.0
    scene tube3
    pause 1.0

    scene tunnel1
    "The smell of flowers vanishes. Just cold, echoing dark. It’s eerie."
    scene tunnel2
    pause 1.0
    scene tunnel3
    pause 1.0
    
    scene fish
    "Sunlight hits my eyes again. Oh it’s fish! It’s beautiful!"


    f "why are you looking at me so intently. Be normal or leave me alone. "
    f "you are supposed to be sad after what happened to the TVs, are you? Would be ironic since..."
    f "ah whatever. By the way, got any snacks?"
    menu:
        "Not right now, i can try to find you some!":
            $ reject += 0
        "What? no...":
            $ reject += 1
        "What are you even talking about?":
            $ reject += 2

    f "of course not, as expected."
    f "well, if you are going to be useless, might as well leave."
    f "more entertainment to be had beyond me, or whatever. Just go, i have nothing for you anymore."

    menu:
        "Useless? Who put you on the planet?":
            $ reject += 2
        "Alright alright, i get it, i’ll go":
            $ reject += 1
        "I’ll be back, with some food hopefully":
            $ reject += 0

    scene boringDoor1
    pause 1.0
    scene boringDoor2
    "A door, what is it doing here?"
    scene boringDoor3
    pause 1.0

    scene boringInsideDoor
    "Woah a whole hallway is inside... how?"
    
    scene boringExit
    "An exit, interesting."
    
    scene boringRibbons
    "Nevermind, these paths are looping under and on top of each other like ribbons."
    
    scene boring3doors
    "3 doors... it’s quiet here."

    d "I lead to digital sirens. I lead to repulsive dishes. I lead to cruel connections."
    d "Eternal satisfaction ahead. You are important yet not important. Craving for attention."
    d "Are you happy? Are you glad? Are you smiling?"
    menu:
        "I don’t think so":
            $ reject += 1
        "I have no reason not to":
            $ reject += 0
        "Only when it’s all over":
            $ reject += 2

    d "You must be tired. You are only getting started. You are pathetic."
    d "Stop thinking. Don’t you want to know? Keep visiting."
    d "I will give solace. I will give you paradise. I will give you qualm."

    menu:
        "I choose letting go":
            $ reject += 0
        "I choose bliss":
            $ reject += 2
        "I choose hesitance":
            $ reject += 1

   # LOOP 2
    scene expression "#000000" with dissolve
    pause 0.5
    scene subway with dissolve
    "The screech of subway brakes fades into the rustle of leaves. I step out. Cool air, green grass... The sky is so bright."

    scene wackyTV
    t "look who it is! You made it! We have been waiting long."
    t "feast upon our colors, soak in our radiance, spend as long as you would like!"
    menu:
        "The temptation is strong, what makes you different?":
            $ reject += 1
        "Waiting? Ah... are you...":
            $ reject += 2
        "I would like that, what is in the program?":
            $ reject += 0
    t "that does not matter, our glow is not eternal, so use us while you can."
    t "it may seem sad, but there is more to this place than just us."
    t "sitting in the same place too long can get boring. Can’t have that, can we?"
    menu:
        "As boring as a rerun":
            $ reject += 2
        "That was fun, thank you!":
            $ reject += 0
        "Goodbye":
            $ reject += 1

    scene tube1
    "It’s bleeding real, breathing petals into the soil. They smell like yesterday."
    scene tube2
    pause 1.0
    scene tube3
    pause 1.0
    
    scene tunnel1
    pause 1.0
    scene tunnel2
    "Yesterday? What does that even mean? It’s cold... and dark. What was i thinking about?"
    scene tunnel3
    pause 1.0
    
    scene fish
    "Sunlight hits my eyes again. It hurts. Oh it’s fish. I feel like throwing up."

    f "Stop right there! What are you looking at? You should leave... NO, stay i mean. "
    f "weep within yourself. how you must or the holy of synthetic, are you awoken to poetic from the husk of when this? unnatural for you how the loss are"
    f "So do you got some vacation food?"
    menu:
        "Not right now, i can try to find you some!":
            $ reject += 0
        "What? no...":
            $ reject += 1
        "What the hell is going on here?":
            $ reject += 2

    f "well, what did i... we... i? expect. Typical typical t...t...typical."
    f "practice rejection. I HATE YOU, no wait... i love you, but you are being too clingy, it’s killing me."
    f "can’t you take a DAMN hint, we just want what’s better for you. A better place is waiting for you. Begone, child."

    menu:
        "Useless, i got zero answers from you":
            $ reject += 2
        "I hate this song and dance":
            $ reject += 1
        "Seeya in the next one! with some food hopefully":
            $ reject += 0

    scene wackyDoor1
    pause 1.0
    scene wackyDoor2
    "A door, what is it doing here? And what was with those fish?"
    scene wackyDoor3
    pause 1.0
    
    scene wackyInsideDoor
    "A whole hallway is inside... why am i not surprised? This is not making any sense."
    
    scene wackyExit
    "An exit? What does that even mean?"
    
    scene wackyRibbons
    "Nevermind, these paths are looping under and on top of each other like my conciousness."
    
    scene wacky3doors
    "3 doors... i’m so certain i’ve been here before."


    d "I lead to seduction. I lead to PLEASE NO I DID NOT MEAN TO. I lead to slimy times."
    d "You love it don’t you? Your        is safe with me. Yummy yummers."
    d "Are you happy? Are you happy? Are you happy?"
    menu:
        "I don’t think so":
            $ reject += 1
        "I have no reason not to":
            $ reject += 0
        "Only when it’s all over":
            $ reject += 2

    d "Awww wittwe baby. Kill me. Grovel before your own chains."
    d "just crawl to me. Not just me actually. You will always come back."
    d "I will give solace. It’s the only way to attain paradise. I give you nothing, yet i will see you again."

    menu:
        "I choose letting go":
            $ reject += 0
        "I choose bliss":
            $ reject += 2
        "I choose hesitance":
            $ reject += 1


   # LOOP 3
    scene expression "#000000" with dissolve
    pause 0.5
    scene subway with dissolve
    "I screech as the subway’s brakes crash into the rustle of leaves. I step out. Humid air, green grass... The sky is too bright."

    scene wackyTV
    t "finally here. Our stimulants have been waiting."
    t "Eat our illuminating distractions. spend forever with us!"
    menu:
        "I can’t stop myself from watching, please let me go":
            $ reject += 1
        "Get out of my head!":
            $ reject += 2
        "I would like that, what is in the program?":
            $ reject += 0
    t "that does not matter, please keep watching, we are dying."
    t "oh god we are dying, why? You want more? Fine go right ahead."
    t "YOU Y...y... s... ssitting in the same place too long can get boring. Can’t have that, can we?"
    menu:
        "Get me out of here":
            $ reject += 2
        "That was fun, fun, fun fun fun fun funfunfunfunfun":
            $ reject += 0
        "Yeah, whatever, goodbye.":
            $ reject += 1

    scene tube1
    "Why is it so real? Why does it not make sense to me? What even is anything?"
    scene tube2
    pause 1.0
    scene tube3
    pause 1.0
    
    scene tunnel1
    "The smell of flowers vanishes. Just cold... so cold..."
    scene tunnel2
    "???" "WoNmtHNTFfXpHznWNPdic"
    scene tunnel3
    pause 1.0
    
    scene fish
    "Sunlight hits my eyes again. Oh it’s fish! It looks delicious! huh?"

    f "STOP! What are you looking at? You should leave... NO, You should leave. "
    f "How you must weep for the loss of the holy from within the husk of synthetic, how poetic when you are unnatural yourself. Or are you awoken to this?"
    f "We are hungry, feed us."
    menu:
        "I want to fatten you up. Too bad i have no food on me":
            $ reject += 0
        "No":
            $ reject += 1
        "What am i? How do i get out of here?":
            $ reject += 2

    f "HAHAHAHAHahahahah..... I knew it."
    f "they did not make me engaging enough... it is not my fault."
    f "go to the door behind me, they should be better at this than me."

    menu:
        "The three doors? But it restarts...":
            $ reject += 2
        "I’ll go i guess":
            $ reject += 1
        "I’ll be back, with some food, i won’t forget this time":
            $ reject += 0

    scene wackyDoor1
    pause 1.0
    scene wackyDoor2
    "Here is the door, the weird impossible door"
    scene wackyDoor3
    pause 1.0
    
    scene wackyInsideDoor
    "And the nonsensical hallway..."
    
    scene wackyExit
    "The fake exit"
    
    scene wackyRibbons
    "The twisting paths"
    "..."


    scene wacky3doors
    d "You like cowboys? You should be able to do it by now. It’s too bad there are no grills around here."
    d "There’s also magical girls. Just keep AAAAAAA. Maybe on the next one, ay?"
    d "drooling yet? Do you enjoy when it hurts? Smile for me."
    menu:
        "I don’t think so":
            $ reject += 1
        "I have no reason not to":
            $ reject += 0
        "Only when i’m dead":
            $ reject += 2

    d "Don’t you worry. Don’t you worry. Don’t you worry."
    d "they won’t dim anymore. I forgive you. The push and pull is forever."
    d "Just let go. So go and pierce the heavens. Or maybe it isn’t."

    menu:
        "I choose letting go":
            $ reject += 0
        "I choose bliss":
            $ reject += 2
        "I choose hesitance":
            $ reject += 1



    # Logic to determine ending
    if reject >= 26:
        jump ending_rejection
    else:
        jump ending_acceptance

label ending_rejection:
    stop music fadeout 2.0
    play music("bad.mp3")
    scene expression "#000000" with dissolve
    "Huh? It’s so dark."
    "It's getting cold. I can't feel my hands. I can't feel my breath. "
    "???" "Voltage is dropping on petri dish four. Increase the electrical pulses, it needs more stimulus or the tissue is going to die."
    "???" "I already turned up the light and the current. It’s not responding anymore. The neural spikes are completely flatlining."
    "???" "Dammit, we just need to keep it alive long enough to finish the reading. Check the main wire, is it loose?"
    "???" "Wait... look at the monitor. Every time we speak, the cells are firing."
    "???" "What? That's impossible, there's no electrical input running right now."
    "???" "Look! I'm talking, and the waveform is mimicking the sound waves. It's not the electricity... Doctor, it's listening to us. It can hear you."
    "???" "It's... processing acoustic vibrations? Oh my god. It's aware."
    "???" "It’s dropping too fast. The cells are rupturing from the lack of input. It's dying."
    "???" "Say something! Keep talking to it! Maybe it-"
    return


label ending_acceptance:

    # LOOP 4
    scene expression "#000000" with dissolve
    pause 0.5
    scene subway with dissolve
    "The screech of subway brakes fades into the rustle of leaves. I step out. Cool air, green grass... The sky is calm now."

    scene boringTV
    t "You returned. You really like us, don't you? There is no reason to look away anymore."

    menu:
        "I want to stay here with you forever.":
            jump ending_t_stay
        "What if I smash your screens?":
            jump ending_t_break
        "Move on":
            pass

    scene tube1
    "I walk past the pulsing monitors toward the giant paint tube."
    scene tube2
    "The vibrant explosion of flowers is still there, but right at the mouth of the tube, a single four-leaf clover stands completely still, catching the light."

    menu:
        "Pluck the clover and rest here in the grass for the rest of my life.":
            jump ending_clover_stay
        "Leave the clover behind and enter the dark hallway.":
            pass

    scene tube3
    pause 1.0
    scene tunnel1
    pause 0.75
    scene tunnel2
    pause 0.75
    scene tunnel3
    "The cold, echoing dark passes quickly. The exit feels closer this time."
    
    scene fish
    "Sunlight hits my eyes again. The water is clear. The fish is waiting."

    f "Ah. Back again. And you still don't have any snacks, do you? Why are you even here?"

    menu:
        "I'll stay here with you. We don't need food, just company.":
            jump ending_f_stay
        "I'm going to pull you out of your tank and see what happens.":
            jump ending_f_break
        "Move on":
            pass

    scene boringDoor1
    pause 1.0
    scene boringDoor2
    pause 1.0
    scene boringDoor3
    pause 1.0
    scene boringInsideDoor
    "I step through the standalone door. The impossible hallway stretches out, but it feels shorter."
    
    scene boringExit
    pause 1.0
    scene boringRibbons
    "The twisting paths ribbon under my feet, leading me back to the quiet clearing."

    scene boring3doors
    d "The final destination. The cycle is whole. We are waiting for your final signature."

    menu:
        "Open the doors wide and settle into the quiet space between them.":
            jump ending_d_stay
        "Rip the doors off their hinges":
            jump ending_d_break
        "Step through one of the doors to move on.":
            jump ending_infinite_loop


# ACCEPTANCE SUB-ENDINGS

# --- TVs Endings ---
label ending_t_stay:
    "I sit down directly in front of the monitors, bathing in the warmth of their static hum."
    t "A wonderful choice. Lean back. Let the colors fill your vision. We will never go dim now."
    "My eyes grow heavy. The glow is beautiful. I am home."
    return

label ending_t_break:
    stop music fadeout 2.0
    play music("bad.mp3")
    scene expression "#000000" with dissolve
    "I lunged forward, smashing my hands directly through the glass screens."
    t "ERROR. STIMULUS CORRUPTED. WHY WOULD YOU—"
    "The monitors burst into violent sparks. The sky fractures like shattered porcelain."
    "Everything locks up. The world is broken. I am frozen in a static nightmare."
    return

# --- Clover Ending ---
label ending_clover_stay:
    "I lie down in the cool grass, carefully cradling the small clover in my hands."
    "The scent of fresh rain and aromatics washes over me completely. The world stops moving."
    "No more hallways. No more loops. Just the quiet, eternal wonder of a single leaf."
    return

# --- Fish Endings ---
label ending_f_stay:
    "I sit down on the grass facing the tank, watching the beautiful scales catch the surreal sunlight."
    f "Well... I guess floating around isn't so bad when there's someone here to watch. Don't worry about the snacks. This is fine."
    "We drift together, completely at peace with this world."
    return

label ending_f_break:
    stop music fadeout 2.0
    play music("bad.mp3")
    scene expression "#000000" with dissolve
    "I reach out and grab the fish, squeezing tight and throwing it against the ground."
    f "SYSTEM FAILURE. LOGIC COLLAPSE. YOU UTTERLY—"
    "The fish vanishes into nothing. The sky turns the color of blood. The air becomes unbreathable as the world unravels."
    "There is nothing left to explore."
    return

# --- Doors Endings ---
label ending_d_stay:
    "I sit down in the center of the three doors, embracing the deep, holy silence of the room."
    d "Solace achieved. Paradise unlocked. The thoughts of the mind are finally quiet."
    "The doors close softly around me, shielding me from the loops forever. I am content."
    return

label ending_d_break:
    stop music fadeout 2.0
    play music("bad.mp3")
    scene expression "#000000" with dissolve
    "I grab the frames of the doors and slam them against each other, shattering the wood into splinters."
    d "CRITICAL THRESHOLD REACHED. REJECTION APPLIED COARSELY. TERMINATING."
    "The sacred clearing implodes. The room collapses in on itself, crushing my consciousness into a single, corrupted point of absolute nothingness."
    return

# --- The Infinite Loop Ending ---
label ending_infinite_loop:
    "I choose a door. I step through, expecting something new."
    scene expression "#000000" with dissolve
    "But the darkness is instantly familiar."
    "A heavy pneumatic hiss echoes in the dark."
    "The cycle repeats."
    jump start