
"""takes in number of clusters and data as [(x,y),(x,y),(x,y)...] returns as [a,b,c...]
where a, b,c stand for separate data cluster, each a = [(x,y),(x,y),(x,y)...]"""
def scikit_k_means(n_clusters,dataset):
	from sklearn.cluster import KMeans
	kmeans = KMeans(n_clusters=n_clusters)
	kmeans.fit(dataset)
	output =[[] for i in range(n_clusters)]
	labels = kmeans.labels_
	for index,label in enumerate(labels):
		output[label].append(dataset[index])
	return(output)

from sklearn.cluster import AffinityPropagation
def scikit_affinite_propagation(dataset):
	af = AffinityPropagation().fit(dataset)
	n_clusters=len(list(af.cluster_centers_indices_))
	output =[[] for i in range(n_clusters)]
	labels = af.labels_
	for index,label in enumerate(labels):
		output[label].append(dataset[index])
	return(output)
