from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes   

trainDataFile = sc.textFile("/FileStore/tables/vrc38nzi1481400928302/trainNoStateType.txt") #without states and breach types

trainingSeparateTextAndLabel = trainDataFile.map(lambda x: x.split(":::"))

trainDict = trainingSeparateTextAndLabel.map(lambda x: {"text": x[0], "label": x[1]})
trainingList = []
for training in trainDict.collect():
  trainingList.append(training)
training_raw = sc.parallelize(trainingList)

# Split data into labels and features
labels = training_raw.map(
    lambda doc: doc["label"],  # Standard Python dict access 
    preservesPartitioning=True 
)

tf = HashingTF(numFeatures=60000).transform( 
    training_raw.map(lambda doc: doc["text"].split(), 
    preservesPartitioning=True))

idf = IDF(minDocFreq=1).fit(tf)
tfidf = idf.transform(tf)

# Combine using zip
training = labels.zip(tfidf).map(lambda x: LabeledPoint(x[0], x[1]))

# Train and check
model = NaiveBayes.train(training)
labels_and_preds = labels.zip(model.predict(tfidf)).map(
    lambda x: {"actual": float(x[0]), "predicted": float(x[1])})
accuracy = 1.0 * labels_and_preds.filter(lambda x: x['actual'] == x['predicted']).count() / labels_and_preds.count()
print('The Accuracy of prediction is: ' + str(accuracy))