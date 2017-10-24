## Training data ##

In this repository you will find the training data for SemEval-2018 Task 3. The training files are provided with preprocessed emoji (i.e. converted to UTF-8 descriptions) and the original emoji (_emoji.txt).


#### NOTE ####
Please note that by using the Twitter data you agree to abide
by the <a href="https://dev.twitter.com/overview/terms/agreement-and-policy" target="_blank">Twitter terms of service</a>, and in particular you agree not to redistribute the data, the annotations or the corpus obtained, as this violates the Twitter Terms of Use.


#### Task A ####
* Task: binary
* Labels: **0** (not ironic), **1** (ironic)
* File format: a tab-separated file with one line per tweet containing per line the tweet index, a binary classification label, and the tweet text.

### Task B ###
* Task: multiclass
* Labels: Labels: **1** (ironic by clash), **2** (situational irony), **3** (other irony), **0** (non-ironic)
* File format: a tab-separated file with one line per tweet containing per line the tweet index, a multiclass classification label, and the tweet text.


#### Details: ####

<h5> Corpus construction</h5>
All tweets were collected using the <a href="http://dev.twitter.com/rest/public" target="_blank"><tt>Twitter API</tt></a> using the hashtags #irony, #sarcasm and #not.

The data were collected between 01/12/2017 and 04/01/2015 and represent 2,676 unique users. The corpus was manually labelled using a fine-grained annotation scheme for irony (Van Hee et al., 2016). 20% of this corpus were annotated as non-ironic, and additional non-ironic tweets were added from a background Twitter corpus to obtain a balanced class distribution. The tweets in the background corpus were collected in the same time span to avoid topical bias and were selected from the same set of Twitter users.


The entire corpus contains 4,792 tweets and is split into a set for training (80%) and testing (20%). Participants are free, however, to split the training set into a set for training and development.

<h5> Corpus cleaning</h5>
Prior to data annotation, the entire corpus was cleaned by removing retweets, duplicates and non-English tweets, and replacement of XML-escaped characters (e.g., &amp;). Emoji were converted to UTF-8 descriptions (e.g. :smiling_face:) for practical reasons related to the annotation of the dataset, but the original datasets (_emoji) are also available in this directory.

