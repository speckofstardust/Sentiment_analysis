import sentiment_analysis
import matplotlib.pyplot as plt 
from tkinter import *

# Function for clearing the contents of all entry boxes and text area.
def clearAll() : 

	# deleting the content from the entry box 
	negativeField.delete(0, END) 
	neutralField.delete(0, END) 
	positiveField.delete(0, END) 
	overallField.delete(0, END) 

	# whole content of text area is deleted 
	textArea.delete(1.0, END)
	
# function to print sentiments of the sentence. 
def detect_sentiment():

	# get a whole input content from text box
	sentence = textArea.get("1.0", "end")
	sentiment_dict = sentiment_analysis.analysis(sentence) 

	string = str(round(sentiment_dict['neg']*100,2)) + "%"
	negativeField.insert(10, string)
	

	string = str(round(sentiment_dict['neu']*100,2)) + "%"
	neutralField.insert(10, string)

	string = str(round(sentiment_dict['pos']*100,2)) +"%"
	positiveField.insert(10, string)
	
	# decide sentiment as positive, negative and neutral 
	if max(sentiment_dict['pos'],sentiment_dict['neu'],sentiment_dict['neg']) == sentiment_dict['pos']:
		string = "Positive"

	elif max(sentiment_dict['pos'],sentiment_dict['neu'],sentiment_dict['neg']) == sentiment_dict['neg']:
		string = "Negative"

	else :
		string = "Neutral"

	overallField.insert(10, string)
	
    #plot a pie graph
	plt.pie(sentiment_dict.values(), labels=["negetive", "neutral", "positive"])
	plt.axis("equal")
	plt.show()
		


# Driver Code 
if __name__ == "__main__" :
	

	# Create a GUI window 
	gui = Tk() 
	
	# Set the background colour of GUI window 
	gui.config(background = "light grey") 

	# set the name of tkinter GUI window 
	gui.title("Sentiment Detector") 

	# Set the configuration of GUI window 
	gui.geometry("400x510") 

	# create a label : Enter Your Task 
	enterText = Label(gui, text = " Enter Your Sentence: ",
									bg = "grey55")

	# create a text area for the root 
	# with lunida 13 font 
	# text area is for writing the content 
	textArea = Text(gui, height = 5, width = 40, font = "lucida 13", wrap="word")

	# create a Submit Button and place into the root window 
	# when user press the button, the command or 
	# function affiliated to that button is executed 
	check = Button(gui, text = "Analyse", fg = "White", 
						bg = "Black", command = detect_sentiment)

	# Create a negative : label 
	negative = Label(gui, text = " Negetive Sentiment: ",
										bg = "grey55") 

	# Create a neutral : label 
	neutral = Label(gui, text = " Neutral Sentiment: ", 
									bg = "grey55") 

	# Create a positive : label 
	positive = Label(gui, text = " Positive Sentiment: ",
										bg = "grey55")

	# Create a overall : label 
	overall = Label(gui, text = " Sentence is Overall Rated As: ",
										bg = "grey55")

	# create a text entry box 
	negativeField = Entry(gui)

	# create a text entry box 
	neutralField = Entry(gui)

	# create a text entry box 
	positiveField = Entry(gui)

	# create a text entry box 
	overallField = Entry(gui) 

	# create a Clear Button and place into the root window 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	clear = Button(gui, text = "Clear", fg = "White", 
					bg = "Black", command = clearAll)
	
	# create a Exit Button and place into the root window 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	Exit = Button(gui, text = "Exit", fg = "White", 
						bg = "Black", command = exit)

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure. 
	enterText.grid(row = 0, column = 2, pady=(15,5))
	
	textArea.grid(row = 1, column = 2, padx = 10, sticky = W)
	
	check.grid(row = 2, column = 2, pady=(10,5))
	
	negative.grid(row = 3, column = 2, pady=(5,0))
	
	neutral.grid(row = 5, column = 2, pady=(5,0))
	
	positive.grid(row = 7, column = 2, pady=(5,0))
	
	overall.grid(row = 9, column = 2, pady=(5,0))
	
	negativeField.grid(row = 4, column = 2)

	neutralField.grid(row = 6, column = 2)
					
	positiveField.grid(row = 8, column = 2)
	
	overallField.grid(row = 10, column = 2)
	
	clear.grid(row = 11, column = 2, pady=(20,5))
	
	Exit.grid(row = 12, column = 2)
	
    # Add a frame to set the size of the window
	frame= Frame(gui, relief= 'sunken')
	frame.grid(sticky= "we")


	# start the GUI 
	gui.mainloop() 
	
