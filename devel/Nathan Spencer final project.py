def endGame(go):
    print('You Loose, ' + go)
    
while True:
    print("The sound of the fierce wind wakes you up from your disgruntled state. \nYou try and remember, \"what was it you were doing?\" \nIt's so hard to think with this throbbing pain in your head... Wait. \nThe pain. \nThose men. \nThey said they were after something of yours. But what was it? \nIt's so hard to think but you remember that it's important. \nYou remember they jumped you, took you to the outskirts of the CITY, \nand hoped to leave you for dead. You can see the CITY from here, \nit's not too far to WALK. \nBut there's a huge strange cloud rolling over the horizon. \nAnd it's fast. You think maybe it'd be better to RUN to the CITY. \nThe wind picks up. You need to make a choice.")
    print("\n")
    print("Do you RUN to the CITY or WALK to the CITY?")
    user = input()
    if user == "run":
        print("Something doesn't seem right. You remember this kind of cloud from before, not \njust here but other places too. You dart in a full sprint towards the CITY. The wind is picking up, you don't have much time. You can hear alarms from the CITY shouting at full blast, \"SANDSTORM APPROACHING, PLEASE STAY INDOORS.\" You make \nit to the CITY on time and head into the nearest open door, which closes fast \nbehind you. You take a big sigh as you can already hear the effects of the \nsandstorm through the door. You're safe, for now.")
    if user == "walk":
        print("You start walking towards the CITY. The wind constantly at your back. The wind picks up. stronger. STRONGER. After some time walking the wind finally concerns you enough for you to look behind. \"SANDSTORM\", you yell as a wall of sand, rock, and gravel hit your human form.")
        print("A couple hours later a search and rescue drone is scanning the desert dunes for survivors. \"no life signs detected.\" it chimes as it heads back towards the city.")
        endGame('Game Over')
        continue
    print("\n")
    print("After taking a few breaths you begin to look around the establishment you've \njust entered. It looks to be a BAR. Eyes from suspicious looking men pierce you \nlike daggers as you begin to walk through the BAR for a drink. A tough looking \nman with an eyepatch is the bartender. As you approach the bartender asks, \"what'll ya have?\" Before you can even answer a loud voice comes from behind you.\"ROY! There you are buddy I've been worried about sick about you, where've you been?\" The man looks familiar to you but you aren't sure who he is. \"Boy that hit to \nthe head must've been nasty. Don't tell me you've forgotten your old pal LEX?\" \nJust then another patron of the bar stands out of his seat. \"Wait, Roy? It's me, BEN. Don't beleive a word this guy says he's been lyin' to you ever since you \nwere tiny. You don't really remember this person at all, but what if he's right? You give this \"BEN\" a look over. He's wearing a bright red jacket with a name \non it, and has something holstered at his hip.")
    print("\"ROY you ain't buying this guy's story are you?\" \"Don't listen to this guy ROY, listen to your old pal BEN\". You don't know who to believe. You need to make a \nchoice.")
    print("\n")
    print("Will you choose LEX or BEN?")
    user = input()
    if user == "lex":
        print("You stand by LEX as a sign of who you've choosen. Just then the man named BEN unholsters his pistol. \"All you had to do was listen to me and everything would've been fine.\" The man named BEN says as he points his pistol at you. But before \nyou can blink, BANG! LEX blasts a round into Ben before he can react.")
    if user == "ben":
        print("You stand by BEN as a sign of your choice. \"NO ROY WAIT!\" The man named LEX \nyells. Just then you hear a click. \"I knew you'd made the right choice.\" The man named BEN tells you. Everything turns black as the last thing you hear is the \nsound of a gunshot.")
        endGame('Game Over')
        continue
    print("\n")
    print(" \"That was a close one.\"Says Lex as he grabs the new dead man's pistol and a \npair of keys from his pocket. \"That guy was part of the same group that tried to kill you. I saw what happened but I left before it got ugly and I was going to help, but uh you know how it is, I gotta whatch out for myself. Anyway you're \ngoing to need wheels if you want to get to thier hideout to get your stuff back.\"Pointing to the keys taken from the gang member in his hand,\"And I have just \nthe ride.\"")
    print("\n")
    print("Out in the parking lot is a brand new mortorcycle. Bright red with the logo of \nthe gang on the side.\"Wow would you look at this guy's bike!\"LEX remarks.\"You \nshould be able to reach the HIDEOUT at the inner city, farthest away from \nsandstorm damage.\"You get on the bike and rev the engine, you know this feeling, you like this feeling. \"You're going to need this.\" LEX says as he hands you \nthe gang member's pistol.")
    print("\n")
    print("Speeding down the highway gives you an exhilarating feeling. You're going to \nmake this gang pay for messing with you. But just before you hit top speed a \nbright light shines on you. \"THIS IS THE POLICE. YOUR VEHICLE HAS BEEN SEEN IN \nRELATION WITH A KNOWN GNAG, PULL OVER NOW AND SURRENDER!\" Balres from a police \nhelicopter. You have to escape them if you want to get to the hideout, after all bringing the cops to the hideout would scare the gang off. But you're not to \nsure about shooting at the police in a city you don't understand. You have to \nmake a choice.")
    print("\n")
    print("Do you SHOOT at the police or try and ESCAPE the police?")
    user = input()
    if user == "escape":
        print("You respond to the helicopters following you with a loud rev of the new \nmotorcycle. You zoom out of the spotlight as the helicopters try and find you. \nEventually they do find you again but you're not making it easy. You realize \nthat you won't escape them on the highway, it's too open. Zooming past cars you \nhead for the wall of the highway and pull up on the handlebars as hard as you \ncan to pop the front tire up. You bounce off the highway and go into a quite \nlarge fall, maybe this wasn't such a good idea. The new bike makes some chirps \nand beeps. \"AUTOMATIC HOVER ACTIVATED.\" The bike chimes as the wheels shift from being vertical to horizontal as you start to glide towards the ground. Landing softly you zoom into a nearby alley and quickly turn off your engine. You \nhear sirens but after a while they become distant and faint. You turn your \nmotorcycle back on and head back towards the gang HIDEOUT.")
    if user == "shoot":
        print("Driving down the highway, you just can't seem to lose them with the spotlights \nall around you. You decide enough is enough and pull out your pistol. You fire a well placed shot into the light of one of the hilicopters and the spotlight \ngoes dark. After a moment of feeling proud four more spotlights shine on you as a police radio on your motercycle starts to become active.\"I repeat, suspect has a weapon. Lethal force authorized.\" Shortly after several helicopters open up a volly of machine gun fire onto the road. you can only hear the richochet of \nbullets before a stray hits your motorcyle's fuel tank, ending your joy ride.")
        endGame('Game Over')
        continue
    print("\n")
    print("You finally arrive at the HIDEOUT of your assailants. Parked in an alley with a \ngood vantage point you begin to scope out the HIDEOUT. Two guards stand at the \nfront gate. In several windows you can see guards on lookout for anything coming from afar. After your last run with the police you're mad. You don't want to \njust get these guys, you want to send a message. You're going to go in guns \nblazing, but in what way that won't make you end up dead? Obviously there's the front gate, which is a safe bet to get inside, but you scan for another option... The roof. Two guards are stationed on the roof. You could easily get your \nmotorcycle on a roof and jump off and try to glide over. But it'll be risky. You need to make a choice.") 
    print("\n")
    print("Do you DRIVE through the front, or JUMP off the roof of the nearest building?")
    user = input()
    if user == "jump":
        print("The CITY skyline shines behind you. Searchlights moving back and fourth, \nglistening neon lights flash, police helicopters fly above the skyscrapers. It's silent. This is it. You start your motorcycle and rev it hard as you zoom to \nthe edge of the building. Activating hover mode you jet off the side of the \nbuilding and start to slowly descend. Seeing the motorcycle rushing off a \nbuilding, the guards on top of the roof are startled, then pull their weapons \nand shoot at you. But you knew what you were getting into. Your pistol already \ndrawn you expertly place a round between the eyes of one of the guards. The \nother guard desperately tries to place a round near you but fails. You respond \nby switching your bike back to normal mode and landing straight on top of the \nsecond guard. You pick up the guard's automatic weapon knowing more resistance \nwill be inside. Just inside the entrance to the roof several guards point their weapons at the door the leads to the roof. They hear a faint rev as the door is suddenly busted in. Blasting their weapons trying to hit the motorcyle, you jump off sending the bike towards the guards, eliminating a few. In the smoke and \nconfusion of the crash you jump through the smoke and open up, \nfinishing off the remaining guards. You've infiltrated the HIDEOUT.")
    if user == "drive":
        print("You rev your motorcycle and head full speed at the gate blasting away with your pistol at the first two guards, eliminating them. The guards in the windows and roof notice this and begin opening up. You're almost at the door, when suddenly a bullet hits your tire sending you flying off the bike. you land only feat from the door. Your leg stings. You can't move it. As you let out a cry for your \nbroken leg guards start to surround you, but you pistol is nowhere in sight...")
        endGame('Game Over')
        continue
    print("\n")
    print("Winding down corridors and occasionally fending off a guard or two, you come \nface to face with a large door. This must be the leader's room. Your \nitem is sure to be in here, along with the leader. You figure you could get \nrevenge and what he stole in one stone. The door being locked you blast away \nwith your weapon, making it resemble swiss cheese more than a door. Startled, a man inside pulls his sidearm aiming straight at you. Being startled yourself you try and let your weapon loose. But it seems that after blasting the door, \nyou're empty. Next thing you know you hear a gunshot, and are sent to the ground yelling. He shot you! \"Well well, what do we have here?\" Says the man. \"If it \nisn't our man of the day. Thought we left you to die out in the desert. Well I \nsuppose I should tell you what we wanted before I end you. It started out as a...\"An instinct kicks in. this is your chance. You still have your sidearm with \nyou and could take a SHOT at him. But if you do you might not ever KNOW more \nabout your past. You need to make a choice.")
    print("\n")
    print("Do you take the SHOT, or listen and KNOW more?")
    user = input()
    if user == "shot":
        print("\"You talk too much.\" You say as you blast wildy into the gang's leader. filling him with holes. After composing yourself you head to the boss's computer hoping to find out more. Searching the contents of the computer you find files on a \nmercenary. Skilled in combat, a tactical thinker, physically adept. You start to remember. This person is you!. The remaining contents of the computer reveal \nthat the gang had planned to implant your memories and experiance into \nintelligent machines to make the ultimte army. Until now... REVENGE IS YOURS!")
        break
    if user == "know":
        print("You decide that information might be more valuable and you let the boss speak.\"\nIt started as a raid on station 12... \"The boss pauses, looking at your belt.\" \nBut enough about me, let's end you.\" Aiming his weapon you regret this decision. So close. Just to fail.")
        endGame('Game Over')
        continue
