import json

sample_str = r'{"created_at":"Mon Feb 29 01:26:23 +0000 2016","id":704115467498201090,"id_str":"704115467498201090","text":"Bella simpleza de #RachelMcAdams Excelente papel en la pel\u00edcula #Spotlight . Recomendable!!! #JuradoTRESemm\u00e9 https:\/\/t.co\/ncjxDBQABc","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":205296675,"id_str":"205296675","name":"Victoria Zangaro","screen_name":"vzangaro","location":"Montevideo, Uruguay","url":null,"description":null,"protected":false,"verified":false,"followers_count":13087,"friends_count":753,"listed_count":48,"favourites_count":3286,"statuses_count":3003,"created_at":"Wed Oct 20 15:11:21 +0000 2010","utc_offset":-10800,"time_zone":"Greenland","geo_enabled":true,"lang":"es","contributors_enabled":false,"is_translator":false,"profile_background_color":"DBE9ED","profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/384577272\/ps.png","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/384577272\/ps.png","profile_background_tile":true,"profile_link_color":"CC3366","profile_sidebar_border_color":"DBE9ED","profile_sidebar_fill_color":"E6F6F9","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/703948437365104640\/dADptMtT_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/703948437365104640\/dADptMtT_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/205296675\/1449279978","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":{"id":"01a9dbb9232f0fac","url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/01a9dbb9232f0fac.json","place_type":"admin","name":"Montevideo","full_name":"Montevideo, Uruguay","country_code":"UY","country":"Uruguay","bounding_box":{"type":"Polygon","coordinates":[[[-56.430439,-34.937896],[-56.430439,-34.701599],[-56.029341,-34.701599],[-56.029341,-34.937896]]]},"attributes":{}},"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[{"text":"RachelMcAdams","indices":[18,32]},{"text":"Spotlight","indices":[64,74]},{"text":"JuradoTRESemm\u00e9","indices":[93,108]}],"urls":[],"user_mentions":[],"symbols":[],"media":[{"id":704115457192824835,"id_str":"704115457192824835","indices":[109,132],"media_url":"http:\/\/pbs.twimg.com\/media\/CcWFRxrXEAM_qWw.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/CcWFRxrXEAM_qWw.jpg","url":"https:\/\/t.co\/ncjxDBQABc","display_url":"pic.twitter.com\/ncjxDBQABc","expanded_url":"http:\/\/twitter.com\/vzangaro\/status\/704115467498201090\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":968,"h":1200,"resize":"fit"},"medium":{"w":600,"h":744,"resize":"fit"},"small":{"w":340,"h":421,"resize":"fit"}}}]},"extended_entities":{"media":[{"id":704115457192824835,"id_str":"704115457192824835","indices":[109,132],"media_url":"http:\/\/pbs.twimg.com\/media\/CcWFRxrXEAM_qWw.jpg","media_url_https":"https:\/\/pbs.twimg.com\/media\/CcWFRxrXEAM_qWw.jpg","url":"https:\/\/t.co\/ncjxDBQABc","display_url":"pic.twitter.com\/ncjxDBQABc","expanded_url":"http:\/\/twitter.com\/vzangaro\/status\/704115467498201090\/photo\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":968,"h":1200,"resize":"fit"},"medium":{"w":600,"h":744,"resize":"fit"},"small":{"w":340,"h":421,"resize":"fit"}}}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"es","timestamp_ms":"1456709183941"}'

i = sample_str.find('\"geo\"')
j = sample_str.find('"geo":null')
print(i, " ", j)

loadedjson = json.loads(sample_str)

print('name: ', loadedjson['user']['name'])
print('text: ', loadedjson['text'])
print('place: ', loadedjson['place'])
print('geo:', loadedjson['geo'])

coords = loadedjson['place']['bounding_box']['coordinates'][0]
print('coords[0]: ', coords[0])
print('coords[1]: ', coords[1])
print('coords[2]: ', coords[2])
print('coords[3]: ', coords[3])

print('geo == None: ', loadedjson['geo'] == None)

print('date: ', loadedjson['created_at'])

