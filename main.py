from say.say_pyaudio import twelve_english_out,process_english

part_Leisure={
    'Cinema':[
        'cinema;電影院','documentary;紀錄片','film;電影','flick;電影',
        'image;影像','movie;電影','producer;製造者','project;計畫',
        'projection;計畫','screen;螢幕','shot;鏡頭','thriller;恐怖片'
    ],
    'Exercise':[
        'ace;一流的','aim;目標','arena;競技場','athlete;運動員','athletic;運動的',
        'badminton;羽毛球','ballet;芭蕾','basketball;籃球','bout;一回合','bowling;保齡球'
        ,'boxer;拳擊手','boxing;拳擊','challenge;挑戰','champion;冠軍','championship;冠軍賽'
        ,'cheer;喝采','climb;攀爬','coach;教練','dance;跳舞','dancer;舞者'
        ,'defend;防禦','defensive;防禦的','dive;跳水','divide;分歧','exercise;運動'
        ,'fight;戰鬥','fighter;戰士','final;最終的','football;足球','foul;犯規'
        ,'goal;目標','golf;高爾夫','gym;健身房','hockey;曲棍球','hole;洞'
        ,'hurdle;障礙物','jog;慢跑','league;聯盟','locker;置物櫃','marathon;馬拉松'
        ,'match;相配','medal;獎章','net;網子','offense;進攻','offensive;進攻的'
        ,'opponent;對手','ping-pong;桌球','pitcher;投手','player;運動員','playgroud;運動場'
        ,'point;得分','position;位置','practice;練習','race;賽跑','rally;集合'
        ,'referee;裁判','relay;傳達','rival;對手','rivalry;競爭','run;跑步'
        ,'runner;跑者','score;分數','skate;溜冰鞋','ski;滑雪板','snare;陷阱'
        ,'soccer;足球','spectator;觀眾','sponsor;贊助者','sport;運動','sportsman;運動員'
        ,'sportsmanship;運動道德','sprint;衝刺','stadium;室內運動場','strike;罷工','surf;衝浪'
        ,'swim;游泳','team;隊伍','tennis;網球','throw;投擲','tournament;競賽'
        ,'trophy;戰利品','tug-of-war;拔河','umpire;裁判','volleyball;排球','wrestle;摔角'
        ,'yoga;瑜珈'
    ],
    'baseball': [
        'base;壘包','baseball;棒球','bat;球棒','batter;打擊手','catch;捕捉'
    ],
    'gardening':[
        'garden;花園','gardener;園丁','greenhouse;溫室','hedge;籬笆','hose;水管',
        'landscape;風景','lawn;草地','prune;修剪','spade;鏟子',
    ],
    'entertainment':[
        'bet;打賭','bingo;賓果遊戲','chess;西洋棋','doll;洋娃娃','firecracker;鞭炮',
        'gamble;賭博','game;遊戲','kite;風箏','lottery;樂透','odds;勝算',
        'pastime;消遣','play;遊戲','prize;獎品','puppet;木偶','puzzle;難題',
        'relish;嗜好','riddle;謎語','seesaw;翹翹班','token;代幣','toy;玩具',
        'trick;戲法'
    ],
    'outdoor_activities':[
        'backpack;背包','barbecue;燒烤','booth;攤子','camp;露營','charcoal;炭',
        'compass;羅盤','fisherman;漁夫','hike;遠足','outdoor;戶外的','outdoors;在戶外',
        'parade;遊行','park;公園','tent;帳篷','torch;火炬'
    ],
    'leisure':[
        'album;相簿','amusement;娛樂','aquarium;水族館','ball;球',
        'banquet;宴會','card;卡片','carnival;嘉年華','cassette;卡帶',
        'compact disk;CD','celebrate;慶祝','celebration;慶祝','center;中央',
        'circus;馬戲團','club;俱樂部','disco;舞廳','divert;逗...開心',
        'fad;一時流行','holiday;假期','idol;偶像','leisure;空閒',
        'leisurely;悠閒的','lounge;交誼廳','massage;按摩','outing;郊遊',
        'party;派對','picnic;野餐','pub;酒館','recreation;娛樂',
        'recreational;娛樂的','saloon;酒吧','vacation;假期'
    ],
    'tour':[
        'baggage;行李','check-in;報到','check-out;結帳離開','guide;嚮導',
        'hostel;青年旅社','hotel;旅館','inn;旅社','motel;汽車旅館',
        'sightseeing;觀光','souvenir;紀念品','journey;旅程','passport;護照',
        'suitcase;手提箱','suite;套房','tour;旅行','tourism;觀光',
        'tourist;觀光客','travel;旅遊','traveler;旅行者','trip;旅行',
        'visa;簽證','visit;參觀','visitor;訪客','voyage;航行',
    ],
    'art':[
        'art;藝術','artifact;手工藝品','artist;藝術家','artistic;藝術的',
        'bronze;青銅','calligraphy;書法','ceramic;陶瓷器','classic;經典',
        'classical;古典的','clay;黏土','contemporary;當代的','craft;手工藝',
        'creative;有創造力的','critic;批評家','critical;評論的','criticism;批評',
        'criticize;批評','exhibit;展示品','exhibition;展覽','express;快遞',
        'expression;表達','handicraft;手工藝品','masterpiece;傑作','muse;沉思',
        'museum;博物館','piece;作品','potery;陶器','realism;現實主義',
        'renaissance;文藝復興','sculptor;雕刻家','sculpture;雕刻','statue;雕像',
        'studio;工作室','style;風格',
    ],
}


if __name__ == '__main__':
    for i in list(part_Leisure):
        value=part_Leisure[i]
        twelve_english_out(value)