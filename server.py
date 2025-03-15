#Zoe Hightower
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = [
    {
        "id": "1",
        "name": "The Strokes",
        "description": "The Strokes are an American rock band formed in 1998, known for their role in reviving garage rock and post-punk revival. Their debut album, Is This It (2001), became an influential indie rock record, featuring raw guitar riffs and Julian Casablancas' unique vocals. The band’s sound blends lo-fi aesthetics with modern rock influences, earning them both critical acclaim and a dedicated fan base. Over the years, they have continued to shape the indie rock scene with albums like Room on Fire and The New Abnormal. Iconic tracks like Last Nite and Reptilia have solidified their place in music history.",
        "popular albums": [
            {
                "album": "Room On Fire",
                "cover": "https://upload.wikimedia.org/wikipedia/en/9/9f/Room_on_Fire_cover.jpg",
                "songs": ["What Ever Happened?",
                           "Reptilia",
                           "Automatic Stop",
                           "12:51",
                           "You Talk Way Too Much",
                           "Between Love & Hate",
                           "Meet Me in the Bathroom",
                           "Under Control",
                           "The Way It Is",
                           "The End Has No End",
                           "I Can't Win"
                        ]
            },
            {
                "album": "The New Abnormal",
                "cover": "https://upload.wikimedia.org/wikipedia/en/f/f8/The_Strokes_-_The_New_Abnormal.png",
                "songs": ["The Adults Are Talking",
                           "Selfless",
                           "Brooklyn Bridge To Chorus",
                           "Bad Decisions",
                           "Eternal Summer",
                           "At The Door",
                           "Why Are Sundays So Depressing",
                           "Not The Same Anymore",
                           "Ode To The Mets"
                        ]
            }
        ],
        "monthly listeners": "13,974,550",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/The_Strokes_by_Roger_Woolman.jpg/1200px-The_Strokes_by_Roger_Woolman.jpg",
        "similar artists": ["Franz Ferdinand", "Arctic Monkeys", "Cage the Elephant", "Radiohead"],
        "subgenres": ["Alternative Rock", "New Wave", "Garage Rock", "Post-Punk Revival", "New York City Indie"],
        "members":["Julian Casablancas", "Fabrizio Moretti", "Nick Valensi", "Nikolai Fraiture", "Albert Hammond Jr."]
    },
    {
        "id": "2",
        "name": "Radiohead",
        "description": "Radiohead is an English rock band formed in 1985, known for their experimental approach to music and deeply introspective lyrics. Their breakthrough album, OK Computer (1997), redefined alternative rock with its atmospheric soundscapes and dystopian themes. The band continued to push boundaries with albums like Kid A and In Rainbows, blending electronic elements, unconventional song structures, and Thom Yorke’s haunting vocals. With iconic tracks such as Creep, Paranoid Android, and No Surprises, Radiohead has cemented their legacy as one of the most innovative and influential bands in modern music.",
        "popular albums": [
            {
                "album": "OK Computer",
                "cover": "https://upload.wikimedia.org/wikipedia/en/b/ba/Radioheadokcomputer.png",
                "songs": ["Airbag",
                           "Parnoid Android",
                           "Subterranean Homesick Alien",
                           "Exit Music (For A Film)",
                           "Let Down",
                           "Karma Police",
                           "Fitter Happier",
                           "Electioneering",
                           "Climbing Up the Walls",
                           "No Surprises",
                           "Lucky",
                           "The Tourist"
                        ]
            },
            {
                "album": "The Bends",
                "cover": "https://upload.wikimedia.org/wikipedia/en/5/55/Radioheadthebends.png",
                "songs": ["Planet Telex",
                           "The Bends",
                           "High and Dry",
                           "Fake Plastic Trees",
                           "Bones",
                           "(Nice Dream)",
                           "Just",
                           "My Iron Lung",
                           "Bullet Proof...I Wish I Was",
                           "Black Star",
                           "Sulk",
                           "Street Spirit (Fade Out)"
                        ]
            }

        ],
        "monthly listeners": "31,065,305",
        "image": "https://i8.amplience.net/i/naras/radiohead_MI0003519538-MN0000326249",
        "similar artists": ["The Smiths", "Joy Division", "The Cure", "Pixies", "The Strokes"],
        "subgenres": ["Alternative Rock", "Art Rock", "Experimental Rock", "Electronica", "Progressive Rock", "Britpop"],
        "members":["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Philip Selway", "Clive Deamer", "Ed O'Brien"]
    },
    {
        "id": "3",
        "name": "Franz Ferdinand",
        "description": "Franz Ferdinand is a Scottish rock band formed in 2002, known for their energetic blend of indie rock, post-punk revival, and dance-punk. Their self-titled debut album, released in 2004, featured infectious guitar hooks and catchy rhythms, leading to major success. Their sound is marked by angular guitars, driving basslines, and charismatic vocals by Alex Kapranos. Over the years, they have released critically acclaimed albums such as You Could Have It So Much Better and Tonight: Franz Ferdinand, with tracks like Take Me Out and Do You Want To becoming anthems of the 2000s indie scene. Their music continues to evolve, embracing electronic and experimental influences.",
        "popular albums": [
            {
                "album": "Franz Ferdinand",
                "cover": "https://upload.wikimedia.org/wikipedia/commons/8/87/%22Franz_Ferdinand%22_%282004%29%2C_by_Franz_Ferdinand.png",
                "songs": ["Jacqueline",
                           "Tell Her Tonight",
                           "Take Me Out",
                           "The Dark Of The Matinée",
                           "Auf Achse",
                           "Cheating On You",
                           "This Fire",
                           "Darts Of Pleasure",
                           "Michael",
                           "Come On Home",
                           "40'"
                        ]
            },
            {
                "album": "You Could Have It So Much Better",
                "cover": "https://upload.wikimedia.org/wikipedia/en/thumb/3/38/You_Could_Have_It_So_Much_Better_%28Franz_Ferdinand_album_-_cover_art%29.png/220px-You_Could_Have_It_So_Much_Better_%28Franz_Ferdinand_album_-_cover_art%29.png",
                "songs": ["The Fallen",
                           "Do You Want To",
                           "This Boy",
                           "Walk Away",
                           "Evil And A Heathen",
                           "You're The Reason I'm Leaving",
                           "Eleanor Put Your Boots On",
                           "Well That Was Easy",
                           "What You Meant",
                           "I'm Your Villain",
                           "You Could Have It So Much Better", 
                           "Fade Together",
                           "Outsiders"
                        ]
            }
        ],
        "monthly listeners": "8,806,991",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRutaKkWHAHR_zez2RiFh-7gjUTkeydpT2z9A&s",
        "similar artists": ["The Strokes", "Pixies", "Cage the Elephant", "Arctic Monkeys"],
        "subgenres": ["Alternative Rock","Post-Punk Revival", "Dance-Punk", "New Wave"],
        "members":["Alex Kapranos", "Audrey Tait", "Miaoux Miaoux", "Bob Hardy", "Dino Bardot", "Nick McCarthy", "Paul Thomson"]
   },
   {
        "id": "4",
        "name": "Arctic Monkeys",
        "description": "Arctic Monkeys are a British rock band formed in Sheffield in 2002. Known for their sharp lyrics, energetic guitar riffs, and evolving sound, they quickly rose to fame with their debut album, Whatever People Say I Am, That's What I'm Not (2006), which became the fastest-selling debut album in UK history at the time. Over the years, their music has transitioned from indie rock and post-punk revival to more experimental and atmospheric styles, as heard in albums like AM (2013) and Tranquility Base Hotel & Casino (2018). Frontman Alex Turner's distinctive voice and poetic songwriting have been central to their success, making them one of the most influential bands of the 21st century.",
        "popular albums": [
            {
                "album": "AM",
                "cover": "https://upload.wikimedia.org/wikipedia/commons/e/e7/%22AM%22_%28Arctic_Monkeys%29.jpg",
                "songs": ["Do I Wanna Know?",
                           "R U Mine?",
                           "One For The Road",
                           "I Want It All",
                           "No.1 Party Anthem",
                           "Mad Sounds",
                           "Fireside",
                           "Why'd You Only Call Me When You're High?",
                           "Snap Out Of It",
                           "Knee Socks",
                           "I Wanna Be Yours"
                        ]
            },
            {
                "album": "Favourite Worst Nightmare",
                "cover": "https://upload.wikimedia.org/wikipedia/en/a/ae/Favourite_Worst_Nightmare.jpg",
                "songs": ["Brianstorm",
                           "Teddy Picker",
                           "D Is for Dangerous",
                           "Balaclava",
                           "Fluorescent Adolescent",
                           "Only Ones Who Know",
                           "Do Me a Favour",
                           "This House Is a Circus",
                           "If You Were There, Beware",
                           "The Bad Thing",
                           "Old Yellow Bricks",
                           "505"
                        ]
            }
        ],
        "monthly listeners": "52,888,301",
        "image": "https://i.scdn.co/image/ab6761610000e5eb7da39dea0a72f581535fb11f",
        "similar artists": ["The Strokes","Franz Ferdinand","Radiohead", "Cage the Elephant"],
        "subgenres": ["Alternative Rock","Britpop", "Post-Punk Revival", "New Wave", "Indie Rock"],
        "members":["Alex Turner","Matt Helders", "Jamie Cook", "Nick O'Malley", "Andy Nicholson"]
   },
   {
        "id": "5",
        "name": "Cage the Elephant",
        "description": "Cage the Elephant is an American rock band known for their eclectic sound, blending elements of alternative rock, indie rock, and garage rock with influences of blues, punk, and psychedelia. Formed in 2006 in Bowling Green, Kentucky, the band gained attention with their energetic performances and distinct sound, led by the charismatic and raspy voice of lead singer Matt Shultz. Their breakout hit, Ain't No Rest for the Wicked, helped establish their place in modern rock music, and they continued to experiment with their sound on albums like Melophobia and Tell Me I'm Pretty. Known for their dynamic live shows, Cage the Elephant is recognized for their ability to blend raw emotion with a genre-defying mix of musical styles.",
        "popular albums": [
            {
                "album": "Melophobia",
                "cover": "https://upload.wikimedia.org/wikipedia/en/1/1e/Cage_the_Elephant_Melophobia.jpg",
                "songs": ["Spiderhead",
                           "Come a Little Closer",
                           "Telescope",
                           "It's just Forever (feat. Alison Mosshart)",
                           "Take It or Leave It",
                           "Halo",
                           "Black Widow",
                           "Hypocrite",
                           "Teeth",
                           "Cigarette Daydreams"
                        ]
            },
            {
                "album": "Tell Me I'm Pretty",
                "cover": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Cage_the_Elephant_-_Tell_Me_I%27m_Pretty.png/220px-Cage_the_Elephant_-_Tell_Me_I%27m_Pretty.png",
                "songs": ["Cry Baby",
                           "Mess Around",
                           "Sweetie Little Jean",
                           "Too Late To Say Goodbye",
                           "Cold Cold Cold",
                           "Trouble",
                           "How Are You True",
                           "That's Right",
                           "Punchin' Bag",
                           "Portuguese Knife Fight",
                        ]
            }
        ],
        "monthly listeners": "15,737,814",
        "image": "https://static01.nyt.com/images/2024/06/19/multimedia/19cage-elephant-03-zhfk/19cage-elephant-03-zhfk-mediumSquareAt3X.jpg",
        "similar artists": ["The Strokes", "Arctic Monkeys","Franz Ferdinand", "Pixies"],
        "subgenres": ["Indie Rock", "Alternative Rock", "Garage Rock", "New Wave", "Psychedelic Rock"],
        "members":["Matt Shultz", "Brad Shults", "Lincoln Parish", "Jared Champion", "Daniel Tichenor", "Nick Bockrath", "Matthan Minster"]
   },
   {
        "id": "6",
        "name": "The Smiths",
        "description": "The Smiths were an influential British indie rock band formed in 1982, known for their melancholic yet catchy sound. Their music often blends jangly guitars, introspective lyrics, and the distinct voice of frontman Morrissey. Lyrically, their songs explore themes of alienation, longing, and social commentary, with a unique mix of wit and sorrow. Despite their relatively short career, with the band breaking up in 1987, The Smiths left a lasting impact on the indie and alternative music scenes, shaping the sound of the '80s and beyond.",
        "popular albums": [
            {
                "album": "Hatful of Hollow",
                "cover": "https://upload.wikimedia.org/wikipedia/en/1/15/HatfulofHollow84.jpg",
                "songs": ["William, It Was Really Nothing",
                           "What Difference Does It Make?",
                           "These Things Take Time",
                           "This Charming Man",
                           "How Soon Is Now?",
                           "Handsome Devil",
                           "Hand in Glove",
                           "Still III",
                           "Heaven Knows I'm Miserable Now",
                           "This Night Has Opened My Eyes",
                           "You've Got Everything Now",
                           "Accept Yourself",
                           "Girl Afraid",
                           "Back to the Old House",
                           "Reel Around the Fountain",
                           "Please, Please, Please, Let Me Get What I Want"
                        ]
            },
            {
                "album": "The Queen Is Dead",
                "cover": "https://upload.wikimedia.org/wikipedia/en/e/ed/The-Queen-is-Dead-cover.png",
                "songs": ["The Queen Is Dead",
                           "Frankly, Mr.Shankly",
                           "I Know It's Over",
                           "Never Had No One Ever",
                           "Cemetry Gates",
                           "Bigmouth Strikes Again",
                           "The Boy with the Thorn in His Side",
                           "Vicar in a Tutu",
                           "There Is a Light That Never Goes Out",
                           "Some Girls Are Bigger Than Others",
                        ]
            }
        ],
        "monthly listeners": "17,083,052",
        "image": "https://i.discogs.com/xrt_A--gs_-MeiYYQzcKYPLd1Wz_ksMRf30FzNKbDQw/rs:fit/g:sm/q:40/h:300/w:300/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTgzMDgw/LTEzMTkzNzgzNTgu/anBlZw.jpeg",
        "similar artists": ["The Cure", "The Cranberries", "Radiohead", "Joy Division","Pixies"],
        "subgenres": ["Britpop", "Alternative Rock", "Art Rock", "Post-Punk Revival"],
        "members":["Morrissery", "Johnny Marr", "Andy Rourke", "Mike Joyce", "Ivor Perry", "Dale Hibbert", "Craig Gannon"]
   },
   {
        "id": "7",
        "name": "The Cranberries",
        "description": "The Cranberries were an Irish rock band formed in Limerick in 1989, known for their distinct blend of alternative rock and post-punk influences. The band gained international fame in the 1990s with their hit songs like 'Zombie,' 'Linger,' and 'Dreams,' led by the powerful and emotive vocals of Dolores O'Riordan. Their sound was marked by catchy melodies, deep lyrics, and O'Riordan's unique vocal style, often combining themes of love, loss, and political strife. The band remained active for several decades, with their music continuing to resonate with fans worldwide until O'Riordan's tragic passing in 2018.",
        "popular albums": [
            {
                "album": "Everybody Else Is Doing It, So Why Can't We?",
                "cover": "https://upload.wikimedia.org/wikipedia/en/d/db/Everybody_Else_Is_Doing_It%2C_So_Why_Can%27t_We%3F.webp",
                "songs": ["I Still Do",
                           "Dreams",
                           "Sunday",
                           "Pretty",
                           "Waltzing Back",
                           "Not Sorry",
                           "Linger",
                           "Wanted",
                           "Still Can't...",
                           "I Will Always",
                           "How",
                           "Put Me Down"
                        ]
            },
            {
                "album": "No Need To Argue",
                "cover": "https://upload.wikimedia.org/wikipedia/en/2/2c/CranberriesNoNeedToArgueAlbumcover.jpg",
                "songs": ["Ode to My Family", 
                          "I Can't Be with You",
                          "Twenty One",
                          "Zombie",
                          "Empty",
                          "Everything I Said",
                          "The Icicle Melts",
                          "Disappointment",
                          "Ridiculous Thoughts",
                          "Dreaming My Dreams",
                          "Yeats' Grave",
                          "Daffodil Lament",
                          "No Need To Argue",
                          "Away",
                          "I Don't Need",
                          "(They Long To Be)Close To You",
                          "So Cold In Ireland"
                        ]
            }
        ],
        "monthly listeners": "24,745,476",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/db/Everybody_Else_Is_Doing_It%2C_So_Why_Can%27t_We%3F.webp",
        "similar artists": ["Pixies", "Joy Division", "Radiohead", "The Smiths"],
        "subgenres": ["Alternative Rock", "Post-Punk Revival", "Dream Pop", "Art Rock"],
        "members":["Dolores O'Riordan", "Niall Quinn", "Fergal Lawler", "Noel Hogan", "Steve DeMarchi", "Michael Gerord Hogan"]
   },
   {
        "id": "8",
        "name": "Joy Division",
        "description": "Joy Division was an English post-punk band formed in 1976, known for their moody and atmospheric sound. Their music blends elements of punk rock with darker, more introspective themes, often exploring alienation, despair, and existential dread. Led by Ian Curtis, whose haunting, baritone vocals became a defining characteristic, the band's music remains influential in both post-punk and new wave genres. Despite their brief career, Joy Division’s legacy continues to resonate, particularly with albums like Unknown Pleasures and Closer, both of which are considered landmarks of the era.",
        "popular albums": [
            {
                "album": "Love Will Tear Us Apart",
                "cover": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9d/Love_will_tear_us_apart.jpg/220px-Love_will_tear_us_apart.jpg",
                "songs": ["Love Will Tear Us Apart"]
            },
            {
                "album": "Unknown Pleasures",
                "cover": "https://upload.wikimedia.org/wikipedia/en/5/5a/UnknownPleasuresVinyl.jpg",
                "songs": ["Disorder", 
                          "Day of the Lords",
                          "Candidate",
                          "Insight",
                          "New Dawn Fades",
                          "She's Lost Control",
                          "Shadowplay",
                          "Wilderness",
                          "Interzone",
                          "I Remember Nothing"
                        ]
            }
        ],
        "monthly listeners": "3,894,473",
        "image": "https://i.discogs.com/Y_xL1AURupXtJ7rPvoZiUg7hEFqDK-Z-9-dqBvVnqyw/rs:fit/g:sm/q:40/h:300/w:300/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM4OTgt/MTMxOTM1OTY4Mi5q/cGVn.jpeg",
        "similar artists": ["The Smiths", "The Cure", "Radiohead", "The Cranberries"],
        "subgenres": ["Dream Pop", "Post-Punk Revival", "Britpop","Alternative Rock","Art Rock"],
        "members":["Ian Curtis", "Peter Hook", "Bernard Sumner", "Stephen Morris"]
   },
   {
        "id": "9",
        "name": "The Cure",
        "description": "The Cure is a British rock band formed in 1976, known for their distinctive sound that blends post-punk, new wave, and alternative rock. Fronted by Robert Smith, the band's music often features moody, atmospheric compositions with introspective lyrics, ranging from melancholic to whimsical. Throughout their career, The Cure has experimented with various styles, producing iconic albums like Seventeen Seconds, The Head on the Door, and Wish. Their ability to evolve while maintaining a unique identity has earned them a lasting influence in the music world and a dedicated fanbase.",
        "popular albums": [
            {
                "album": "Wish",
                "cover": "https://upload.wikimedia.org/wikipedia/en/2/2b/TheCureWish.jpg",
                "songs": ["Open",
                           "High",
                           "Apart",
                           "From the Edge of the Deep Green Sea",
                           "Wendy Time",
                           "Doing the Unstuck",
                           "Friday I'm in Love",
                           "Trust",
                           "A Letter to Elise",
                           "Cut",
                           "To Wish Impossible Things",
                           "End"
                        ]
            },
            {
                "album": "Three Imaginary Boys",
                "cover": "https://upload.wikimedia.org/wikipedia/en/1/18/TheCureThreeImaginaryBoysalbumcover.jpg",
                "songs": ["10:15 Saturday Night",
                          "Accuracy",
                          "Grinding Halt",
                          "Another Day",
                          "Object",
                          "Subway Song",
                          "Foxy Lady",
                          "Meat Hook",
                          "So What",
                          "Fire in Cairo",
                          "It's Not You",
                          "Three Imaginary Boys",
                          "The Weedy Burton"
                        ]
            }
        ],
        "monthly listeners": "17,108,150",
        "image": "https://lh3.googleusercontent.com/zgxx9xJI-x-brHQKRONelnaAEklEkq4pShEJ5Eq19yhWxOwfuiyoR_YpzcPZ_ckimGO2syALRh5MWvQ=w544-h544-p-l90-rj",
        "similar artists": ["The Smiths", "Radiohead","Joy Division"],
        "subgenres": ["New Wave", "Alternative Rock","Post-Punk Revival", "Britpop", "Experimental Rock"],
        "members":["Robert Smith", "Michael Dempsey", "Lol Tolhurst", "Matthieu Hartley", "Simon Gallup", "Andy Anderson", "Phil Thornalley", "Boris Williams", "Porl Thompson", "Roger O'Donnell", "Perry Bamonte", "Jason Cooper", "Reeves Gabrels"]
   },
   {
        "id": "10",
        "name": "Pixies",
        "description": "The Pixies are an American alternative rock band formed in 1986 in Boston. Known for their dynamic blend of quiet-loud song structures and surreal, often cryptic lyrics, they became a major influence on the 1990s indie rock scene. Their sound combines elements of punk rock, surf rock, and noise rock, with the distinctive falsetto vocals of Black Francis and the ethereal harmonies of Kim Deal. The band gained a cult following with albums like Surfer Rosa and Doolittle, whose tracks like 'Where Is My Mind?' and 'Debaser' are considered iconic in alternative music history.",
        "popular albums": [
            {
                "album": "Doolittle",
                "cover": "https://upload.wikimedia.org/wikipedia/en/6/6b/Pixies-Doolittle.jpg",
                "songs": ["Debaser",
                          "Tame",
                          "Wave of Mutilation",
                          "I Bleed",
                          "Here Comes Your Man",
                          "Dead",
                          "Monkey Gone to Heaven",
                          "Mr. Grieves",
                          "Crackity Jones",
                          "La La Love You",
                          "No. 13 Baby",
                          "There Goes My Gun",
                          "Hey",
                          "Silver",
                          "Gouge Away"
                        ]
            },
            {
                "album": "Surfer Rosa",
                "cover": "https://upload.wikimedia.org/wikipedia/en/2/2c/CranberriesNoNeedToArgueAlbumcover.jpg",
                "songs": ["Bone Machine",
                          "Break My Body",
                          "Something Against You",
                          "Broken Face",
                          "Gigantic",
                          "River Euphrates",
                          "Where Is My Mind?",
                          "Cactus",
                          "Tony's Theme",
                          "Oh My Golly!",
                          "Vamos",
                          "I'm Amazed",
                          "Brick Is Red"
                        ]
            }
        ],
        "monthly listeners": "9,171,935",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp6ymCGsjZEm3LisoKOji-aPpKuuzOHL9zyQ&s",
        "similar artists": ["Radiohead", "The Cranberries", "The Smiths", "Cage the Elephant", "Franz Ferdinand"],
        "subgenres": ["Alternative Rock", "Post-Punk Revival", "New Wave", "Garage Rock"],
        "members":["Black Francis", "Joey Santiago", "David Lovering", "Kim Deal", "Paz Lenchantin", "Kim Shattuck", "Simon Archer"]
   },
]

#can change dynamically with different ids
favorites=["1","2","6"]

#homepage
@app.route('/')
def home_page():
   return render_template('homepage.html', favorites=favorites, data=data) 

#viewing a band page
@app.route('/view/<id>')
def view_page(id):
    global data 
    for band in data:
        if band["id"] == id:
            return render_template('bandpage.html', band=band, data=data) 
    return "Band not found", 404


#search results page
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('search_field', '').strip().lower()
    
    if query:
        results = [
            band for band in data if (
                query in band["name"].lower() or
                any(query in member.lower() for member in band["members"]) or
                any(query in subgenre.lower() for subgenre in band["subgenres"])
            )
        ]

        result_count = len(results)

        return render_template('index.html', query=query, results=results, result_count=result_count)
    
    return render_template('homepage.html', favorites=[], data=data)

#page of a specifc genre
@app.route('/genres/<query>', methods=['GET'])
def genre_search(query):
    
    results = [band for band in data if any(query.lower() in subgenre.lower() for subgenre in band["subgenres"])]
    result_count = len(results)
    return render_template('index.html', query=query, results=results, result_count=result_count)

#page of a specific members bands
@app.route('/members/<query>', methods=['GET'])
def member_search(query):
    
    results = [band for band in data if any(query.lower() in member.lower() for member in band["members"])]
    result_count = len(results)
    return render_template('index.html', query=query, results=results, result_count=result_count)
    
#sends user to adding page
@app.route('/add')
def add_entry():
    bands = [band["name"] for band in data]
    genres = list(set(subgenre for band in data for subgenre in band.get("subgenres", [])))
    return render_template('add.html', bands=bands, genres=genres, data=data)

#sends user to editing page
@app.route('/edit/<id>')
def edit(id):
    global data 
    bands = [band["name"] for band in data]
    genres = list(set(subgenre for band in data for subgenre in band.get("subgenres", [])))
    for band in data:
        if band["id"] == id:
            similar = band.get("similar artists", [])
            subgenres = band.get("subgenres", [])
            return render_template('edit.html', band=band, data=data, bands=bands, genres=genres, similar=similar, subgenres=subgenres)

#editing and adding 
@app.route('/edit/edit_entry', methods=['POST'])
def edit_entry():
    global data
    
    json_data = request.get_json()
    entry = json_data[0]
    
    is_new_band = False
    old_name = None
    old_similar_artists = []

    # Check if editing an existing band and if so deletes it 
    if entry["id"] and any(item["id"] == entry["id"] for item in data):
        for i, item in enumerate(data):
            if item["id"] == entry["id"]:
                old_name = item["name"]
                old_similar_artists = item.get("similar artists", []).copy()
                data.pop(i)
                break
    else:
        is_new_band = True
        #new id if new band 
        max_id = max(int(band["id"]) for band in data)
        entry["id"] = str(max_id + 1)
    
    
    data.insert(0, entry)

    new_band_name = entry["name"]
    new_similar_artists = entry.get("similar artists", [])

    #changes similar artists' similar artists sections
    if is_new_band:
        for similar_artist in new_similar_artists:
            for band in data:
                if band["name"] == similar_artist and new_band_name not in band.get("similar artists", []):
                    band.setdefault("similar artists", []).append(new_band_name)
    elif old_name and old_name != new_band_name:
        for band in data:
            if old_name in band.get("similar artists", []):
                band["similar artists"].remove(old_name)
                band["similar artists"].append(new_band_name)

    removed_similar_artists = set(old_similar_artists) - set(new_similar_artists)
    for removed_artist in removed_similar_artists:
        for band in data:
            if band["name"] == removed_artist and old_name in band.get("similar artists", []):
                band["similar artists"].remove(old_name)

    for band in data:
        if band["name"] in new_similar_artists and new_band_name not in band.get("similar artists", []):
            band["similar artists"].append(new_band_name)
        elif band["name"] not in new_similar_artists and new_band_name in band.get("similar artists", []):
            band["similar artists"].remove(new_band_name)

    #return id so user will be sent to current view url
    return jsonify({"id": entry["id"]})


   
if __name__ == '__main__':
   app.run(debug = True, port=5001)
