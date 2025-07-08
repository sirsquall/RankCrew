#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from rankcrew.crew import Rankcrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'singing',
        'topic_keyword' : 'chant, voix, sont, musique, chants, cours, vocale, vocal, tessiture, notes, chanson, chansons, paris, chanteurs, leurs, lyrique, melodie, musicale, apprendre, registre, vocales, différents, note, type, fréquence, soprano, chanteur, aigue, for, apprentissage, paghjella, female, types, enfant, technique, basse, sonore, texte, expression, opéra, paroles, rôles, ténor, bébé, vie, travers, sons, central, techniques, histoire',
        'company' : 'apolline',
        'company_website' : 'https://www.apolline.art/',
        'company_info' : 'Apolline is a Swiss music school specializing in art lessons (singing, piono, guitar, drums, theater, musical theater, manga drawing, comics drawing, painting illustration, academic drawing, painting) for children 6-16 years old. They operate ONLY in French-speaking Switzerland (Lausanne, Geneva, etoy, vevey, montreux, sion, fribourg, yverdon, neuchatel). Services: for the music we offer semi-private 2 person, in person only (no online/video lessons, no home visits), group workshops, vocal coaching for children, and for the visual art and theater is group session in our school, no-online. Target audience: Children from 6-16 years old. Teaching approach: Mix of classical and contemporary techniques, personalized pedagogy. Locations: Physical studios. What they DON\'T offer: Online lessons, home visits, digital platforms, mobile apps, recording services',
        'company_keyword' : 'cours, school',
        'existing_articles' : '',
        'language_list' : 'french, portuguese, arabic',
        'country' : 'Switzerland',
        'ton_of_voice' : 'professional yet accessible',
        'current_date': datetime.now().strftime("%B %d, %Y"),
        
    }

    try:
        Rankcrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'singing',
        'topic_keyword' : 'chant, voix, sont, musique, chants, cours, vocale, vocal, tessiture, notes, chanson, chansons, paris, chanteurs, leurs, lyrique, melodie, musicale, apprendre, registre, vocales, différents, note, type, fréquence, soprano, chanteur, aigue, for, apprentissage, paghjella, female, types, enfant, technique, basse, sonore, texte, expression, opéra, paroles, rôles, ténor, bébé, vie, travers, sons, central, techniques, histoire',
        'company' : 'apolline',
        'company_website' : 'https://www.apolline.art/',
        'company_info' : 'Apolline is a Swiss music school specializing in art lessons (singing, piono, guitar, drums, theater, musical theater, manga drawing, comics drawing, painting illustration, academic drawing, painting) for children 6-16 years old. They operate ONLY in French-speaking Switzerland (Lausanne, Geneva, etoy, vevey, montreux, sion, fribourg, yverdon, neuchatel). Services: for the music we offer semi-private 2 person, in person only (no online/video lessons, no home visits), group workshops, vocal coaching for children, and for the visual art and theater is group session in our school, no-online. Target audience: Children from 6-16 years old. Teaching approach: Mix of classical and contemporary techniques, personalized pedagogy. Locations: Physical studios. What they DON\'T offer: Online lessons, home visits, digital platforms, mobile apps, recording services',
        'company_keyword' : 'cours, school',
        'existing_articles' : '',
        'language_list' : 'french, portuguese, arabic',
        'country' : 'Switzerland',
        'ton_of_voice' : 'formal',
        'current_date': datetime.now().strftime("%B %d, %Y"),
    }
    
    try:
        Rankcrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Rankcrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': 'singing',
        'topic_keyword' : 'chant, voix, sont, musique, chants, cours, vocale, vocal, tessiture, notes, chanson, chansons, paris, chanteurs, leurs, lyrique, melodie, musicale, apprendre, registre, vocales, différents, note, type, fréquence, soprano, chanteur, aigue, for, apprentissage, paghjella, female, types, enfant, technique, basse, sonore, texte, expression, opéra, paroles, rôles, ténor, bébé, vie, travers, sons, central, techniques, histoire',
        'company' : 'apolline',
        'company_website' : 'https://www.apolline.art/',
        'company_info' : 'Apolline is a Swiss music school specializing in art lessons (singing, piono, guitar, drums, theater, musical theater, manga drawing, comics drawing, painting illustration, academic drawing, painting) for children 6-16 years old. They operate ONLY in French-speaking Switzerland (Lausanne, Geneva, etoy, vevey, montreux, sion, fribourg, yverdon, neuchatel). Services: for the music we offer semi-private 2 person, in person only (no online/video lessons, no home visits), group workshops, vocal coaching for children, and for the visual art and theater is group session in our school, no-online. Target audience: Children from 6-16 years old. Teaching approach: Mix of classical and contemporary techniques, personalized pedagogy. Locations: Physical studios. What they DON\'T offer: Online lessons, home visits, digital platforms, mobile apps, recording services',
        'company_keyword' : 'cours, school',
        'existing_articles' : '',
        'language_list' : 'french, portuguese, arabic',
        'country' : 'Switzerland',
        'ton_of_voice' : 'formal',
        'current_date': datetime.now().strftime("%B %d, %Y"),
    }

    try:
        Rankcrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")