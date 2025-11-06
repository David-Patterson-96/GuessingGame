# Create the word list and import the random function
import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# Fact Dictionary
thisdict = {
    # Pearson Word Fact
    "pearson": ("Between April 1897 to December 1897, Pearson's Magazine published the story of the H.G. Wells' classic sci-fi novel 'The War of the Worlds' "
                "\nwhere each month a few chapters of the story would be release similar to a comic book or TV show."
                "\nUntil the chapters where collected and edited together as novel in 1898."),
    # Tripod Word Fact
    "tripod": ("The Martian Fighting Machine tripods are the main frontline trooper of the Martian invasion force "
                "\nthe H.G. Wells' classic sci-fi novel 'The War of the Worlds.' Plotted by one Martian inside and armed with all kinds of deadly weapon, "
                "\nthese metal monsters harvest humans and wipe out any human resistance forces that stand in their way." 
                "\nNot only are the tripods are the most iconic thing from "'The War of the Worlds'" but all of science fiction."
                "\nInspiring many sci-fi gaint robots, mechs, and mechas like the famous AT-AT walkers from Star Wars and so on."),
    # Martian Word Fact
    "martian": ("The Martians are a race of bear sized octopus-like creatures that invade the Earth "
                "\nin the H.G. Wells' classic sci-fi novel 'The War of the Worlds.' The Martians are not just monsters, H.G. Wells based his aliens on "
                "\nCharles Darwin's popular Theory of Evolution and put in loads of scientific details in their design." 
                "\nSuch as the Martians only feeding on human blood due a lack of digestive system organs like stomachs and so on. "
                "\nIt is even speculated that the octopus design of Wells' Martians is a social commentary of the British Empire's imperialism, "
                "\nwhich is often depicted as an octopus in many political cartoons of the time"),
    # Mars Word Fact
    "mars": ("The fourth planet in the Solar (Sol) System, Mars was the planet the alien invaders come from in the "
                "\nH.G. Wells' classic sci-fi novel 'The War of the Worlds.'" 
                "\nSince ancient times, humanity has been having this red planet on the mind with naming it after the Roman God of War, "
                "\nthinking if there is life on the planet, and seeing it as the Earth's twin." 
                "\nWhile there are now robots exploring the lifeless rock, many still hope that life on the red planet exist "
                "\nor that humans colonize Mars in the future."
                "\nHowever the popluar days of evil aliens from Mars invading and take over Earth of popular 20th century sci-fi are a relic of the past."),
    # Heat-Ray Word Fact
    "heatray": ("The Heat-Ray is one ot the two main weapon the Martians use to invade Earth in the H.G. Wells' classic sci-fi novel "
                "\n'The War of the Worlds.' The weapon shoots an invisible ray of heat that turns anything that the ray touches to burst into flame. "
                "\nWhile a product of 19th century science fiction, however today Wells' Heat-Ray shares a lot in common with the"
                "\nmodern carbon dioxide (CO2) laser, a device that uses gases to discharge an invisible ray of heat that burn targets into flames."),
    # Black Smoke Word Fact
    "blacksmoke": ("The Black Smoke is one ot the two main weapon the Martians use to invade Earth in the H.G. Wells' classic sci-fi novel "
                "\n'The War of the Worlds. A chemical weapon which, after the canister that contains the toxic gas hits the ground, "
                "\nreleases a huge cumulus black cloud that sinks and slowly spreads over the ground in a liquid-like matter, killing any who inhales it instantly." 
                "\nH.G. Wells wasn't too far off with the idea of the Black Smoke weapon as chemical warfare and toxic gas weapons "
                "\nsuch as Tear gas would become reaitly during the offset of World War 1 in 1914, only 16 years after 'The War of the Worlds' was publuished."),
    # Cylinder Word Fact
    "cylinder": ("The cylinders are spaceships that the Martians use the travel to Earth after being fired from "
                "\na massive gun from a deep pit on the planet Mars in the H.G. Wells' classic sci-fi novel 'The War of the Worlds.'"
                "\nThese massive spaceships, which have a diameter of about thirty yards, come to Earth under the guise of green falling stars before landing. "
                "\nare able to house materials to build five Martian Fighting Machine tripods and other tools to help in their invasion of Earth. "
                "\nWhile this method of space travel seems impractical now. However, in the 19th and early 20th century, it was commonly believed that "
                "\nspace travel was achieved by shooting people in massive hollow bullets from a gaint gun called space gun or Verne gun. "
                "\nBut thanks to the advent of Robert H. Goddard's invention of liquid rocket fuel and the multi-stage rocket in 1914, "
                "\nthis idea of space travel is now a novelty of early sci-fi."),
    # London Word Fact
    "london": ("London, England was the capital city of the British Empire durring its height "
                "\n and still remains as the captial of both England and the United Kingdom."
                "\nIn the H.G. Wells' classic sci-fi novel 'The War of the Worlds', the Martain invade in small towns in the Surrey countryside like Woking, "
                "\nlocated 25 miles away from London, before pushing towards London, weakening the British Empire's forces."
                "\n Defeating the British Army in just three days."
                "\nLondon then after humanity's defeat becomes the main base of the Martian"
                "\n before the city becomes their mass grave as the Martains are defeated by Earth's microscopic bacteria."
                "\nNot only that but London will also be where William Heinemann would publish H.G. Wells' 'The War of the Worlds' as a novel in 1898."),
    # Crystal Egg Word Fact
    "crystalegg": ("Written in 1987, 'The Crystal Egg' is a short story written by H.G. Wells about a poor, depressed antique shop owner in London, England "
                "\nwho comes in ownership of a strange alien device that allows him to see life on Mars and the Martians to watch him."
                "\nWhile many claim 'The Crystal Egg' short story is a perquel to the H.G. Wells' classic sci-fi novel 'The War of the Worlds', "
                "\ndue the Martians and their machines have the same design and characterizations between the two stories."
                "\nHowever there are no clear foreshadowing nor direct tie-ins to either events in both stories."),
    # Robert H. Goddard Word Fact
    "goddard": ("Inspired by the H.G. Wells' classic sci-fi novel 'The War of the Worlds' at the age of 17 years old, a young American named "
                "\nRobert H. Goddard would begin his dream of seeing humanity leaving Earth and taking to stars." 
                "\nFrom that moment forward, Robert H. Goddard would invent liquid rocket fuel and the multi-stage rocket both in 1914."
                "\nGoddard's archievements would lead to great advances in space exploration such as the famous Apollo 11 moon landing of 1969."
                "\nIn 1959, the National Aeronautics and Space Administration (NASA) would name their first space flight center after Robert H. Goddard, "
                "\nGoddard Space Flight Center located in Greenbelt, Maryland."),
    # H.G. Wells Word Fact
    "hgwells": ("Originally a science teacher, Herbert George Wells would become one of the famous writers of the 20th century and "
                "\nhe along with Jules Verne are often called 'The Fathers of of Science Fiction.'"  
                "\nMany of H.G. Wells' famous titles being the likes of 'The War of the Worlds', 'The Time Machine', 'The Invisible Man', "
                "\n'The Island of Doctor Moreau', and 'The First Men in the Moon.'"
                "\nThese sci-fi novels were not just pure entertainment as H.G. Wells often put in social commentary such as 'The War of the Worlds' being "
                "\na criticism of the British Empire's imperialism and humanity vs nature told in a "'what goes around comes around'" matter. "
                "\nHowever H.G. Wells not only wrote science fiction, as the man wrote many science and political essays and books "
                "\nwith his first ever published work being 'Textbook of Biology' in 1893."),
    # Orson Welles Word Fact
    "orson": ("On October 30, 1938, actor and director Orson Welles along with CBS Radio's The Mercury Theatre on the Air played "
                "\na live radio drama of the H.G. Wells' classic sci-fi novel 'The War of the Worlds."
                "\nUnlike most radio dramas of the time, the Mercury Theatre play the drama in the form of live news reports "
                "\ncausing mass panic among radio listeners who miss the opening warning that state the show was purely fictional."
                "\nAfter the initial public outcry, there were a few remakes of the 1938 'War of the Worlds' boardcast arcoss the world in the following years"
                "\nsuch as the 1968 WKBW 'War of the Worlds' radio boardcast."
                "\nAs for Orson Welles, he found a career in filmmaking after his 'War of the Worlds' boardcast as an actor and director "
                "\n with works ranging from 1941's 'Citizen Kane' to 1986's 'The Transformers: The Movie.'")
}

# main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('Tripod Assault')
    root.config(bg="#E7FFFF")
    count = 0
    win_count = 0

    # choosing word
    index = random.randint(0, 10)
    file = open("words", "r")
    l = file.readlines()
    selected_word = l[index].strip('\n')

    # creation of word dashes variables
    x = 250
    for i in range(0, len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={}, y={})'.format(i, x, 500))

    # letter icons
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
          "x", "y", "z"]
    for letter in alphabet:
        exec('{}=PhotoImage(file="{}.png")'.format(letter, letter))

    # Martian Tripod images
    h123 = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
    for tripod in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(tripod, tripod))

    # letters placement
    button = [['b1', 'a', 0, 595], ['b2', 'b', 70, 595], ['b3', 'c', 140, 595], ['b4', 'd', 210, 595],
              ['b5', 'e', 280, 595], ['b6', 'f', 350, 595], ['b7', 'g', 420, 595], ['b8', 'h', 490, 595],
              ['b9', 'i', 560, 595], ['b10', 'j', 630, 595], ['b11', 'k', 700, 595], ['b12', 'l', 770, 595],
              ['b13', 'm', 840, 595], ['b14', 'n', 0, 645], ['b15', 'o', 70, 645], ['b16', 'p', 140, 645],
              ['b17', 'q', 210, 645], ['b18', 'r', 280, 645], ['b19', 's', 350, 645], ['b20', 't', 420, 645],
              ['b21', 'u', 490, 645], ['b22', 'v', 560, 645], ['b23', 'w', 630, 645], ['b24', 'x', 700, 645],
              ['b25', 'y', 770, 645], ['b26', 'z', 840, 645]]

    for q1 in button:
        exec(
            '{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

    # hangman placement
    han = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7']]
    for p1 in han:
        exec('{}=Label(root, bg="#E7FFFF", image={})'.format(p1[0], p1[1]))

    # placement of first hangman image
    c1.place(x=300, y=-10)

    # exit button
    def close():
        global run
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()

    e1 = PhotoImage(file='exit.png')
    ex = Button(root, bd=0, command=close, bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=e1)
    ex.place(x=770, y=10)
    s2 = 'SCORE:' + str(score)
    s1 = Label(root, text=s2, bg="#E7FFFF", font=("arial", 25))
    s1.place(x=10, y=10)

    # button press check function
    def check(letter, button):
        global count, win_count, run, score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0, len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i, letter.upper()))
                    root.update()
                    # Adding points to the player's score
            if win_count == len(selected_word):
                score += 100

                # Word Fact window object
                if selected_word in thisdict:
                    fact_window = Toplevel()
                    fact_window.title("Fun Fact")
                    fact_window.geometry("1388x300")
                    fact_label = Label(fact_window,
                                       text=thisdict[selected_word],
                                       font=("Helvetica", 20, "underline", "bold"))
                    fact_label.place(x=20, y=-5)
                    fact_window.configure(bg='#E7FFFF')

                fact_window.update()

                # Display winning game message
                answer = messagebox.askyesno('GAME OVER', 'YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        # Count player's remaining tries and display proper Martian Tripod image
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count +1,300,-10))
            root.update()
            # Display lost game message and reset player's score to 0
            if count == 6:
                answer = messagebox.askyesno('GAME OVER', 'YOU LOST! THE WORD WAS: ' + selected_word.upper() + ' \nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()

    root.mainloop()
