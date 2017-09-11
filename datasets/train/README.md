## Training data ##

In this repository you will find the training data for SemEval-2018 Task 3.

### NOTE ###
Please note that by using the Twitter data you agree to abide
by the Twitter terms of service (https://dev.twitter.com/overview/terms/agreement-and-policy),
and in particular you agree not to redistribute the data, the annotations or the corpus obtained, as this violates the Twitter Terms of Use.


#### Task A ####
* Task: binary
* Labels: **0** (not ironic), **1** (ironic)
* File format: a tab-separated file with one line per tweet containing per line the tweet index, a binary classification label, and the tweet text.

### Task B ###
* Task: multiclass
* Labels: Labels: **1** (ironic by clash), **2** (other irony), **3** (situational irony), **4** (non-ironic)
* File format: a tab-separated file with one line per tweet containing per line the tweet index, a multiclass classification label, and the tweet text.


#### Details: ####
All tweets were collected using the <a href="http://dev.twitter.com/rest/public target="_blank">[Twitter API]</a> using the hashtags #irony, #sarcasm and #not.

The data were collected between 01/12/2017 and 04/01/2015 and represent 2,676 unique users. The corpus was manually labeled using a fine-grained annotation scheme for irony (Van Hee et al., 2016). 20% of this corpus were annotated as non-ironic, and additional non-ironic tweets were added from a background (i.e. randomly crawled) Twitter corpus to balance the corpus distribution.

The entire corpus contains 4,792 tweets and is split into a set for training (80%) and testing (20%). Participants are free, however, to split the training set into a set for training and development.

*** Corpus cleaning ***
Prior to data annotation, the entire corpus was cleaned by removing retweets, duplicates and non-English tweets, and replacement of XML-escaped characters (e.g., &amp;). Emoji were converted to UTF-8 descriptions (e.g. :smiling\_face:) for practical reasons related to the annotation of the dataset and by using the script emoji\_converter.py.

