import pandas as pd
import numpy as np


def coding_count(listCodes):
    '''
    Take List of codes with some entries having multiple codes and count the number of entries for each code.
    '''
    listOfCodes = listCodes.tolist()
    codes = []
    for i in listOfCodes:
        x = i.split(', ')
        codes.extend(x)
    
    neutral = codes.count('neutral')
    name = codes.count('name')
    llm = codes.count('LLM')
    hacking = codes.count('hacking')
    news = codes.count('news')
    error = codes.count('error')
    tested = codes.count('tested')
    usability = codes.count('usability')
    secret = codes.count('secret')
    government = codes.count('government')
    dominion = codes.count('dominion')
    verifiable = codes.count('verifiable')
    believe = codes.count('believe')
    detection = codes.count('detection')
    transparent = codes.count('transparent')
    rest = len(codes) - neutral - name - llm - hacking - news - error - tested - usability - secret - government - dominion - verifiable - believe - detection - transparent

    return neutral, name, llm, hacking, news, error, tested, usability, secret, government, dominion, verifiable, believe, detection, transparent, rest

def coding_count_p(neutral, name, llm, hacking, news, error, tested, usability, secret, government, dominion, verifiable, believe, detection, transparent, rest):
    hundo_p = neutral + name + llm + hacking + news + error + tested + usability + secret + government + dominion + verifiable + believe + detection + transparent + rest

    neutral = (neutral/hundo_p)*100
    name = (name/hundo_p)*100
    llm = (llm/hundo_p)*100
    hacking = (hacking/hundo_p)*100
    news = (news/hundo_p)*100
    error = (error/hundo_p)*100
    tested = (tested/hundo_p)*100
    usability = (usability/hundo_p)*100
    secret = (secret/hundo_p)*100
    government = (government/hundo_p)*100
    dominion = (dominion/hundo_p)*100
    verifiable = (verifiable/hundo_p)*100
    believe = (believe/hundo_p)*100
    detection =  (detection/hundo_p)*100
    transparent = (transparent/hundo_p)*100
    rest = (rest/hundo_p)*100

    return neutral, name, llm, hacking, news, error, tested, usability, secret, government, dominion, verifiable, believe, detection, transparent, rest


def fact_coding_count(listCodes):
    newList = listCodes.tolist()
    fake = newList.count('fake')
    election_feeling = newList.count('election_feeling')
    machine_feeling = newList.count('machine_feeling')
    election_fact = newList.count('election_fact')
    machine_fact = newList.count('machine_fact')
    misc = newList.count('misc')
    rest = len(newList) - fake - election_feeling - machine_feeling - election_fact - machine_fact - misc

    return fake, election_feeling, machine_feeling, election_fact, machine_fact, misc, rest

def fact_coding_percent(fake, election_feeling, machine_feeling, election_fact, machine_fact, misc, rest):
    hun_percent = fake + election_feeling + machine_feeling + election_fact + machine_fact + misc + rest
    fake_p = (fake / hun_percent)*100
    election_feeling_p = (election_feeling / hun_percent)*100
    machine_feeling_p = (machine_feeling / hun_percent)*100
    election_fact_p = (election_fact / hun_percent)*100
    machine_fact_p = (machine_fact / hun_percent)*100
    misc_p = (misc / hun_percent)*100
    rest_p = (rest / hun_percent)*100

    return fake_p, election_feeling_p, machine_feeling_p, election_fact_p, machine_fact_p, misc_p, rest_p


