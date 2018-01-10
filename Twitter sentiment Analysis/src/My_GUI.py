# -*- coding: utf-8 -*-

import numpy as np

import plotly.plotly as py

import matplotlib.pyplot as plt

import nltk

import tkinter as tk
from tkinter import *
class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master,width=500,height=60)
        self.grid()

        self.fnLabel = Label(master, text="TWITTER SENTIMENT ANALYSIS USING PYTHON")
        self.fnLabel.config(font=("Times New Roman", 14))
        self.fnLabel.grid()

        self.fnameLabel = Label(master, text="Choose File for analysis:")
        self.fnameLabel.grid()

        self.fc = Label(master, text="Chosen file path: ")
        self.fc.grid()

        self.label_fpath = Label(master, text="")
        self.label_fpath.grid()

        self.err_label = Label(master, text="")
        self.err_label.grid()
        
        self.submitButton = Button(master, command=self.buttonClick, text="Choose File")
        self.submitButton.grid()

        self.analyseButton = Button(master, command=self.analyse, text="analyse")
        self.analyseButton.grid()

        self.fpath=''


    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        
        self.fpath=filedialog.askopenfilename()
        self.label_fpath.config(text=self.fpath)
        self.err_label.config(text='')
        pass

    def analyse(self):
        #File analysis code starts here

        pos_tweets = [('I love this car', 'positive'),

                  ('This view is amazing', 'positive'),

                  ('I feel great this morning', 'positive'),

                  ('I am so excited about the concert', 'positive'),

                  ('He is my best friend', 'positive'),

                  ('The entire audience applauded at the conclusion of the film.', 'positive'),	
                    ('I left the theater with a lilt in my step', 'positive'),	
                    ('Duris has a wholesome appearance and gives a fine performance.', 'positive'),	
                    ('The rest of the cast also play well.', 'positive'),	
                    ('Cinematography noteworthy including fine views of Barcelona and its famed Gaudi towers', 'positive'),	
                    ('STEAMBOAT WILLIE is an amazingly important film to our cinema history', 'positive'),	
    ('This second appearance of Mickey Mouse (following the silent PLANE CRAZY earlier that year) is probably his most famous film--mostly because it was so ground-breaking', 'positive'),	
    ('While you don not yet hear Mickey speak, there are tons of sound effects and music throughout the film--something we take for granted now but which was a huge crowd pleaser in positive928', 'positive'),	
    ('However, after seeing the short again after about 25 years, I was amazed at how timeless the film actually is', 'positive'),	
    ('Its just adorable seeing Mickey playing "Turkey in the Straw" in a highly imaginative (if occasionally cruel) way', 'positive'),	
    ('Clever and a real crowd-pleaser--this film still ranks among Mickeys best films even after 80 wonderful years', 'positive'),	
    ('Being a 90s child, I truly enjoyed this show and I can proudly say that I enjoyed it big time and even more than the classical WB cartoons', 'positive'),
    ('But "Tiny Toons" kept the 90s vibe and delivered one of the most popular, funny, and underrated cartoons ever created', 'positive'),
    ('The memories are murky but I can only say that I enjoyed every single episode and product related to the show', 'positive'),
    ('Easily, none other cartoon made me laugh in a tender way (before getting into dark sitcoms oriented for teenagers)', 'positive'),
    ('The characters were all funny and had the peculiarity of not having a true lead character', 'positive'),
    ('Every single character was hilarious and deserved to be called a lead', 'positive'),
    ('The characters are interesting and you really care for them', 'positive'),
    ('An instant classic, with a great soundtrack and a catchy song during the ending credits', 'positive'),
    ('Do not miss it', 'positive'),
    ('Emily Watsons character is very strong, and she has only to give a quick glance and you understand everything', 'positive'),
    ('Despite the pans of reviewers, I liked this movie', 'positive'),
    ('In fact, I liked it better than Interview With a Vampire and I liked this Lestat (Stuart Townsend) better than Cruises attempt', 'positive'),
    ('Aailiyah was pretty good as Akasha, in places compelling (her first entrance and mini dance scene)', 'positive'),
    ('I am a big fan of this series mostly due to Anne Rice style, sensitivities and treatments', 'positive'),
    ('I guess I liked the details of his dysfunction--he was believable', 'positive'),
    ('But I thought his acting was skilled', 'positive'),
    ('Meredith M was better than all right', 'positive'),
    ('A very charming film with wonderful sentiment and heart', 'positive'),
    ('It is rare when a film-maker takes the time to tell a worthy moral tale with care and love that does not fall into the trap of being overly syrupy or over indulgent', 'positive'),
    ('Nine out of ten for a truly lovely film', 'positive'),
    ('This early film from future goremeister Lucio Fulci is a very good addition to the giallo sub-genre', 'positive'),
    ('This is one of the best Italian thrillers of the early 70s', 'positive'),
    ('A standout scene', 'positive'),
    ('It is still wild stuff though and is highly recommended to fans of giallo cinema', 'positive'),
    ('The movie was very interesting from beginning to the end', 'positive'),
    ('I liked the way Dustin Hoffmans character was ready to do just about everything to stay with his son', 'positive'),
    ('This movie is also revealing', 'positive'),
    ('Personally, I think it shows that people should learn to find a compromise them self without involving other people into issue', 'positive'),
    ('All the actors give a wonderful performance, especially Jennifer Rubin as Jamie Harris, who changes from the nervous starlet in the beginning through the strange events she is part of to the cool star', 'positive'),
    ('You learn a lot about the real inside emotions of people in this movie, and a lot about the movie business itself', 'positive'),
    ('The movie in movie situations in the beginning and through the game that is played with her by the "acting coach" are fascinating', 'positive'),
    ('Also the music by Mark Snow is possibly the best score I have ever heard', 'positive'),
    ('You would not forget this movie!  ', 'positive'),
    ('This movie is so awesome!  ', 'positive'),
    ('I loved it, it was really scary', 'positive'),
    ('I love the Scream movies and all horror movies and this one ranks way up there', 'positive'),
    ('If you want a real scare rent this one!  ', 'positive'),
    ('43018', 'positive'),
    ('This is an extraordinary film', 'positive')
    

                  ]


        neg_tweets = [('I do not like this car', 'negative'),

                  ('This view is horrible', 'negative'),

                  ('I feel tired this morning', 'negative'),

                  ('I am not looking forward to the concert', 'negative'),

                  ('He is my enemy', 'negative'),
                   ('About ten minutes into this film I started having second thoughts', 'negative'),
    ('About half way through this film I started to dislike it', 'negative'),
    ('By the time the film ended, I not only disliked it, I despised it.', 'negative'),
    ('What this film lacks is a convincing script', 'negative'),
    ('The script looks as if only a rough draft was written and shooting began before a finished script was completed', 'negative'),
    ('Things happen, characters personalities change, plot twists occur for no real reason other than that script calls for it', 'negative'),
    ('This is probably the most irritating show I have ever seen in my entire life.', 'negative'),
    ('It is indescribably the most annoying and idiotic show I have ever seen', 'negative'),
    ('Everything about it is just bad', 'negative'),
    ('I could not understand, what kind of idiot would produce this mess in the first place not to mention several season', 'negative'),
    ('The script is bad, very bad  it contains both cheesiness and unethical joke that you normally see in rated R or NC-positive7 movie', 'negative'),
    ('The casting is also horrible, cause all you see is a really really BAD Actors, period', 'negative'),
    ('Final Word: This Show is a real torture!!  ', 'negative'),
    ('It is zillion times away from reality', 'negative'),
    ('Watching washing machine twirling around would not hurt your eyes as much as this show', 'negative'),
    ('Rating: 0/10 (Grade: Z) Note: The Show Is So Bad That Even Mother Of The Cast Pull Her Daughter Out Of The Show', 'negative'),
    ('20th Century Foxs ROAD HOUSE 1948) is not only quite a silly noir but is an implausible unmitigated bore of a movie', 'negative'),
    ('Full of unconvincing cardboard characters it is blandly written by Edward Chodorov, who also produced, and is surprisingly directed by Jean Negulesco from whom one would expect a great deal more', 'negative'),
    ('From here on the Widmark character turns unintentionally comical!  ', 'negative'),
    ('His losing his marbles so early in the proceedings is totally implausible and unconvincing', 'negative'),
    ('And if that is not enough of a mess of a movie for you - the picture is also marred with a constant use of studio sets and indoor exteriors', 'negative'),
    ('Whatever prompted such a documentary is beyond me!  ', 'negative'),
     (') Do not waste your time', 'negative'),
    ('End of Days is one of the worst big-budget action movies I have ever seen', 'negative'),
    ('He surely does not know how to make a coherent action movie from the screenwriter of Air Force One who was only obliged to write the script just for a big sum of money', 'negative'),
    ('This was one of the worst films i have ever seen', 'negative'),
    ('I am still trying to get over how bad it was', 'negative'),
                  ('positive hour 54 minutes of sheer tedium, melodrama and horrible acting, a mess of a script, and a sinking feeling of GOOD LORD, WHAT WERE THEY THINKING?  ', 'negative'),
    ('Lots of holes in the script', 'negative'),
    ('It is like a bad two hour TV movie', 'negative'),
    ('Now imagine that every single one of those decisions was made wrong', 'negative'),
    ('The dialogue is atrocious', 'negative'),
    ('The acting is beyond abysmal', 'negative'),
    ('Everything stinks', 'negative'),
    ('Trouble is, the writing and directing make it impossible to establish those things that make a movie watchable, like character, story, theme and so on', 'negative'),
    ('Worse, there is an incredibly weak sub-plot thrown in that follows a little band of latter-day Mansonites as they go after a reporter who working on a story on the anniversary of the killings', 'negative'),
    ('It is dumb and pointless, and a complete waste of time', 'negative'),
    ('In short, do not bother with this movie', 'negative'),
    ('Either way, it sucks', 'negative'),
    ('The script is horrendously stupid', 'negative'),
    ('The story starts too fast with absolutely no suspense or build-up in the slightest', 'negative'),
    ('Everything Captain Howdy says is either laughable or just plain stupid', 'negative'),
    ('What the hell kind of crap is that?!  ', 'negative'),
    ('Then, there is the plot holes', 'negative'),
    ('You could drive a semi truck into these holes!  ', 'negative')




                  ]


        tweets = []

        for (words, sentiment) in pos_tweets + neg_tweets:

            words_filtered = [e.lower() for e in words.split() if len(e) >= 3]

            tweets.append((words_filtered, sentiment))

        test_tweets = [

            (['feel', 'happy', 'this', 'morning'], 'positive'),

            (['larry', 'friend'], 'positive'),

            (['not', 'like', 'that', 'man'], 'negative'),

            (['house', 'not', 'great'], 'negative'),

            (['your', 'song', 'annoying'], 'negative')]


        def get_words_in_tweets(tweets):

            all_words = []

            for (words, sentiment) in tweets:

              all_words.extend(words)
            
            return all_words

        def get_word_features(wordlist):

            wordlist = nltk.FreqDist(wordlist)

            word_features = wordlist.keys()

            return word_features

        word_features = get_word_features(get_words_in_tweets(tweets))
 

        def extract_features(document):

            document_words = set(document)

            features={}

            for word in word_features:

                features['contains(%s)' % word] = (word in document_words)

            return features

        document = ['I','love','chocolates']

        training_set = nltk.classify.apply_features(extract_features, tweets)

        classifier = nltk.NaiveBayesClassifier.train(training_set)

        #Reading tweets from a file

        if (self.fpath!=''):
            f= open(self.fpath,'r')

            pcount=0

            ncount=0

            for line in f.readlines():
                tweet= line

                print('\n'+ 'The tweet- '+ tweet +' is classified as: \n')

                if((classifier.classify(extract_features(tweet.split())))=='positive'):

                    print("positive")

                    pcount+=1

                elif((classifier.classify(extract_features(tweet.split())))=='negative'):

                    print("negative")

                    ncount+=1

            f.close();

            print("\nPositive tweets are:"+ str(pcount))

            print("\n Negative tweets are:"+ str(ncount))

            #Plotting the bar graphs for the results 

            y=[pcount,ncount]

            N=len(y)

            x=range(N)

            width=1/2

            plt.bar(x, y,width,color="green")
            plt.show()

        else:
            self.err_label.config(text='Choose a file first!')


        #File analysis code ends here 
 
if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
