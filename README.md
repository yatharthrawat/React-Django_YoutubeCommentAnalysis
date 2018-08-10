# React-Django_YoutubeCommentAnalysis
Web Application that classifies youtube comments as positive and negative with react frontend and DRF as backend.

Classification is done by the NaiveBayes Classifier in the Natural Language ToolKit (NLTK).
Currently classification is erroneous as the classifier uses the bag of words model and therefore doesn't account complexity in natural language.
With time as I learn more about Machine Learning and Natural Language Processing, I hope to improve this classifier and make it reach as close as human accuracy as possible

Classifier is saved as Classifier.sav using pickle to prevent repetitive training of model.
Model is currently trained on twitter_samples and movie_reviews corpus found in NLTK

This web app also uses the Youtube Data API to get comments of a particular video.
Therefore, to use the App, one requires creating a client_secret.json (OAUTH) file using the Google API console for the Youtube Data API.
Place the file in the backend folder.

The app's backend is written in Python using the Django Rest Framework. 
The backend is responsible for making API calls to the Data API as well as classifying the incoming comments as positive or negative using the classifier.
The backend then returns a JSON body for consumption by the frontend. (REST API)

The app's frontend uses React.
The frontend takes the URL from youtube as input for the backend and displays the consumed JSON.
Green stands for positive comment
Red stand for Negative comment
If number of positive and negative comments are equal, the background color of the page becomes yellow.


