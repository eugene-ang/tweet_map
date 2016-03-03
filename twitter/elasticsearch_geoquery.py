import requests
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

    # Good queries
    ##s = Search(using=es, index="tweets") \
    ##    .query("match_phrase", text="Carlo Maria Cordio") \
    ##s = Search(using=es, index="tweets") \
    ##    .query("match_all")
    #.filter("term", category="search") \
    #.query("match", title="python")   \
    #.query(~Q("match", description="beta"))
    #q = Q("match_phrase", text='popcornsex') & Q("match_phrase", text='Carlo Maria')
    #q = Q("match_phrase", ** {'user.description':'I watch horror'})
    #q = Q("match", ** {'place.full_name':'Tampa, FL'} )

def get_tweets_within_distance( lat_deg_dec , lon_deg_dec, thresh_dist_km ):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    s = Search(using=es, index="tweets")
    q = Q('bool',
            must=[Q('match_all')],
            filter= {'geo_distance' : {'distance': thresh_dist_km, 'location': {'lat':lat_deg_dec,'lon':lon_deg_dec}}}
        )
    s = s.query(q)
    response = s.execute()
    return response


if __name__ == '__main__':
    
    # Old development
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    s = Search(using=es, index="tweets")
    s = s.params(size=20)
    s = s.query("match_all")


    # Use this for the 10 words
    #q = Q("match_phrase", text='popcornsex') & Q("match_phrase", text='Carlo Maria')


    
    #q = Q('bool',
    #    must=[Q('match_all')],
    #    filter= {'geo_distance' : {'distance': threshold, 'location': {'lat':reflat,'lon':reflon}}}
    #)
    #s = s.query(q)
    print(s.to_dict())
    response = s.execute()
    print(response)
    for hit in response:
        try:
            print("score is: ", hit.meta.score)
            print(hit.name)
            print(hit.text)
            print(hit.location)
        except:
            continue

##    singapore = [1.5, 103.5]
##    nyc = [40.7127, -74.0059]
##    location = nyc
##
##    dist_threshold = '10km';
##    
##    response = get_tweets_within_distance( location[0], location[1], dist_threshold );
##    
##    for hit in response:
##        try:
##            print("score is: ", hit.meta.score)
##            print(hit.name)
##            print(hit.text)
##            print(hit.location)
##        except:
##            continue



    
