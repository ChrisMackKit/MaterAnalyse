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
    hacking_pos = codes.count('hacking_pos')
    hacking_neg = codes.count('hacking_neg')
    news = codes.count('news')
    error_pos = codes.count('error_pos')
    error_neg = codes.count('error_neg')
    tested = codes.count('tested')
    usability = codes.count('usability')
    secret_pos = codes.count('secret_pos')
    secret_neg = codes.count('secret_neg')
    government = codes.count('government')
    dominion = codes.count('dominion')
    verifiable_pos = codes.count('verifiable_pos')
    verifiable_neg = codes.count('verifiable_neg')
    believe = codes.count('believe')
    detection = codes.count('detection')
    transparent = codes.count('transparent')
    rest = len(codes) - neutral - name - llm - hacking_pos - hacking_neg - news - error_pos - error_neg - tested - usability - secret_pos - secret_neg - government - dominion - verifiable_pos - verifiable_neg - believe - detection - transparent

    return neutral, name, llm, hacking_pos, hacking_neg, news, error_pos, error_neg, tested, usability, secret_pos, secret_neg, government, dominion, verifiable_pos, verifiable_neg, believe, detection, transparent, rest

def coding_count_list(listCodes):
    '''
    Take List of codes with some entries having multiple codes and count the number of entries for each code.
    '''
    total = len(listCodes)
    listOfCodes = listCodes.tolist()
    codes = []
    for i in listOfCodes:
        x = i.split(', ')
        codes.extend(x)
    
    neutral = codes.count('neutral')
    name = codes.count('name')
    llm = codes.count('LLM')
    hacking_pos = codes.count('hacking_pos')
    hacking_neg = codes.count('hacking_neg')
    news = codes.count('news')
    error_pos = codes.count('error_pos')
    error_neg = codes.count('error_neg')
    tested = codes.count('tested')
    usability = codes.count('usability')
    secret_pos = codes.count('secret_pos')
    secret_neg = codes.count('secret_neg')
    government = codes.count('government')
    dominion = codes.count('dominion')
    verifiable_pos = codes.count('verifiable_pos')
    verifiable_neg = codes.count('verifiable_neg')
    believe = codes.count('believe')
    detection = codes.count('detection')
    transparent = codes.count('transparent')
    rest = len(codes) - neutral - name - llm - hacking_pos - hacking_neg - news - error_pos - error_neg - tested - usability - secret_pos - secret_neg - government - dominion - verifiable_pos - verifiable_neg - believe - detection - transparent

    all_val = [neutral, name, llm, hacking_pos, hacking_neg, news, error_pos, error_neg, tested, usability, secret_pos, secret_neg, government, dominion, verifiable_pos, verifiable_neg, believe, detection, transparent]
    return_list = [(x/total)*100 for x in all_val]
        

    return return_list

def coding_count_p(neutral, name, llm, hacking, news, error, tested, usability, secret, government, dominion, verifiable, believe, detection, transparent, rest, amount):
    #hundo_p = neutral + name + llm + hacking + news + error + tested + usability + secret + government + dominion + verifiable + believe + detection + transparent + rest

    neutral = (neutral/amount)*100
    name = (name/amount)*100
    llm = (llm/amount)*100
    hacking = (hacking/amount)*100
    news = (news/amount)*100
    error = (error/amount)*100
    tested = (tested/amount)*100
    usability = (usability/amount)*100
    secret = (secret/amount)*100
    government = (government/amount)*100
    dominion = (dominion/amount)*100
    verifiable = (verifiable/amount)*100
    believe = (believe/amount)*100
    detection =  (detection/amount)*100
    transparent = (transparent/amount)*100
    rest = (rest/amount)*100

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

def fact_coding_count_list(listCodes):
    total = len(listCodes)
    newList = listCodes.tolist()
    fake = newList.count('fake')
    election_feeling = newList.count('election_feeling')
    machine_feeling = newList.count('machine_feeling')
    election_fact = newList.count('election_fact')
    machine_fact = newList.count('machine_fact')
    misc = newList.count('misc')
    rest = len(newList) - fake - election_feeling - machine_feeling - election_fact - machine_fact - misc
    #old: [fake, election_feeling, machine_feeling, election_fact, machine_fact, misc]
    list_codes = [machine_fact, machine_feeling, election_fact, election_feeling, fake, misc]
    return_list = [(x / total)*100 for x in list_codes]

    return return_list


def fact_coding_percent(fake, election_feeling, machine_feeling, election_fact, machine_fact, misc, rest, amount):
    #hun_percent = fake + election_feeling + machine_feeling + election_fact + machine_fact + misc + rest
    fake_p = (fake / amount)*100
    election_feeling_p = (election_feeling / amount)*100
    machine_feeling_p = (machine_feeling / amount)*100
    election_fact_p = (election_fact / amount)*100
    machine_fact_p = (machine_fact / amount)*100
    misc_p = (misc / amount)*100
    rest_p = (rest / amount)*100

    return fake_p, election_feeling_p, machine_feeling_p, election_fact_p, machine_fact_p, misc_p, rest_p


