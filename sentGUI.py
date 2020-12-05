from tkinter import *
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests

#root = Tk()
###root.title('Sentiment Analysis')
#root.geometry('300x400')

#compName = Text(root, width=20, height=1)
#compTicker = Text(root, width=20, height=1)
#compTicker.pack(pady=20)
#compName.pack(pady=20)

class SentAnalysis:

    def __init__(self):
        root = Tk()
        root.title('NASDAQ Headline Sentiment Analyzer v0.1')
        root.geometry('850x350')
        root.iconbitmap('sentAnalysis.ico')
        #root.configure(background='black')

        button_frame = Frame(root)
        button_frame.grid(column=3, row=9)
        output = Text(root, width=70, height=1)
        
        titleLabel= Label(root, text='NASDAQ Headline Sentiment Analyzer v0.1')
        titleLabel.config(font=('Verdana 12 bold'))
        compNameLabel = Label(root, text='Company Name:')
        compTickerLabel = Label(root, text='Ticker Symbol')

        compName = Text(root, width=20, height=1)
        compTicker = Text(root, width=20, height=1)
        saveButton = Button(button_frame, text='Get Data', command=lambda:self.getURL(compName, compTicker, output))
        titleLabel.grid(column=3, row=2, pady=20, padx=30)
        compNameLabel.grid(column=3, row=3)
        compTickerLabel.grid(column=3, row=5)
        compName.grid(column=3, row=4, pady=7, padx=60)
        compTicker.grid(column=3,  row=6, padx=30)
        saveButton.grid(column=3, row=1, padx=30)
        output.grid(column=3, row=8, pady=45, padx=133)
        root.mainloop()
        return compName, compTicker


    def getURL(self, compName, compTicker, output):
        compNameText = compName.get('1.0', 'end-1c')
        compTickerText = compTicker.get('1.0', 'end-1c')
        linkText = compNameText + '/' + compTickerText + '/' 
        url = ('https://www.fool.com/quote/nasdaq/') + linkText        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        el1 = soup.select('h4')
        headlines = []
        substring = 'Transcript'
        self.getHeadlines(el1, headlines, substring, output)


    def getHeadlines(self, el1, headlines, substring, output):
        for i in el1:
            head = i.get_text()
            headlines.append(head.lower())
        str1 = ''
        headlines = str1.join(headlines)
        self.sentAnalysis(headlines, output)
        return headlines


    def sentAnalysis(self, headlines, output):
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(headlines)
        output.insert(END, vs)







SentAnalysis()
