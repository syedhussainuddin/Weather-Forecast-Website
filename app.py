from flask import Flask, render_template, request, send_from_directory
from data2 import json_file, all_data  # Import your JSON generation function

app = Flask(__name__ , static_folder='static')

JSON_FOLDER = 'E:/Uni Projects/zelo'


weather_activities = {
    "Mostly sunny" : ["Go to the beach", "Sunbathe", "Photography"],
    "Clear": ["Go for a walk", "Sunbathe", "Photography"],
    "Partly Cloudy": ["Jogging", "Biking", "Stargazing"],
    "Cloudy": ["Reading indoors", "Visit a museum", "Walk in the park"],
    "Fog": ["Drive carefully", "Stay indoors", "Photography (mysterious feel)"],
    "Rain": ["Indoor workout", "Watch movies", "Read a book"],
    "Snow": ["Skiing", "Building a snowman", "Winter hiking"],
    "Sleet": ["Stay indoors", "Drive cautiously", "Hot beverages"],
    "Drizzle": ["Light walk", "Indoor crafting", "Watch TV shows"],
    "Thunderstorms": ["Stay indoors", "Watch movies", "Listen to music"],
    "Hail": ["Stay indoors", "Protect your car", "Listen to music"],
    "Windy": ["Fly a kite", "Go sailing", "Go windsurfing"],
    "Blizzard": ["Stay indoors", "Read a book", "Enjoy hot drinks"],
    "Dust": ["Stay indoors", "Clean your house", "Stay hydrated"],
    "Sand": ["Stay indoors", "Go to the beach", "Protect skin from sun"],
    "Smoke": ["Stay indoors", "Wear a mask", "Avoid outdoor activities"],
    "Tornado": ["Seek shelter", "Stay indoors", "Monitor weather updates"],
    "Hurricane": ["Stay indoors", "Prepare emergency kit", "Monitor updates"],
    "Freezing Rain": ["Stay indoors", "Drive cautiously", "Warm beverages"],
    "Sunny": ["Go to the beach", "Picnic in the park", "Photography"],
    "Flurries": ["Winter sports", "Photography", "Watch the snow fall"],
    "Overcast": ["Visit a café", "Indoor workout", "Go for a walk"],
    "Isolated Thunderstorms": ["Stay indoors", "Listen to music", "Read a book"],
    "Scattered Thunderstorms": ["Stay indoors", "Watch TV shows", "Cook a meal"],
    "Heavy Rain": ["Indoor activities", "Watch movies", "Relax with a book"],
    "Light Rain": ["Take a walk", "Indoor workout", "Photography"],
    "Moderate Rain": ["Stay indoors", "Watch movies", "Read a book"],
    "Heavy Snow": ["Skiing", "Winter hiking", "Building a snow fort"],
    "Light Snow": ["Go for a walk", "Photography", "Build a snowman"],
    "Moderate Snow": ["Skiing", "Winter hiking", "Photography"],
    "Patchy Fog": ["Go for a walk", "Photography", "Drive cautiously"],
    "Partly Cloudy with Showers": ["Take an umbrella", "Indoor workout", "Read a book"],
    "Showers": ["Take an umbrella", "Indoor activities", "Watch movies"],
    "Cloudy with Showers": ["Stay indoors", "Read a book", "Watch TV shows"],
    "Clear with Showers": ["Take an umbrella", "Indoor workout", "Read a book"],
    "Clear with Snow": ["Winter sports", "Photography", "Go for a walk"],
    "Light Drizzle": ["Take a light walk", "Read a book", "Photography"],
    "Heavy Drizzle": ["Stay indoors", "Watch movies", "Warm drinks"],
    "Freezing Drizzle": ["Stay indoors", "Drive cautiously", "Hot beverages"],
    "Isolated Showers": ["Take an umbrella", "Go for a walk", "Photography"],
    "Scattered Showers": ["Go for a walk", "Indoor workout", "Relax indoors"],
    "Heavy Flurries": ["Winter sports", "Photography", "Indoor activities"],
    "Light Flurries": ["Go for a walk", "Photography", "Winter crafts"],
    "Partly Cloudy with Snow": ["Go for a walk", "Photography", "Build a snowman"],
    "Showers of Rain and Snow": ["Stay indoors", "Watch movies", "Warm beverages"],
    "Cloudy with Snow": ["Winter sports", "Photography", "Go for a walk"],
    "Patchy Freezing Fog": ["Drive carefully", "Stay indoors", "Photography"],
    "Partly Cloudy with Thunderstorms": ["Stay indoors", "Watch TV shows", "Listen to music"],
    "Scattered Clouds": ["Go for a walk", "Biking", "Photography"],
    "Clear with Fog": ["Stay indoors", "Photography", "Read a book"],
    "Patchy Snow": ["Go for a walk", "Photography", "Build a snowman"],
    "Isolated Snow": ["Go for a walk", "Photography", "Winter sports"],
    "Widespread Dust": ["Stay indoors", "Clean your house", "Stay hydrated"],
    "Light Snow Showers": ["Photography", "Build a snowman", "Go for a walk"],
    "Heavy Snow Showers": ["Skiing", "Snowboarding", "Winter sports"],
    "Mixed Rain and Snow": ["Stay indoors", "Watch movies", "Drive cautiously"],
    "Heavy Mixed Rain and Snow": ["Stay indoors", "Read a book", "Watch TV shows"],
    "Light Mixed Rain and Snow": ["Take an umbrella", "Photography", "Indoor activities"],
    "Partly Cloudy with Light Rain": ["Take an umbrella", "Go for a walk", "Indoor workout"],
    "Partly Cloudy with Heavy Rain": ["Stay indoors", "Watch movies", "Read a book"],
    "Light Rain Showers": ["Take an umbrella", "Go for a walk", "Photography"],
    "Heavy Rain Showers": ["Stay indoors", "Watch movies", "Read a book"],
    "Sleet Showers": ["Stay indoors", "Drive cautiously", "Warm drinks"],
    "Thundershowers": ["Stay indoors", "Watch movies", "Listen to music"],
    "Overcast with Showers": ["Stay indoors", "Read a book", "Watch TV shows"],
    "Overcast with Snow": ["Skiing", "Winter hiking", "Photography"],
    "Partly Cloudy with Sleet": ["Stay indoors", "Drive cautiously", "Drink hot beverages"],
    "Isolated Snow Showers": ["Go for a walk", "Photography", "Winter sports"],
    "Clear with Light Snow": ["Go for a walk", "Photography", "Winter crafts"],
    "Clear with Heavy Snow": ["Skiing", "Winter hiking", "Build a snowman"],
    "Clear with Moderate Snow": ["Winter sports", "Photography", "Winter hiking"],
    "Clear with Sleet": ["Stay indoors", "Drive cautiously", "Drink hot beverages"],
    "Clear with Rain": ["Go for a walk", "Photography", "Picnic in the park"]
}

description_activities = {
    "Clear": [
        "Boosts stamina and strengthens leg muscles.",
        "Relaxes the mind and reduces stress.",
        "Enhances creativity and artistic vision."
    ],
    "Partly Cloudy": [
        "Improves cardiovascular health and endurance.",
        "Tones muscles and improves coordination.",
        "Calms the mind and inspires reflection."
    ],
    "Cloudy": [
        "Encourages focus and intellectual growth.",
        "Stimulates creativity and curiosity.",
        "Promotes relaxation and emotional clarity."
    ],
    "Fog": [
        "Improves driving focus and patience.",
        "Promotes relaxation and prevents overstimulation.",
        "Enhances mood through artistic inspiration."
    ],
    "Rain": [
        "Improves core strength and flexibility.",
        "Encourages emotional connection and relaxation.",
        "Boosts intellectual engagement and creativity."
    ],
    "Snow": [
        "Improves balance and builds leg strength.",
        "Enhances creativity and provides fun.",
        "Strengthens muscles and increases stamina."
    ],
    "Sleet": [
        "Encourages safety awareness and caution.",
        "Relaxes the mind and reduces stress.",
        "Soothes the body and mind with warmth."
    ],
    "Drizzle": [
        "Relieves stress and promotes relaxation.",
        "Boosts creativity and hand coordination.",
        "Encourages mental relaxation and focus."
    ],
    "Thunderstorms": [
        "Promotes calmness and reduces anxiety.",
        "Engages creativity and boosts dopamine levels.",
        "Improves emotional balance and creativity."
    ],
    "Hail": [
        "Teaches adaptability and problem-solving.",
        "Encourages relaxation and emotional recovery.",
        "Boosts mood through favorite music."
    ],
    "Windy": [
        "Improves motor skills and coordination.",
        "Increases strength and adrenaline levels.",
        "Boosts energy and improves focus."
    ],
    "Blizzard": [
        "Encourages mental calmness and patience.",
        "Promotes intellectual engagement and joy.",
        "Improves circulation and emotional warmth."
    ],
    "Dust": [
        "Enhances mindfulness and adaptability.",
        "Promotes a clean and organized environment.",
        "Reduces dryness and improves hydration."
    ],
    "Sand": [
        "Encourages relaxation and mental recovery.",
        "Soothes the mind and enhances mindfulness.",
        "Promotes physical protection and care."
    ],
    "Smoke": [
        "Encourages caution and environmental awareness.",
        "Boosts health by reducing pollution exposure.",
        "Reduces respiratory strain and improves focus."
    ],
    "Tornado": [
        "Promotes safety awareness and quick thinking.",
        "Enhances focus and situational preparedness.",
        "Improves mental resilience and adaptability."
    ],
    "Hurricane": [
        "Encourages preparation and problem-solving.",
        "Boosts mental focus and calmness.",
        "Reduces stress through proactive measures."
    ],
    "Freezing Rain": [
        "Promotes safety and situational awareness.",
        "Improves mood with warmth and comfort.",
        "Reduces tension and increases relaxation."
    ],
    "Sunny": [
        "Improves vitamin D and energy levels.",
        "Encourages social bonding and happiness.",
        "Inspires creativity and joy in nature."
    ],
    "Flurries": [
        "Boosts adrenaline and excitement.",
        "Encourages artistic creativity and joy.",
        "Promotes calmness through natural beauty."
    ],
    "Overcast": [
        "Enhances focus and concentration.",
        "Boosts energy and reduces stress.",
        "Promotes physical and mental clarity."
    ],
    "Isolated Thunderstorms": [
        "Promotes calmness and situational awareness.",
        "Boosts creativity and reduces stress.",
        "Encourages intellectual growth and relaxation."
    ],
    "Scattered Thunderstorms": [
        "Promotes calmness and emotional stability.",
        "Encourages intellectual engagement and creativity.",
        "Increases relaxation and mental clarity."
    ],
    "Heavy Rain": [
        "Enhances mindfulness and creative thinking.",
        "Encourages relaxation and emotional growth.",
        "Boosts imagination and mental clarity."
    ],
    "Light Rain": [
        "Encourages physical relaxation and calmness.",
        "Improves core strength and flexibility.",
        "Boosts creativity and emotional clarity."
    ],
    "Moderate Rain": [
        "Encourages mindfulness and calm thinking.",
        "Promotes relaxation and emotional recovery.",
        "Boosts intellectual engagement and creativity."
    ],
    "Heavy Snow": [
        "Improves physical strength and endurance.",
        "Boosts adrenaline and focus.",
        "Enhances creativity and emotional connection."
    ],
    "Light Snow": [
        "Promotes mindfulness and artistic vision.",
        "Encourages physical relaxation and creativity.",
        "Boosts imagination and sense of wonder."
    ],
    "Moderate Snow": [
        "Improves endurance and builds stamina.",
        "Inspires joy and emotional connection.",
        "Boosts mood through scenic beauty."
    ],
    "Patchy Fog": [
        "Improves awareness and patience.",
        "Encourages mindfulness and reflection.",
        "Stimulates creativity and calmness."
    ],
    "Partly Cloudy with Showers": [
        "Boosts energy and stamina.",
        "Encourages emotional relaxation and joy.",
        "Improves focus and mental clarity."
    ],
    "Showers": [
        "Refreshes the mind and reduces stress.",
        "Enhances creativity and relaxation.",
        "Boosts physical endurance and stamina."
    ],
    "Cloudy with Showers": [
        "Encourages mindfulness and creativity.",
        "Promotes physical relaxation and calmness.",
        "Boosts intellectual engagement and focus."
    ],
    "Clear with Showers": [
        "Refreshes the senses and calms the mind.",
        "Boosts focus and emotional clarity.",
        "Encourages relaxation and reflection."
    ],
    "Clear with Snow": [
        "Inspires creativity and artistic thought.",
        "Enhances physical balance and agility.",
        "Boosts mood through scenic beauty."
    ],
    "Light Drizzle": [
        "Improves relaxation and reduces tension.",
        "Encourages mindfulness and focus.",
        "Boosts energy and creativity."
    ],
    "Heavy Drizzle": [
        "Promotes relaxation and emotional recovery.",
        "Improves focus and mental clarity.",
        "Reduces stress and encourages calmness."
    ],
    "Freezing Drizzle": [
        "Enhances safety awareness and focus.",
        "Promotes warmth and relaxation.",
        "Improves mindfulness and clarity."
    ],
    "Isolated Showers": [   
        "Boosts creativity and emotional connection.",
        "Encourages relaxation and emotional balance.",
        "Improves focus and mental clarity."
    ],
    "Light Freezing Rain": [
        "Encourages cautious movement and safety.",
        "Promotes emotional warmth and comfort.",
        "Boosts focus and mental clarity."
    ],
    "Heavy Freezing Rain": [
        "Enhances resilience and adaptability.",
        "Promotes relaxation and patience.",
        "Reduces stress through warmth and calm."
    ],
    "Patchy Light Rain": [
        "Promotes physical relaxation and calmness.",
        "Boosts creativity and emotional clarity.",
        "Encourages mindfulness and thoughtful reflection."
    ],
    "Patchy Moderate Rain": [
        "Improves cardiovascular health and endurance.",
        "Encourages emotional relaxation and peace.",
        "Boosts focus and intellectual engagement."
    ],
    "Patchy Heavy Rain": [
        "Promotes mindfulness and emotional balance.",
        "Reduces stress and increases calmness.",
        "Improves physical stamina and strength."
    ],
    "Patchy Light Snow": [
        "Encourages artistic creativity and mindfulness.",
        "Boosts physical strength and balance.",
        "Promotes emotional relaxation and joy."
    ],
    "Patchy Moderate Snow": [
        "Enhances physical endurance and strength.",
        "Boosts creativity and emotional connection.",
        "Encourages mindfulness and calm thinking."
    ],
    "Patchy Heavy Snow": [
        "Improves stamina and overall fitness.",
        "Promotes creativity and emotional warmth.",
        "Boosts resilience and mental focus."
    ],
    "Light Sleet": [
        "Encourages caution and balance outdoors.",
        "Improves physical resilience and focus.",
        "Promotes relaxation with warmth afterward."
    ],
    "Moderate Sleet": [
        "Enhances awareness and adaptability.",
        "Improves physical strength and agility.",
        "Encourages mental clarity and reflection."
    ],
    "Heavy Sleet": [
        "Builds resilience and mental toughness.",
        "Encourages physical recovery and relaxation.",
        "Improves mindfulness and focus in challenging conditions."
    ],
    "Light Rain Shower": [
        "Relieves stress and promotes relaxation.",
        "Boosts creativity and hand coordination.",
        "Encourages mental relaxation and focus."
    ],
    "Moderate Rain Shower": [
        "Boosts stamina and cardiovascular health.",
        "Promotes mindfulness and intellectual growth.",
        "Encourages emotional relaxation and peace."
    ],
    "Heavy Rain Shower": [
        "Improves endurance and builds mental focus.",
        "Boosts creativity and emotional clarity.",
        "Encourages relaxation and mindfulness."
    ],
    "Light Snow Shower": [
        "Promotes creativity and artistic vision.",
        "Improves balance and builds leg strength.",
        "Encourages mindfulness and joy in nature."
    ],
    "Moderate Snow Shower": [
        "Boosts physical strength and endurance.",
        "Inspires creativity and emotional connection.",
        "Promotes mindfulness and relaxation."
    ],
    "Heavy Snow Shower": [
        "Encourages resilience and adaptability.",
        "Builds strength and physical endurance.",
        "Enhances emotional balance and focus."
    ],
    "Light Sleet Shower": [
        "Improves coordination and balance outdoors.",
        "Promotes resilience and adaptability.",
        "Encourages relaxation with warmth afterward."
    ],
    "Moderate Sleet Shower": [
        "Encourages mindfulness in challenging conditions.",
        "Boosts physical endurance and strength.",
        "Promotes relaxation and mental clarity."
    ],
    "Heavy Sleet Shower": [
        "Enhances resilience and adaptability.",
        "Builds physical strength and stamina.",
        "Encourages relaxation and calmness indoors."
    ],
    "Ice Pellets": [
        "Improves focus and adaptability.",
        "Encourages resilience in challenging situations.",
        "Promotes safety awareness and mindfulness."
    ],
    "Light Ice Pellets": [
        "Promotes caution and focus.",
        "Encourages physical recovery afterward.",
        "Improves emotional balance and clarity."
    ],
    "Moderate Ice Pellets": [
        "Builds resilience and mental focus.",
        "Encourages mindfulness and relaxation.",
        "Boosts physical strength and adaptability."
    ],
    "Heavy Ice Pellets": [
        "Enhances strength and endurance.",
        "Promotes relaxation and emotional recovery.",
        "Encourages focus and mental clarity."
    ]
}

activity_pngs = {
    "Go to the beach" : "sunset.png",
    "Picnic in the park" : "park.png",
    "Fly a kite": "kite.png",
    "Go sailing": "boat.png",
    "Go windsurfing" : "windsurfing.png",
    "Creative hobbies (e.g., painting, drawing)": "paint.png",
    "Reading or journaling": "open-book.png",
    "Meditation or mindfulness exercises": "exercise.png",
    "Swimming": "swimming-icon.png",
    "Hiking or nature walks": "hiking.png",
    "Photography": "photography.png",
    "Socializing with friends or family": "social-media.png",
    "Music (e.g., playing instruments or listening)": "music-note.png",
    "Exercising at the gym": "man-fitness.png",
    "Indoor workouts (e.g., pilates, cardio)": "treadmill.png",
    "Spending time outdoors with pets": "pet.png",
    "Relaxing in a park": "park.png",
    "Camping": "fire.png",
    "Crafting or DIY projects": "paper-crafts.png",
    "Volunteering or community service": "support.png",
    "Walking or running outdoors": "running-icon.png",
    "Cycling or biking": "cycling-icon.png",
    "Yoga or stretching": "yoga-pose.png",
    "Outdoor sports (e.g., soccer, basketball)": "football.png",
    "Artistic writing or poetry": "poetry.png",
    "Dancing": "part-people.png",
    "Gardening": "gardening.png",
    "Cooking or baking": "chef.png",
    "Watching movies or TV shows": "video.png",
    "Playing board games or video games": "console.png",
    "Traveling or exploring new places": "travelling.png",
    "Visiting museums or galleries": "exhibition.png",
    "Fishing": "fishing.png",
    "Visiting a spa or wellness center": "massage.png",
    "Attending live events or concerts": "concert.png",
}

# Route for the landing page
@app.route('/')
def landingpage():
    return render_template('landingpage.html')  

# Route for the weather page
@app.route('/weatherpage', methods=['GET'])
def weatherpage():
    # Get city and country from the search bar
    city = request.args.get('city')
    country = request.args.get('country')

    if not city or not country:
        return "City and Country must be provided", 400

    try:
        json_file(city, country)

    except Exception as e:
        return f"Error generating weather data: {e}", 500
    
    try:
        x = all_data(city, country)
        weather = x['1st_day']['weather_day'] 

        weather_activities_keys = list(weather_activities.keys())
        description_activities_keys = list(description_activities.keys())

        for i in range(len(weather_activities_keys)):
            if weather in weather_activities_keys:
                activities = weather_activities[weather]
                activity1 = activities[0]
                activity2 = activities[1]
                activity3 = activities[2]
            else:
                activity1 = "N/A Available for this weather"
                activity2 = "N/A Available for this weather"
                activity3 = "N/A for this weather"


        for i in range(len(description_activities_keys)):
            if  weather in description_activities_keys:
                descriptions = description_activities[weather]
                description1 = descriptions[0]
                description2 = descriptions[1]
                description3 = descriptions[2]
            else:
                description1 = "N/A Available for this weather"
                description2 = "N/A Availablr for this weather"
                description3 = "N/A Availablr for this weather"
            



    except Exception as e:
        return f"Error in the activities written part: {e}", 500
    

    try:
        accept1 = False
        accept2 = False
        accept3 = False
        keys_list = list(activity_pngs.keys())
        
        if activity1 in keys_list:
            link1 = activity_pngs[activity1]
            accept1 = True
        else:
            link1 = "default.png"

        if activity2 in keys_list:
            link2 = activity_pngs[activity2]
            accept2 = True
        else:
            link2 = "default.png"

        if activity3 in keys_list:
            link3 = activity_pngs[activity3]
            accept3 = True
        else:
            link3 = "default.png"

        # if accept1 == False:
        #     link1 = "default.png"
        # if accept2 == False:
        #     link2 = "default.png"
        # if accept3 == False:
        #     link3 = "default.png"

    except Exception as e:
        return f"Error in the activity pictures part: {e}", 500
    
    return render_template('weatherpage.html', activity1=activity1, activity2=activity2, activity3=activity3, description1=description1, description2=description2, description3=description3, link1=link1, link2=link2, link3=link3)  

# Route to serve the generated JSON file
@app.route('/weather_data.json')
def get_weather_data():
    return send_from_directory(JSON_FOLDER, 'weather_data.json')                            #Hussains Laptop
    #return send_from_directory('E:/github/Weather-App-Project', 'weather_data.json')       #Usmans Laptop

# @app.route('/weather_data.json')
# def send_file(weather_data.json):
#     return send_from_directory(app.static_folder,weather_data)

if __name__ == '__main__':
    app.run(debug=True)
