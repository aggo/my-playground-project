import matplotlib.pyplot as plt
# from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from fontTools.ttLib import TTFont


def run():
    font = TTFont('../../data/fonts_small/architextregular.ttf')
    print(font)

if __name__=="__main__":
    run()
