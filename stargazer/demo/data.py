# -*- coding: UTF-8 -*-

def _build_track_for_journey(journey):
    places = []
    for s in journey['stories']:
        if not len(places) or s['place'] != places[-1]:
            places.append(s['place'])
    return places
                
def _count_places_for_people(people):
    places = set()
    if 'journeys' in people:
        for j in people['journeys']:
            for s in j['stories']:
                places.add(s['place'])
    return len(places)

def _extract_stories_by_place(place, journeys):
    stories_by_date = {}
    for journey in journeys:
        for story in journey['stories']:
            if story['place'] == place:
                if story['date'] not in stories_by_date.keys():
                    stories_by_date[story['date']] = []
                stories_by_date[story['date']].append(story)
    
    stories_by_date_sorted = [(date, stories_by_date[date]) for date in sorted(stories_by_date.keys(), reverse=True)]
                
    return stories_by_date_sorted

owner = {
    'username': 'snowhs',
    'fullname': 'Snow Hellsing',
    'journey_count': 3,
    'place_count': 7,
    'story_count': 21
}

j_d_yunnan = {
    'title': '云南写生',   
    'abspath_full': '/journeys/v/1/yunnan/',           
    'stories': [
        {
            'title': '第一天在旅馆楼顶拍的星轨',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6492382943_ea2a32562a_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6492382943_ea2a32562a_b.jpg',
            'place': '大理',
            'date': '2011-10-15',
            'abspath_full': '/stories/v/k/long_lake/',
        },
        {
            'title': '日出后才起床的灰雁们',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6851869567_17f29f704d_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6851869567_17f29f704d_b.jpg',
            'place': '大理',
            'date': '2011-10-15',
            'abspath_full': '/stories/v/j/long_lake/',
        },
        {
            'title': '大理第一天感受',
            'text': '这是没有图片的故事的例子。乱七八糟的正文，乱七八糟的正文，乱七八糟的正文，乱七八糟的正文，乱七八糟的正文',
            'photos': [],
            'cover_uri': '',
            'place': '大理',
            'date': '2011-10-15',
            'abspath_full': '/stories/v/i/long_lake/',
        },
        {
            'title': '洱海的第一班游船',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6851868381_f8fe2c7452_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6851868381_f8fe2c7452_b.jpg',
            'place': '洱海',
            'date': '2011-10-16',
            'abspath_full': '/stories/v/h/long_lake/',
        },
        {
            'title': '古镇小院的老人',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6579084387_3f9eabcbeb_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6579084387_3f9eabcbeb_b.jpg',
            'place': '喜州古镇',
            'date': '2011-10-16',
            'abspath_full': '/stories/v/g/long_lake/',
        },
        {
            'title': '喜州古镇民居,大理',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6579083731_45552dfbd5_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6579083731_45552dfbd5_b.jpg',
            'place': '喜州古镇',
            'date': '2011-10-16',
            'abspath_full': '/stories/v/f/long_lake/',
        },
        {
            'title': '苍山索道旁的巨型棋盘',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6519832019_78ccc44608_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6519832019_78ccc44608_b.jpg',
            'place': '苍山',
            'date': '2011-10-17',
            'abspath_full': '/stories/v/e/long_lake/',
        },
        {
            'title': 'Three towers of the Chongsheng Temple, Dali',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6519831633_0f2551a900_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6519831633_0f2551a900_b.jpg',
            'place': '大理',
            'date': '2011-10-18',
            'abspath_full': '/stories/v/d/long_lake/',
        },
        {
            'title': 'trees near Longkan Wharf, Dali',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6519831409_bde48d6d1f_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6519831409_bde48d6d1f_b.jpg',
            'place': '大理',
            'date': '2011-10-18',
            'abspath_full': '/stories/v/c/long_lake/',
        },
        {
            'title': 'Waves, Erhai Lake, Dali',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6519830951_84252857e4_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6519830951_84252857e4_b.jpg',
            'place': '大理',
            'date': '2011-10-18',
            'abspath_full': '/stories/v/b/long_lake/',
        },
        {
            'title': '才村码头的鸬鹚/ Cormorant, Caicun Wharf, Dali',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6508752347_dd5982a357_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6508752347_dd5982a357_b.jpg',
            'place': '大理',
            'date': '2011-10-18',
            'abspath_full': '/stories/v/a/long_lake/',
        },
        {
            'title': '龙龛码头的鸟儿/ Bird walk on the Longkan Wharf,Dali',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6508750923_b8c316e959_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6508750923_b8c316e959_b.jpg',
            'place': '大理',
            'date': '2011-10-18',
            'abspath_full': '/stories/v/9/long_lake/',
        },
        {
            'title': 'flower on the Haishe Island',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6492389853_a9bf06b9c0_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6492389853_a9bf06b9c0_b.jpg',
            'place': '海蛇岛',
            'date': '2011-10-19',
            'abspath_full': '/stories/v/8/long_lake/',
        },
        {
            'title': 'Erhai Lake',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6492388527_673980781f_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6492388527_673980781f_b.jpg',
            'place': '洱海',
            'date': '2011-10-20',
            'abspath_full': '/stories/v/7/long_lake/',
        },
        {
            'title': 'Sunrise of Erhai Lake/洱海日出',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6492386783_3b08ca6351_b.jpg',
                       '/s/stargazer/demo/dragoncd/yunnan/6492381893_261849acd4_b.jpg',
                       '/s/stargazer/demo/dragoncd/yunnan/6492379021_68e052aa00_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6492386783_3b08ca6351_b.jpg',
            'place': '洱海',
            'date': '2011-10-20',
            'abspath_full': '/stories/v/6/long_lake/',
        },
        {
            'title': '苍山七龙池瀑布群，大理',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/yunnan/6492385047_f2eece2161_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/yunnan/6492385047_f2eece2161_b.jpg',
            'place': '大理',
            'date': '2011-10-21',
            'abspath_full': '/stories/v/5/long_lake/',
        },
    ]
}
j_d_yunnan['track'] = _build_track_for_journey(j_d_yunnan)
j_d_yunnan['cover_uri'] = j_d_yunnan['stories'][0]['cover_uri']

j_d_jiuzhai = {
    'title': '九寨沟',
    'abspath_full': '/journeys/v/2/jiuzhaigou',
    'stories': [
        {
            'title': '珍珠滩瀑布',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/jiuzhai/6191963417_3510fb7486_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/jiuzhai/6191963417_3510fb7486_b.jpg',
            'place': '珍珠滩瀑布',
            'date': '2011-9-7',
            'abspath_full': '/stories/v/4/long_lake/',
        },
        {
            'title': '树正瀑布',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/jiuzhai/6192455146_89107eb535_b.jpg',
                       '/s/stargazer/demo/dragoncd/jiuzhai/6191937001_780b7d7312_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/jiuzhai/6192455146_89107eb535_b.jpg',
            'place': '树正瀑布',
            'date': '2011-9-7',
            'abspath_full': '/stories/v/3/long_lake/',
        },
        {
            'title': '五花海/ Wuhua Lake , Jiuzhaigou Valley',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/jiuzhai/6192453290_799b270318_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/jiuzhai/6192453290_799b270318_b.jpg',
            'place': '五花海',
            'date': '2011-9-8',
            'abspath_full': '/stories/v/2/long_lake/',
        },
        {
            'title': '长海/ Long Lake , Jiuzhaigou Valley',
            'text': '',
            'photos': ['/s/stargazer/demo/dragoncd/jiuzhai/6191933951_6c517c8445_b.jpg'],
            'cover_uri': '/s/stargazer/demo/dragoncd/jiuzhai/6191933951_6c517c8445_b.jpg',
            'place': '长海',
            'date': '2011-9-8',
            'abspath_full': '/stories/v/1/long_lake/',
        },
    ]
}
j_d_jiuzhai['track'] = _build_track_for_journey(j_d_jiuzhai)

journey_list = [
    j_d_yunnan,
    j_d_jiuzhai,
]
    

people_drangoncd = {
    'username': 'dragoncd',
    'fullname': 'Confused Dragon',
    'avatar_uri': '/s/stargazer/demo/dragoncd/4117350631_4df43169db.jpg',
    'abspath_full': '/people/v/dragoncd/',
    'journeys': [j_d_yunnan, j_d_jiuzhai],              
}

people_drangoncd['journey_count'] = len(people_drangoncd['journeys'])
people_drangoncd['story_count'] = sum([len(j['stories']) for j in people_drangoncd['journeys']])
people_drangoncd['place_count'] = _count_places_for_people(people_drangoncd)

people_drangoncd['cover_uri'] = people_drangoncd['avatar_uri']
people_drangoncd['title'] = people_drangoncd['fullname']

# ---------
people_maklu = {
    'username': 'maklu',
    'fullname': '卢卫彬',
    'avatar_uri': '/s/stargazer/demo/maklu/5949576750_597801a57d_b.jpg',
    'abspath_full': '/people/v/maklu/',
    'journeys': [],              
}

people_maklu['journey_count'] = len(people_maklu['journeys'])
people_maklu['story_count'] = sum([len(j['stories']) for j in people_maklu['journeys']])
people_maklu['place_count'] = _count_places_for_people(people_maklu)

people_maklu['cover_uri'] = people_maklu['avatar_uri']
people_maklu['title'] = people_maklu['fullname']

#
# place
# ------
#
place_dali = {
    'name': '大理',
    'abspath_full': '/places/v/1/大理/',
    'stories_by_date': _extract_stories_by_place('大理', journey_list)
}
place_dali['story_count'] = sum([len(group[1]) for group in place_dali['stories_by_date']])

place_dali['cover_uri'] = place_dali['stories_by_date'][0][1][0]['cover_uri']
place_dali['title'] = place_dali['name']

#-------
place_erhai = {
    'name': '洱海',
    'abspath_full': '/places/v/2/洱海/',
    'stories_by_date': _extract_stories_by_place('洱海', journey_list)
}
place_erhai['story_count'] = sum([len(group[1]) for group in place_erhai['stories_by_date']])

place_erhai['cover_uri'] = place_erhai['stories_by_date'][0][1][0]['cover_uri']
place_erhai['title'] = place_erhai['name']

#
# context
# ------
#
journey_updates = []
for journey in journey_list:
    update = journey['stories'][-1]
    update['text'] += update['title'] + '\n' + 'updated: {}'.format(update['date'])
    update['title'] = journey['title']
    journey_updates.append(update)

context_data = {
    'owner': people_drangoncd,
    'journey_list': journey_list,
    'journey': j_d_yunnan,
    'place': place_dali,
    'story': j_d_yunnan['stories'][0],
    'journey_updates': journey_updates,
}

#all_bricks = j_d_yunnan['stories']
#all_bricks.extend(j_d_jiuzhai['stories'])
all_bricks = [people_drangoncd, place_dali, j_d_yunnan]
all_bricks.extend(j_d_jiuzhai['stories'])
all_bricks.extend([people_maklu, place_erhai])
all_bricks.extend(j_d_yunnan['stories'])

