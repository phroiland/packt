import re
from pyspark.streaming import StreamingContext
ssc = StreamingContext(sc, 30)
lines = ssc.socketTextStream(localhost, 9999)
wordcounts = lines.filter(lambda line: len(line) > 0) \
	.flatMap(lambda line: re.split(W+, line)) \
	.filter(lambda word: len(word) > 0) \
	.map(lambda word: (word.lower(), 1)) \
	.reduceByKey(lambda x, y: x + y)
wordcounts.pprint()
ssc.start()
ssc.awaitTermination()
import re
from pyspark.streaming import StreamingContext
