import numpy as np
import matplotlib.pyplot as plt

#Pie Diagram
def drawPie_trust(g1):
    perc_trust = (np.sum(g1 == 1) / len(g1)) * 100
    perc_no_trust = (np.sum(g1 == 2) / len(g1)) * 100
    perc_not_sure = (np.sum(g1 == 3) / len(g1)) * 100
    y = np.array([perc_trust, perc_no_trust, perc_not_sure])
    plt.pie(y, labels=['Trust','No Trust','Not Sure'])
    plt.show()

def drawPie_fact_code(g1):
    machine_fact = (np.sum(g1 == 'machine_fact') / len(g1)) * 100
    election_fact = (np.sum(g1 == 'election_fact') / len(g1)) * 100
    machine_feeling = (np.sum(g1 == 'machine_feeling') / len(g1)) * 100
    election_feeling = (np.sum(g1 == 'election_feeling') / len(g1)) * 100
    fake = (np.sum(g1 == 'fake') / len(g1)) * 100
    misc = (np.sum(g1 == 'misc') / len(g1)) * 100
    y = np.array([machine_fact, election_fact, machine_feeling, election_feeling, fake, misc])
    plt.pie(y, labels = ['machine_fact', 'election_fact', 'machine_feeling', 'election_feeling', 'fake', 'misc'])
    plt.show()

#Stocked Bar Diagram
def drawStockBar_trust_5(valueList, valueList2, valueList3, valueList4, valueList5):

    y1 = np.array([(np.sum(valueList == 1)/ len(valueList))*100, (np.sum(valueList2 == 1)/ len(valueList2))*100, (np.sum(valueList3 == 1)/ len(valueList3)) * 100, (np.sum(valueList4 == 1)/ len(valueList4))*100, (np.sum(valueList5 == 1)/ len(valueList5)) * 100])
    y2 = np.array([(np.sum(valueList == 2)/ len(valueList))*100, (np.sum(valueList2 == 2)/ len(valueList2))*100, (np.sum(valueList3 == 2)/ len(valueList3)) * 100, (np.sum(valueList4 == 2)/ len(valueList4))*100, (np.sum(valueList5 == 2)/ len(valueList5)) * 100])
    y3 = np.array([(np.sum(valueList == 3)/ len(valueList))*100, (np.sum(valueList2 == 3)/ len(valueList2))*100, (np.sum(valueList3 == 3)/ len(valueList3)) * 100, (np.sum(valueList4 == 3)/ len(valueList4))*100, (np.sum(valueList5 == 3)/ len(valueList5)) * 100])
    
    x = ['A', 'B', 'C', 'D', 'E']

    # plot bars in stack manner
    plt.bar(x, y1, color='#000080')
    plt.bar(x, y2, bottom=y1, color='#1F51FF')
    plt.bar(x, y3, bottom=y1+y2, color='#A7C7E7')
    plt.xlabel("Group")
    plt.ylabel("Amount")
    plt.legend(["Trust", "No Trust", "Not Sure"])
    plt.title("")
    plt.show()

def drawStockBar_trust_3(valueList, valueList2, valueList3):

    y1 = np.array([(np.sum(valueList == 1)/ len(valueList))*100, (np.sum(valueList2 == 1)/ len(valueList2))*100, (np.sum(valueList3 == 1)/ len(valueList3)) * 100])
    y2 = np.array([(np.sum(valueList == 2)/ len(valueList))*100, (np.sum(valueList2 == 2)/ len(valueList2))*100, (np.sum(valueList3 == 2)/ len(valueList3)) * 100])
    y3 = np.array([(np.sum(valueList == 3)/ len(valueList))*100, (np.sum(valueList2 == 3)/ len(valueList2))*100, (np.sum(valueList3 == 3)/ len(valueList3)) * 100])
    
    x = ['A', 'B', 'C']

    # plot bars in stack manner
    plt.bar(x, y1, color='#000080')
    plt.bar(x, y2, bottom=y1, color='#1F51FF')
    plt.bar(x, y3, bottom=y1+y2, color='#A7C7E7')
    plt.xlabel("Group")
    plt.ylabel("Amount")
    plt.legend(["Trust", "No Trust", "Not Sure"])
    plt.title("")
    plt.show()

def drawStockBar_trust_2(valueList, valueList2):

    y1 = np.array([(np.sum(valueList == 1)/ len(valueList))*100, (np.sum(valueList2 == 1)/ len(valueList2))*100])
    y2 = np.array([(np.sum(valueList == 2)/ len(valueList))*100, (np.sum(valueList2 == 2)/ len(valueList2))*100])
    y3 = np.array([(np.sum(valueList == 3)/ len(valueList))*100, (np.sum(valueList2 == 3)/ len(valueList2))*100])
    
    x = ['A', 'B']

    # plot bars in stack manner
    plt.bar(x, y1, color='#000080')
    plt.bar(x, y2, bottom=y1, color='#1F51FF')
    plt.bar(x, y3, bottom=y1+y2, color='#A7C7E7')
    plt.xlabel("Group")
    plt.ylabel("Amount")
    plt.legend(["Trust", "No Trust", "Not Sure"])
    plt.title("")
    plt.show()


'''x = ['A', 'B', 'C', 'D']
y1 = np.array([10.1, 20, 10, 30])
y2 = np.array([20, 25.3, 15, 25])
y3 = np.array([12, 15, 19.5, 6])
y4 = np.array([10, 29, 13.34, 19])

print(y1)
# plot bars in stack manner
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='y')
plt.bar(x, y4, bottom=y1+y2+y3, color='g')
plt.xlabel("Teams")
plt.ylabel("Score")
plt.legend(["Round 1", "Round 2", "Round 3", "Round 4"])
plt.title("Scores by Teams in 4 Rounds")
plt.show()'''
