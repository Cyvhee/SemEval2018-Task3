## Trial data ##

In this repository you will find the trial data for SemEval-2018 Task 3.

#### Task A ####
A tab-separated file with one line per tweet containing per line the tweet index, a binary classification label, and the tweet text.

Labels: **0** (non-ironic) and **1** (ironic)

#### Task B ####
A tab-separated file with one line per tweet containing per line the tweet index, a multiclass classification label, and the tweet text.

Labels: **1** (ironic by clash), **2** (other irony), **3** (situational irony), **4** (non-ironic)


#### Data details: ####
All tweets were collected using the [Twitter API](https://dev.twitter.com/rest/public) using the hashtags #irony, #sarcasm and #not. All tweets were collected between 01/12/2017 and 04/01/2015 and represent 2,676 unique users.
The tweets were manually labeled using a fine-grained annotation scheme for irony (Van Hee et al., 2016). Part of the tweets were manually annotated as non-ironic, and additional non-ironic tweets were collected from a background (i.e. randomly crawled) Twitter corpus to balance the corpus distribution.

Prior to data annotation, the entire corpus was cleaned by removing retweets, duplicates and non-English tweets, and replacement of XML-escaped characters (e.g., ```&amp;```). Emoji were converted to UTF-8 descriptions (e.g. :smiling\_face:) for practical reasons and by using the script emoji\_converter.py.