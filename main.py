#!/usr/bin/env python3
"""
Hackstory Project: The Assassination of Nizam al-Mulk
A Flask web application that tells the story of this pivotal historical event
"""

from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Story data structure
STORY_DATA = {
    "title": "The Assassination of Nizam al-Mulk",
    "subtitle": "How a Single Dagger Toppled an Empire",
    "pages": [
        {
            "id": 1,
            "title": "The Mountain Fortress",
            "text": [
                "High in the Alborz Mountains, veiled in mist and legend, stood Alamūt — a fortress carved into stone and silence, nestled deep within the isolated valley of the same name.",
                "It was here that Ḥasan-i Ṣabbāḥ, leader of the Nizārī Ismaʿilis, built not an empire, but a weaponized faith.",
                "Their elite assassins — fedāʾīs — struck with precision, blades drawn in crowded markets or royal courts. Disguised as beggars, monks, or merchants, they never returned — and never missed."
            ],
            "images": [
                {"id": "alamut_fortress", "alt": "Alamut Castle perched on mountain peak"},
                {"id": "paradise_garden", "alt": "Hassan's paradise garden within the fortress"},
                {"id": "fedai_training", "alt": "Assassin training in moonlit courtyard"}
            ]
        },
        {
            "id": 2,
            "title": "The Rising Empire",
            "text": [
                "But the greatest enemy of Hassan-i Sabbah's shadowy kingdom was the Great Seljuk Empire.",
                "The Seljuks had emerged in the 11th century as Turkic nomads who converted to Sunni Islam and swept across Persia like a divine wind.",
                "To the Seljuks, the Nizari Ismailis represented everything that threatened the Islamic order they sought to establish."
            ],
            "images": [
                {"id": "seljuk_map", "alt": "Map of the vast Seljuk Empire"},
                {"id": "turkic_cavalry", "alt": "Seljuk horsemen charging into battle"},
                {"id": "seljuk_court", "alt": "Magnificent Seljuk royal court"}
            ]
        },
        {
            "id": 3,
            "title": "The Grand Vizier",
            "text": [
                "For thirty years, one man had been the architect of this golden age. Nizam al-Mulk — Abu Ali al-Hasan ibn Ali — was not merely a vizier, but the soul of an empire.",
                "Through the Nizamiyyah madrasas he established across the empire, knowledge flourished from Baghdad to Samarkand.",
                "Yet this 74-year-old master of statecraft had become Hassan-i Sabbah's ultimate target."
            ],
            "images": [
                {"id": "nizam_portrait", "alt": "Portrait of the wise vizier Nizam al-Mulk"},
                {"id": "nizamiyyah_school", "alt": "Students learning in Nizamiyyah madrasa"},
                {"id": "administration", "alt": "Efficient Persian bureaucracy at work"}
            ]
        },
        {
            "id": 4,
            "title": "The Fatal Night",
            "text": [
                "On the night of October 14, 1092, fate finally caught up with the great vizier.",
                "As darkness enveloped the camp, a figure emerged from the shadows. Cloaked in the simple robes of a wandering dervish, the stranger approached the flickering campfire.",
                "'Hassan-i Sabbah sends his regards!' the assassin cried, his mission complete."
            ],
            "images": [
                {"id": "night_caravan", "alt": "Persian caravan camping under stars"},
                {"id": "approaching_assassin", "alt": "Cloaked figure approaching in darkness"},
                {"id": "assassination_moment", "alt": "The fatal moment of assassination"}
            ]
        },
        {
            "id": 5,
            "title": "The Empire's Fall",
            "text": [
                "Within thirty-five days of his vizier's death, Sultan Malik-Shah himself was found dead in his tent.",
                "The succession crisis that followed was catastrophic. Malik-Shah's sons fought brutal wars against each other.",
                "What had once been a unified empire stretching from the Mediterranean to Central Asia fragmented into dozens of petty sultanates."
            ],
            "images": [
                {"id": "empire_fragmentation", "alt": "Map showing empire breaking apart"},
                {"id": "succession_wars", "alt": "Brothers fighting for the throne"},
                {"id": "crusader_arrival", "alt": "Crusaders finding a weakened Islamic world"}
            ]
        },
        {
            "id": 6,
            "title": "Legacy of the Dagger",
            "text": [
                "The Hashashins would terrorize the Middle East for another 166 years, their very name becoming synonymous with political murder.",
                "The murder of Nizam al-Mulk proved that in an age of faith and steel, the most dangerous weapon was not the sword, but absolute conviction.",
                "From his mountain fortress, Hassan-i Sabbah watched his enemies' empire burn. Alamūt was more than a fortress — it was a message: no one was untouchable."
            ],
            "images": [
                {"id": "hassan_portrait", "alt": "Hassan-i Sabbah, the Old Man of the Mountain"},
                {"id": "spreading_fear", "alt": "Fear of assassins spreads across the land"},
                {"id": "alamut_legacy", "alt": "Alamut's lasting symbolic message"}
            ]
        }
    ]
}


SOURCES = [
    {
        "title": "The Assassins: A Radical Sect in Islam",
        "author": "Bernard Lewis",
        "year": "1967",
        "publisher": "Oxford University Press"
    },
    {
        "title": "The Seljuks: Politics, Society and Culture",
        "author": "Christian Lange and Songül Mecit",
        "year": "2011",
        "publisher": "Edinburgh University Press"
    },
    {
        "title": "Nizam al-Mulk: His Thought and the Experience of Government in Medieval Islam",
        "author": "Hubert Darke",
        "year": "1978",
        "publisher": "Curzon Press"
    }
]


@app.route('/')
def index():
    return render_template('index.html', story_data=STORY_DATA)


@app.route('/story')
def story():
    return render_template('story.html', pages=STORY_DATA['pages'])


@app.route('/api/page/<int:page_id>')
def get_page(page_id):
    for page in STORY_DATA['pages']:
        if page['id'] == page_id:
            return jsonify(page)
    return jsonify({'error': 'Page not found'}), 404


@app.route('/api/story')
def get_story():
    return jsonify(STORY_DATA)


@app.route('/sources')
def sources():
    return render_template('sources.html', sources=SOURCES)


@app.route('/about')
def about():
    team_info = {
        "project_name": "The Assassination of Nizam al-Mulk: How a Single Dagger Toppled an Empire",
        "description": "An interactive digital storytelling experience that brings to life the pivotal assassination of the great Seljuk vizier Nizam al-Mulk in 1092 CE. This single act of political murder led to the collapse of one of history's greatest Islamic empires and changed the course of the Crusades.",
        "why_chosen": "This story represents a perfect example of how individual actions can reshape civilizations. The assassination demonstrates the power of strategic political violence and shows how the mighty Seljuk Empire's collapse enabled Crusader success in the Holy Land.",
        "team_members": [
            {"name": "Your Name", "grade": "12", "role": "Lead Developer & Historical Researcher"},
            {"name": "Team Member 2", "grade": "11", "role": "Frontend Designer & Content Writer"},
            {"name": "Team Member 3", "grade": "12", "role": "Visual Artist & UI/UX Designer"}
        ]
    }
    return render_template('about.html', team_info=team_info)


def create_templates():
    if not os.path.exists('templates'):
        os.makedirs('templates')

    if not os.path.exists('static'):
        os.makedirs('static')
        os.makedirs('static/css')
        os.makedirs('static/js')
        os.makedirs('static/images')


def save_story_data():
    with open('story_data.json', 'w', encoding='utf-8') as f:
        json.dump(STORY_DATA, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    create_templates()
    save_story_data()

    app.run(debug=True, host='0.0.0.0', port=5000)