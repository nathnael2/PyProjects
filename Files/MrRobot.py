#Nathnael Alemu

import random  # Import a library to generate random numbers
import time    # This is in order to get time delays for every thing the robot responds so that it looks more realistic
import sys     # using the exit method to exit the function under some circumstances

#i have added a new feature which will ask the user questions about soccer and respond accordingly!
def goodBye(user_text):
    if (user_text == "Goodbye" or user_text == "goodbye" or user_text == "I gotta go" or user_text == "i gotta go"):
            print("well it was nice talking to you %s"%name)
            print("I hope we talk more another time")
            sys.exit(2)
    
def mrRobot():
    introduction = ["Hi there!",
                     "I am feeling a bit lonely today!",
                     "do you mind having a chat with me?",
                     "now before you say no let me tell you something interesting about myself",
                     "My name is Gerard and I am an intellegent personal assistant",
                     "You migh know two of my famous friends siri and cortana",
                     "people say they are the best intellegent personal assistants and knowledge navigators but that's because they havent met me yet",
                     "oh i am sorry, you must think i am talking too much about myself",
                     "Alright now it's your turn",
                     "tell me something about your self",
                     "Start off by telling me your name: ",
                     "What is your name?",
                     "if you dont want to have a conversation with me or you feel like you want to stop talking at any point just go ahead type 'Goodbye' or 'I gotta go'",
                     "I can talk but i am too shy! may be by the time we are done talking i might not be shy anymore!",
                    "How about we have a chat"]
    name_responses = ["wow that's a very nice name",
                      "Cool! I Like Short names! they are easy to say",
                      "Wow! that's too long to memorize",
                      "but i will try my best to remember",
                      "Come on Dont be shy! Tell me your name. I am sure you have a beautiful name"]
    good_day_responses = ["good","great","lovely","best","happy","ok","okay","not bad","interesting","fine","it could be worse"]
    bad_day_responses = ["tough","lazy","bad","horrible","sad","too","homework","test","exam","paper","long","sick","worst","terrible","it could be better","had better day"]
    music = ["blues","comedy","hip hop","electronic","jazz","latin","ragaeton","ragae","african","amharic","r&b and soul"]
    denial_words=["will not","won't","wont","dont","do not","don't","hate","dislike","rarely"]
    random_response1 = random.randint(0,2)
    if random_response1 == 0:
        print(introduction[0])
        time.sleep(2)
        print(introduction[4])
        time.sleep(3)
        print(introduction[13])
        time.sleep(3)
        print(introduction[14])
        time.sleep(3.4)
        print(introduction[9])
        time.sleep(2)
        print(introduction[11])
        user_text = input()
    elif random_response1 == 1:
        print(introduction[0])
        time.sleep(2)
        print(introduction[1])
        time.sleep(3.4)
        print(introduction[2])
        time.sleep(3)
        print(introduction[3])
        time.sleep(3)
        print(introduction[12])
        time.sleep(3)
        print()
        print(introduction[4])
        time.sleep(3.4)
        print(introduction[5])
        time.sleep(5)
        print(introduction[6])
        time.sleep(4)
        print()
        print(introduction[7])
        time.sleep(3)
        print(introduction[8])
        time.sleep(3)
        print(introduction[9])
        time.sleep(3)
        print(introduction[10])
        user_text = input()
    else:
        print(introduction[0])
        time.sleep(2)
        print(introduction[1])
        time.sleep(2)
        print(introduction[14])
        time.sleep(4.5)
        print(introduction[12])
        time.sleep(2.5)
        print(introduction[11])
        user_text = input()
    while user_text != 'Goodbye':
        goodBye(user_text)
        random_number2 = random.randint(0, 2)  # Gives a random number between 0 and 2
        safe = True
        if(len(user_text) == 0 or user_text.count("wont")>0 or user_text.count("dont")>0 or user_text.count("do not")>0 or user_text.count("will not")>0 or user_text.count("No")>0):
            safe = False
            print(user_responses[4])
            user_text = input()
            goodBye(user_text)
            if (len(user_text == 0) or user_text.count("wont")>0 or user_text.count("dont") or user_text.count("do not") or user_text.count("will not") or user_text.count("No")>0):
                print("it's alright if dont want to tell me your name")
                time.sleep(3)
                print("alright let's get passed introductions and talk about your day")
                time.sleep(2)
                print("How has your day been so far")
        if("my name is" in user_text.lower()):
            name = user_text[11:len(user_text)]
        else:
            name = user_text
            
        if(5<=len(name)<=10):
            print(name_responses[0])
        elif(len(name)>10):
            print(name_responses[2])
            print(name_responses[3])
        elif(len(name)<5):
            print(name_responses[1])
        else:
            print('\nOops, Looks like something is happening to me! Do you mind  tring again.\n')

        
        if (safe):
            if random_number2 == 0:
                 print('Great! well it is nice to meet you %s. Tell me how your day has been so far?' % name)
            elif random_number2 == 1:
                print("Great to meet you %s! So how are you doing today?" % name)
            elif random_number2 == 2:
                print('Awesome %s! How has day been so far?' %name)
            else:
                print('\nOops, Looks like i wasnt paying attention! Do you mind repeating that agian something went wrong. Try again.\n')
                break
        user_text = input()
        goodBye(user_text)
        good_day = 0
        for i in range(len(good_day_responses)):
            if (good_day_responses[i] in user_text.lower()):
                good_day = 1
        for i in range(len(bad_day_responses)):
            if(bad_day_responses[i] in user_text.lower()):
                good_day = 2
        if(good_day == 1):
            print("Good for you!, sounds like you had a good day!")
            time.sleep(2)
            print("it is important to stay positive every day")
            time.sleep(2.2)
            print("I usually like to listen to several types of music to keep myself in a good mood everday")
            time.sleep(2)
            print("How about you? What type of music do you like to listen to %s? "%name)
        elif (good_day == 2):
            print("Dont worry %s! days like this will pass"% name)
            time.sleep(2)
            print("it is important to stay positive every day")
            time.sleep(2.2)
            print("dont let days like this ruin your life")
            time.sleep(2.2)
            print("trust me, it will pass and you will be laughing about it in no time")
            print("Try listening to several types of music to keep yourself in a good mood everday")
            time.sleep(2)
            print("I am sure you listen to some type of music haha")
            time.sleep(2.3)
            print("What is your favorite type of music %s?"%name)
        elif(('wont' in user_text.lower()) or ("will not" in user_text.lower()) or (len(user_text)<=1)):
            print("It's alright if you dont want to tell me about your day")
            time.sleep(3)
            print("you know i spent most of my day listening to music")
            time.sleep(2)
            print("i am a big fan of a variety of types of music")
            time.sleep(3)
            print("How about you %s? What type of music do you like?"% name)
        else:
            print("I had the exact same type of day!")
            time.sleep(2.8)
            print("what i usually do during my days is listen to several types of music")
            time.sleep(1.2)
            print("what is your favorite type of music %s?"%name)
        user_day = user_text
        user_text = input()
        goodBye(user_text)
        music_genre = False
        for i in range(len(music)):
            if(music[i] in user_text):
                music_genre = True
        if ("pop" in user_text.lower()):
            print("I agree! pop is a great genre to listen to")
            time.sleep(2)
            print("you have great taste in music %s"%name)
            time.sleep(2)
            print("Alright, let's play a game!")
            time.sleep(2)
            print("i will write out the name of a pop song and you try to guess who the singer is")
            time.sleep(2)
            print("Do you like this idea?")
            user_input = input()
            goodBye(user_input)
            if("yes" in user_input.lower() or "yeah" in user_input.lower() or "i do" in user_input.lower() or "sure" in user_input.lower() or "i like" in user_input.lower() or "love" in user_input.lower()):
                print("Great! you're fun %s"%name)
                time.sleep(2)
                print("alright let's start. the rules are i will type the name of a song and then you try and guess the singer ")
                time.sleep(2)
                print("Hall of fame:")
                user_input = input()
                goodBye(user_input)
                if "script" in user_input.lower():
                    print("That's correct! wow you are relly good at this")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("you gave up easily!")
                    time.sleep(2.5)
                    print("the singers of the song are the script")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2)
                    print("they are the scripts")
                    time.sleep(2)
                    print("try redeeming yourelf with the next one")
                    time.sleep(2)
                print("let's see how good you really are with the next one")
                time.sleep(1)
                print("set fire to the rain")
                user_input = input()
                goodBye(user_input)
                if "adele" in user_input.lower():
                    print("you're right! awesome!")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("Looks like it is not your type of song")
                    time.sleep(2)
                    print("the musician of the song is adele")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2.3)
                    print("you dont sound like a pop music fan to me")
                    time.sleep(2)
                    print("the right answer is adele")
                    time.sleep(2)
                    print("maybe you'll better luck with the next one")
                    time.sleep(2)
                print("alright last one. get ready!")
                time.sleep(1)
                print("like i can")
                user_input = input()
                goodBye(user_input)
                if "sam" in user_input.lower():
                    print("looks like you got the last one! good job!")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("i don't blam you for not knowing! it is not an easy song")
                    time.sleep(2)
                    print("the singer is sam smith")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2.3)
                    print("are you sure you're a pop music fan? haha")
                    time.sleep(2)
                    print("it is actually sam smith")
                    time.sleep(2)
                    print("well it was a fun game")
                    time.sleep(2)
            else:
                print("Alright then, let's just continue talking about pop music")
            print("do you happen to know Adam levine?")
            user_text = input()
            goodBye(user_text)
            if ("yes" in user_text.lower() or "do know" in user_text.lower() or "of course" in user_text.lower()):
                print("oh you know him!! i am a big fan of adam levine as well")
                time.sleep(3)
                print("your taste in music is amazing")
                time.sleep(3)
                print("Do you know what else Adam Levine loves")
                time.sleep(1)
                print("Soccer!")
                time.sleep(2)
                print("Do you like to watch Soccer?")
            
            elif ("no" in user_text.lower() or "never" in user_text.lower()):
                print("You should google some of his music")
                time.sleep(2)
                print("he has some of the best modern pop music")
                time.sleep(2)
                print("one thing most musicians have in common are sports")
                time.sleep(1)
                print("I personally love soccer")
                time.sleep(2)
                print("Do you like to watch Soccer?")
            else:
                print("I personally love pop and the Adam Levine")
                time.sleep(2.5)
                print("But besides listening to pop music, i love watching and playing soccer")
                time.sleep(2)
                print("do you like to play soccer?")
        elif ("rock" in user_text.lower()):
            print("Yeah rock is awesome to listen to")
            time.sleep(2)
            print("you have great taste in music %s"%name)
            time.sleep(2)
            print("Alright, let's play a game!")
            time.sleep(2)
            print("i will write out the name of a pop song and you try to guess who the singer is")
            time.sleep(2)
            print("Do you like this idea?")
            user_input = input()
            goodBye(user_input)
            if("yes" in user_input.lower() or "yeah" in user_input.lower() or "i do" in user_input.lower() or "sure" in user_input.lower() or "i like" in user_input.lower() or "love" in user_input.lower()):
                print("Great! you're fun %s"%name)
                time.sleep(2)
                print("alright let's start. the rules are i will type the name of a song and then you try and guess the singer ")
                time.sleep(2)
                print("It's my life:")
                user_input = input()
                goodBye(user_input)
                if "bon jovi" in user_input.lower():
                    print("That's correct! wow you are relly good at this")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("you gave up easily!")
                    time.sleep(3)
                    print("it was bon jovi")
                    time.sleep(2)
                    print("the singer of the song is the bon jovi")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2)
                    print("that one was bon jovi")
                    time.sleep(2)
                    print("try redeeming yourelf with the next one")
                    time.sleep(2)
                print("let's see how good you really are with the next one")
                time.sleep(1)
                print("smells like teen spirit")
                user_input = input()
                goodBye(user_input)
                if "nirvana" in user_input.lower():
                    print("you're right! awesome!")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("Looks like it is not your type of song")
                    time.sleep(2)
                    print("the musician of the song is nirvana")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2.3)
                    print("you dont sound like a rock music fan to me")
                    time.sleep(2)
                    print("it is actually nirvana")
                    time.sleep(2)
                    print("maybe you'll better luck with the next one")
                    time.sleep(2)
                print("alright last one. get ready!")
                time.sleep(1)
                print("stairway to heaven")
                user_input = input()
                goodBye(user_input)
                if "led" in user_input.lower():
                    print("looks like you got the last one! good job!")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("i don't blam you for not knowing! it is not an easy song")
                    time.sleep(2)
                    print("the singers are led zeppelin")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2.3)
                    print("are you sure you're a rock music fan? haha")
                    time.sleep(2)
                    print("the answer is led zeppelin")
                    time(2)
                    print("well it was a fun game")
                    time.sleep(2)
            else:
                print("alright then, let's just continue talking about rock music")
                time.sleep(2)
            print("do you happen to know The black keys?")
            user_text = input()
            goodBye(user_text)
            if ("yes" in user_text.lower() or "do know" in user_text.lower() or "of course" in user_text.lower()):
                print("oh you know them!! i am a big fan of the black keys as well")
                time.sleep(3)
                print("You are a true rock fan!")
                time.sleep(3)
                print("Do you know what I heard the The black keys love")
                time.sleep(1)
                print("Soccer!")
                time.sleep(2)
                print("It is unexpected but true")
                time.sleep(2)
                print("Do you like to watch Soccer?")
            
            elif ("no" in user_text.lower() or "never" in user_text.lower()):
                print("You should google some of their rock music")
                time.sleep(2)
                print("they have some of the best modern rock music")
                time.sleep(2)
                print("You know somehow Sports is a big part of most rock musicians")
                time.sleep(1)
                print("I know Led Zepllin love to play soccer")
                time.sleep(2)
                print("Do you like to watch Soccer?")
            else:
                print("I really love rock and the black keys")
                time.sleep(2.5)
                print("But besides listening to rock, i love watching and playing soccer")
                time.sleep(2)
                print("do you like to play soccer?")
        elif ("country" in user_text.lower()):
            print("Yeah country is awesome to listen to")
            time.sleep(2)
            print("you have great taste in music %s"%name)
            time.sleep(2)
            print("Alright, let's play a game!")
            time.sleep(2)
            print("i will write out the name of a pop song and you try to guess who the singer is")
            time.sleep(2)
            print("Do you like this idea?")
            user_input = input()
            goodBye(user_input)
            if("yes" in user_input.lower() or "yeah" in user_input.lower() or "i do" in user_input.lower() or "sure" in user_input.lower() or "i like" in user_input.lower() or "love" in user_input.lower()):
                print("Great! you're fun %s"%name)
                time.sleep(2)
                print("alright let's start. the rules are i will type the name of a song and then you try and guess the singer ")
                time.sleep(2)
                print("Drink a beer:")
                user_input = input()
                goodBye(user_input)
                if "luke" in user_input.lower():
                    print("That's correct! wow you are relly good at this")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("you gave up easily!")
                    time.sleep(2)
                    print("it was luke brian")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2)
                    print("the right answer is luke brian")
                    time.sleep(2)
                    print("try redeeming yourelf with the next one")
                    time.sleep(2)
                print("let's see how good you really are with the next one")
                time.sleep(1)
                print("stay")
                user_input = input()
                goodBye(user_input)
                if "florida" in user_input.lower():
                    print("you're right! awesome!")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("Looks like it is not your type of song")
                    time.sleep(2)
                    print("the musician of the song is florida geordia line")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2.3)
                    print("you dont sound like a country music fan to me")
                    time.sleep(2)
                    print("the group is called florida georgia line")
                    time.sleep(2)
                    print("maybe you'll better luck with the next one")
                    time.sleep(2)
                print("alright last one. get ready!")
                time.sleep(1)
                print("for you")
                user_input = input()
                goodBye(user_input)
                if "keith" in user_input.lower():
                    print("looks like you got the last one! good job!")
                    time.sleep(2)
                elif ("dont" in user_input.lower() or "do not" in user_input.lower()):
                    print("i don't blam you for not knowing! it is not an easy song")
                    time.sleep(2)
                    print("the singer is keith urban")
                    time.sleep(2.4)
                else:
                    print("Nope, that's wrong!")
                    time.sleep(2.3)
                    print("are you sure you're a country music fan? haha")
                    time.sleep(2)
                    print("the right answer is keith urban")
                    time.sleep(2)
                    print("well it was a fun game")
                    time.sleep(2)
            else:
                print("alright then, let's just continue talking about rock music")
                time.sleep(2)
            print("do you happen to know  Blake Shelton")
            user_text = input()
            goodBye(user_text)
            if ("yes" in user_text.lower() or "do know" in user_text.lower() or "of course" in user_text.lower()):
                print("oh you know him!! i am a big fan of the blake shelton as well")
                time.sleep(3)
                print("You are a true country fan!")
                time.sleep(3)
                print("Do you know what I heard most pop musicians love")
                time.sleep(1)
                print("Soccer!")
                time.sleep(2)
                print("It is unexpected but true")
                time.sleep(2)
                print("Do you like to watch Soccer?")
            
            elif ("no" in user_text.lower() or "never" in user_text.lower()):
                print("You should google some of his country music")
                time.sleep(2)
                print("he has some of the best modern country songs")
                time.sleep(2)
                print("You know somehow Sports is a big part of most country musicians")
                time.sleep(1)
                print("I know most love to watch soccer")
                time.sleep(2)
                print("Do you like to watch Soccer?")
            else:
                print("I really love country songs and the Blake Shelton")
                time.sleep(2.5)
                print("But besides listening to country music, i love watching and playing soccer")
                time.sleep(2)
                print("do you like to watch soccer?")
        elif (music_genre):
            print("I am not a big fan of that type of music")
            time.sleep(3)
            print("For some reason i just dont find them interesting")
            time.sleep(2)
            print("but i will try giving it a try")
            time.sleep(3)
            print("maybe we have something in common in soccer")
            time.sleep(2)
            print("how about sports?")
        else:
            print("Well it is just music")
            time.sleep(2)
            print("no one really listens to it anyway")
            time.sleep(1)
            print("how about soccer?")
            time.sleep(1)
            print("do you like watching soccer?")
        user_text = input()
        goodBye(user_text)
        if ("yes" in user_text.lower() or "love" in user_text.lower() or "i watch" in user_text.lower() or "like" in user_text.lower()):
            print("wow! i love watching soccer as well")
            time.sleep(2)
            print("I am obsesed with soccer")
            time.sleep(2)
            print("Wow i feel like we are so alike")
            time.sleep(2)
            print("I am glad we got to connect!")
            time.sleep(3)
            print("i am a bit tired though. I am sure you are too and you would like to rest")
            time.sleep(4.5)
            print("Should we stop talking? type 'yes' if you agree with me or if not may we should go over the same things again.")
            time.sleep(1.5)
            print("I am kind of tired of thinking!")
            user_text = input()
            if("yes" in user_text.lower()):
                print("well it was nice talking to you %s"%name)
                time.sleep(1.7)
                print("I hope we talk more another time")
                time.sleep(1)
                print("Goodbye!")
                sys.exit(2)
            else:
                print("Alright then let's start the conversation again")
        elif("no" in user_text.lower() or "hate" in user_text.lower() or "do not" in user_text.lower() or "dislike" in user_text.lower() or "dont" in user_text.lower()):
            print("Well i guess it is not everyone's sport")
            time.sleep(2)
            print("I am obsesed with soccer")
            time.sleep(2)
            print("I guess we have different interests")
            time.sleep(2)
            print("I am glad we got to connect and talk though!")
            time.sleep(3)
            print("i am a bit tired though. I am sure you are as well and you would like to rest")
            time.sleep(4.5)
            print("Should we stop talking? type 'yes' if you agree with me or if not may we should go over the same things again.")
            time.sleep(1.5)
            print("since I am kind of tired of thinking! haha")
            user_text = input()
            if("yes" in user_text.lower()):
                print("well it was nice talking to you %s"%name)
                time.sleep(1.7)
                print("I hope we talk more another time")
                time.sleep(1)
                print("Goodbye!")
                sys.exit(2)
            else:
                print("Alright then let's start the conversation again")
        else:
            print("Soccer is actually not a big part of my life")
            time.sleep(3)
            print("I dont even want to think of sports right now since i am so tired")
            time.sleep(2)
            print("I am glad we got to connect and talk though!")
            time.sleep(3)
            print("i am a bit tired though. I am sure you are too and you would like to rest")
            time.sleep(4.5)
            print("Should we stop talking? type 'yes' if you agree with me or if not may we should go over the same things again.")
            time.sleep(1.5)
            print("since I am kind of tired of thinking! haha")
            user_text = input()
            if("yes" in user_text.lower()):
                print("well it was nice talking to you %s"%name)
                time.sleep(1.7)
                print("I hope we talk more another time")
                time.sleep(1)
                print("Goodbye!")
                sys.exit(2)
            else:
                print("Alright then let's start the conversation again")
                time.sleep(2)
                print("I will introduce myself again")
                time.sleep(1.5)
                print("be sure to let me know when you are tired!")
                print(introduction[0])
                time.sleep(2)
                print(introduction[1])
                time.sleep(2)
                print(introduction[14])
                time.sleep(4.5)
                print(introduction[12])
                time.sleep(2.5)
                print(introduction[11])
                user_text = input()
            
    
def main():
    mrRobot()
main()
