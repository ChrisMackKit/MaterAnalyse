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
    fig, ax = plt.subplots(figsize=(5, 6))
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

def drawStockBar_trust_5_save(title, valueList, namingList, title_extra = ''):
    path='G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Trust_Dist'
    y1 = np.array([(np.sum(valueList[0] == 1)/ len(valueList[0]))*100, (np.sum(valueList[1] == 1)/ len(valueList[1]))*100,(np.sum(valueList[2] == 1)/ len(valueList[2])) * 100, (np.sum(valueList[3] == 1)/ len(valueList[3]))*100, (np.sum(valueList[4] == 1)/ len(valueList[4])) * 100])
    y2 = np.array([(np.sum(valueList[0] == 2)/ len(valueList[0]))*100, (np.sum(valueList[1] == 2)/ len(valueList[1]))*100, (np.sum(valueList[2] == 2)/ len(valueList[2])) * 100, (np.sum(valueList[3] == 2)/ len(valueList[3]))*100, (np.sum(valueList[4] == 2)/ len(valueList[4])) * 100])
    y3 = np.array([(np.sum(valueList[0] == 3)/ len(valueList[0]))*100, (np.sum(valueList[1] == 3)/ len(valueList[1]))*100, (np.sum(valueList[2] == 3)/ len(valueList[2])) * 100, (np.sum(valueList[3] == 3)/ len(valueList[3]))*100, (np.sum(valueList[4] == 3)/ len(valueList[4])) * 100])
    fig, ax = plt.subplots(figsize=(5, 6))
    colors = ["#973A11", "#FFAE6C", "#DDDAD5"]
    y_values = [y1,y2,y3]
    labels = ["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"]
    y_bottom = np.zeros(len(namingList))
    for i in range(3):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)

        y_bottom += y
    plt.xlabel("")
    plt.ylabel("Amount")
    plt.legend(["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(f'Do you trust the voting system? {title_extra}')
    plt.savefig(f"{path}\\Trust_{title}.png", dpi=300, bbox_inches='tight')
    plt.close

def drawStockBar_trust_6_save(title, valueList, namingList, title_extra = ''):
    path='G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Trust_Dist'
    y1 = np.array([(np.sum(valueList[0] == 1)/ len(valueList[0]))*100, (np.sum(valueList[1] == 1)/ len(valueList[1]))*100,(np.sum(valueList[2] == 1)/ len(valueList[2])) * 100, (np.sum(valueList[3] == 1)/ len(valueList[3]))*100, (np.sum(valueList[4] == 1)/ len(valueList[4])) * 100, (np.sum(valueList[5] == 1)/ len(valueList[5])) * 100])
    y2 = np.array([(np.sum(valueList[0] == 2)/ len(valueList[0]))*100, (np.sum(valueList[1] == 2)/ len(valueList[1]))*100, (np.sum(valueList[2] == 2)/ len(valueList[2])) * 100, (np.sum(valueList[3] == 2)/ len(valueList[3]))*100, (np.sum(valueList[4] == 2)/ len(valueList[4])) * 100, (np.sum(valueList[5] == 2)/ len(valueList[5])) * 100])
    y3 = np.array([(np.sum(valueList[0] == 3)/ len(valueList[0]))*100, (np.sum(valueList[1] == 3)/ len(valueList[1]))*100, (np.sum(valueList[2] == 3)/ len(valueList[2])) * 100, (np.sum(valueList[3] == 3)/ len(valueList[3]))*100, (np.sum(valueList[4] == 3)/ len(valueList[4])) * 100, (np.sum(valueList[5] == 3)/ len(valueList[5])) * 100])
    fig, ax = plt.subplots(figsize=(6, 6))
    
    colors = ["#973A11", "#FFAE6C", "#DDDAD5"]
    y_values = [y1,y2,y3]
    labels = ["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"]
    y_bottom = np.zeros(len(namingList))
    for i in range(3):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)

        y_bottom += y
    plt.xlabel("")
    plt.ylabel("Percentage", fontsize=14)
    plt.legend(["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(f'Do you trust the voting system? {title_extra}')
    plt.savefig(f"{path}\\Trust_{title}.png", dpi=300, bbox_inches='tight')
    plt.close

def drawStockBar_fact_code_6_save(title, valueList, namingList, title_extra = ''):
    path='G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Fact_Code\\StackBar'
    if len(valueList) == 6:
        y1 = np.array([valueList[0][0], valueList[1][0], valueList[2][0], valueList[3][0], valueList[4][0], valueList[5][0]])
        y2 = np.array([valueList[0][1], valueList[1][1], valueList[2][1], valueList[3][1], valueList[4][1], valueList[5][1]])
        y3 = np.array([valueList[0][2], valueList[1][2], valueList[2][2], valueList[3][2], valueList[4][2], valueList[5][2]])
        y4 = np.array([valueList[0][3], valueList[1][3], valueList[2][3], valueList[3][3], valueList[4][3], valueList[5][3]])
        y5 = np.array([valueList[0][4], valueList[1][4], valueList[2][4], valueList[3][4], valueList[4][4], valueList[5][4]])
        y6 = np.array([valueList[0][5], valueList[1][5], valueList[2][5], valueList[3][5], valueList[4][5], valueList[5][5]])
        fig, ax = plt.subplots(figsize=(5, 6))
    if len(valueList) == 5:
        y1 = np.array([valueList[0][0], valueList[1][0], valueList[2][0], valueList[3][0], valueList[4][0]])
        y2 = np.array([valueList[0][1], valueList[1][1], valueList[2][1], valueList[3][1], valueList[4][1]])
        y3 = np.array([valueList[0][2], valueList[1][2], valueList[2][2], valueList[3][2], valueList[4][2]])
        y4 = np.array([valueList[0][3], valueList[1][3], valueList[2][3], valueList[3][3], valueList[4][3]])
        y5 = np.array([valueList[0][4], valueList[1][4], valueList[2][4], valueList[3][4], valueList[4][4]])
        y6 = np.array([valueList[0][5], valueList[1][5], valueList[2][5], valueList[3][5], valueList[4][5]])
        fig, ax = plt.subplots(figsize=(5, 6))
    elif len(valueList) == 3:
        y1 = np.array([valueList[0][0], valueList[1][0], valueList[2][0]])
        y2 = np.array([valueList[0][1], valueList[1][1], valueList[2][1]])
        y3 = np.array([valueList[0][2], valueList[1][2], valueList[2][2]])
        y4 = np.array([valueList[0][3], valueList[1][3], valueList[2][3]])
        y5 = np.array([valueList[0][4], valueList[1][4], valueList[2][4]])
        y6 = np.array([valueList[0][5], valueList[1][5], valueList[2][5]])
        fig, ax = plt.subplots(figsize=(5, 6))
    elif len(valueList) == 2:
        y1 = np.array([valueList[0][0], valueList[1][0]])
        y2 = np.array([valueList[0][1], valueList[1][1]])
        y3 = np.array([valueList[0][2], valueList[1][2]])
        y4 = np.array([valueList[0][3], valueList[1][3]])
        y5 = np.array([valueList[0][4], valueList[1][4]])
        y6 = np.array([valueList[0][5], valueList[1][5]])
        fig, ax = plt.subplots(figsize=(3, 6))
    else:
        y1 = np.array([valueList[0][0]])
        y2 = np.array([valueList[0][1]])
        y3 = np.array([valueList[0][2]])
        y4 = np.array([valueList[0][3]])
        y5 = np.array([valueList[0][4]])
        y6 = np.array([valueList[0][5]])
        fig, ax = plt.subplots(figsize=(2, 6))

    colors = ["#973A11", "#FFAE6C", "#DDDAD5", "#8AD8E4", "#1074AF", '#4F7942']
    y_values = [y1,y2,y3,y4,y5,y6]
    labels = ['machine_fact', 'machine_feeling', 'election_fact', 'election_feeling', 'fake', 'misc']
    y_bottom = np.zeros(len(namingList))
    for i in range(6):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)
        y_bottom += y
    plt.xlabel("")
    plt.ylabel("Percentage", fontsize=14)
    plt.legend(['machine_fact', 'machine_feeling', 'election_fact', 'election_feeling', 'fake', 'misc'], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(f'Coding Open Question - fact vs feeling {title_extra}', fontsize=15)
    ax = plt.gca()
    ax.set_ylim([0,102])
    plt.savefig(f"{path}\\Fact_Code_{title}.png", dpi=300, bbox_inches='tight')
    plt.close

def drawStockBar_fact_code__save(title, valueList, namingList, title_extra = ''):
    path='G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Fact_Code\\StackBar'
    if len(valueList) == 6:
        y1 = np.array([valueList[0][0] + valueList[0][2], valueList[1][0] + valueList[1][2], valueList[2][0] + valueList[2][2], valueList[3][0] + valueList[3][2], valueList[4][0] + valueList[4][2], valueList[5][0] + valueList[5][2]])
        y2 = np.array([valueList[0][1] + valueList[0][3], valueList[1][1] + valueList[1][3], valueList[2][1] + valueList[2][3], valueList[3][1] + valueList[3][3], valueList[4][1] + valueList[4][3], valueList[5][1] + valueList[5][3]])
        y3 = np.array([valueList[0][4], valueList[1][4], valueList[2][4], valueList[3][4], valueList[4][4], valueList[5][4]])
        y4 = np.array([valueList[0][5], valueList[1][5], valueList[2][5], valueList[3][5], valueList[4][5], valueList[5][5]])
        fig, ax = plt.subplots(figsize=(5, 6))
    if len(valueList) == 5:
        y1 = np.array([valueList[0][0] + valueList[0][2], valueList[1][0] + valueList[1][2], valueList[2][0] + valueList[2][2], valueList[3][0] + valueList[3][2], valueList[4][0] + valueList[4][2]])
        y2 = np.array([valueList[0][1] + valueList[0][3], valueList[1][1] + valueList[1][3], valueList[2][1] + valueList[2][3], valueList[3][1] + valueList[3][3], valueList[4][1] + valueList[4][3]])
        y3 = np.array([valueList[0][4], valueList[1][4], valueList[2][4], valueList[3][4], valueList[4][4]])
        y4 = np.array([valueList[0][5], valueList[1][5], valueList[2][5], valueList[3][5], valueList[4][5]])
        fig, ax = plt.subplots(figsize=(5, 6))
    elif len(valueList) == 3:
        y1 = np.array([valueList[0][0] + valueList[0][2], valueList[1][0] + valueList[1][2], valueList[2][0] + valueList[2][2]])
        y2 = np.array([valueList[0][1] + valueList[0][3], valueList[1][1] + valueList[1][3], valueList[2][1] + valueList[2][3]])
        y3 = np.array([valueList[0][4], valueList[1][4], valueList[2][4]])
        y4 = np.array([valueList[0][5], valueList[1][5], valueList[2][5]])
        fig, ax = plt.subplots(figsize=(5, 6))
    elif len(valueList) == 2:
        y1 = np.array([valueList[0][0] + valueList[0][2], valueList[1][0] + valueList[1][2]])
        y2 = np.array([valueList[0][1] + valueList[0][3], valueList[1][1] + valueList[1][3]])
        y3 = np.array([valueList[0][4], valueList[1][4]])
        y4 = np.array([valueList[0][5], valueList[1][5]])
        fig, ax = plt.subplots(figsize=(3, 6))
    else:
        y1 = np.array([valueList[0][0] + valueList[0][2]])
        y2 = np.array([valueList[0][1] + valueList[0][3]])
        y3 = np.array([valueList[0][4]])
        y4 = np.array([valueList[0][5]])
        fig, ax = plt.subplots(figsize=(2, 6))

    colors = ["#973A11", "#FFAE6C", "#DDDAD5", "#1074AF"]
    y_values = [y1,y2,y3,y4]
    labels = ['fact', 'feeling', 'fake', 'misc']
    y_bottom = np.zeros(len(namingList))
    for i in range(4):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)

        y_bottom += y

    plt.xlabel("")
    plt.ylabel("Percentage", fontsize=14)
    plt.legend(['fact', 'feeling', 'fake', 'misc'], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(f'Coding Open Question - fact vs feeling {title_extra}', fontsize=15)
    ax = plt.gca()
    ax.set_ylim([0,102])
    plt.savefig(f"{path}\\Fact_Code_VS_{title}.png", dpi=300, bbox_inches='tight')
    plt.close

def drawStockBar_trust_3_save(title, valueList, namingList, title_extra = ''):
    path='G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Trust_Dist'
    y1 = np.array([(np.sum(valueList[0] == 1)/ len(valueList[0]))*100, (np.sum(valueList[1] == 1)/ len(valueList[1]))*100,(np.sum(valueList[2] == 1)/ len(valueList[2])) * 100])
    y2 = np.array([(np.sum(valueList[0] == 2)/ len(valueList[0]))*100, (np.sum(valueList[1] == 2)/ len(valueList[1]))*100, (np.sum(valueList[2] == 2)/ len(valueList[2])) * 100])
    y3 = np.array([(np.sum(valueList[0] == 3)/ len(valueList[0]))*100, (np.sum(valueList[1] == 3)/ len(valueList[1]))*100, (np.sum(valueList[2] == 3)/ len(valueList[2])) * 100])
    fig, ax = plt.subplots(figsize=(4, 6))
    colors = ["#973A11", "#FFAE6C", "#DDDAD5"]
    y_values = [y1,y2,y3]
    labels = ["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"]
    y_bottom = np.zeros(len(namingList))
    for i in range(3):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)

        y_bottom += y
    plt.xlabel("")
    plt.ylabel("Percentage", fontsize=14)
    plt.legend(["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(f'Do you trust the voting system? {title_extra}')
    plt.savefig(f"{path}\\Trust_{title}.png", dpi=300, bbox_inches='tight')
    plt.close

def drawStockBar_trust_2_save(title, valueList, namingList, title_extra = ''):
    path='G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Trust_Dist'
    y1 = np.array([(np.sum(valueList[0] == 1)/ len(valueList[0]))*100, (np.sum(valueList[1] == 1)/ len(valueList[1]))*100])
    y2 = np.array([(np.sum(valueList[0] == 2)/ len(valueList[0]))*100, (np.sum(valueList[1] == 2)/ len(valueList[1]))*100])
    y3 = np.array([(np.sum(valueList[0] == 3)/ len(valueList[0]))*100, (np.sum(valueList[1] == 3)/ len(valueList[1]))*100])
    fig, ax = plt.subplots(figsize=(4, 6))
    colors = ["#973A11", "#FFAE6C", "#DDDAD5"]
    y_values = [y1,y2,y3]
    labels = ["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"]
    y_bottom = np.zeros(len(namingList))
    for i in range(3):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)

        y_bottom += y
    plt.xlabel("")
    plt.ylabel("Percentage", fontsize=14)
    plt.legend(["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(f'Do you trust the voting system? {title_extra}')
    plt.savefig(f"{path}\\Trust_{title}.png", dpi=300, bbox_inches='tight')
    plt.close

def drawStockBar_trust_3(title, valueList, valueList2, valueList3, namingList, title_extra = ''):

    y1 = np.array([(np.sum(valueList == 1)/ len(valueList))*100, (np.sum(valueList2 == 1)/ len(valueList2))*100, (np.sum(valueList3 == 1)/ len(valueList3)) * 100])
    y2 = np.array([(np.sum(valueList == 2)/ len(valueList))*100, (np.sum(valueList2 == 2)/ len(valueList2))*100, (np.sum(valueList3 == 2)/ len(valueList3)) * 100])
    y3 = np.array([(np.sum(valueList == 3)/ len(valueList))*100, (np.sum(valueList2 == 3)/ len(valueList2))*100, (np.sum(valueList3 == 3)/ len(valueList3)) * 100])
    fig, ax = plt.subplots(figsize=(3, 6))
    colors = ["#973A11", "#FFAE6C", "#DDDAD5"]
    y_values = [y1,y2,y3]
    labels = ["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"]
    y_bottom = np.zeros(len(namingList))
    for i in range(3):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)

        y_bottom += y
    plt.xlabel("Group")
    plt.ylabel("Percentage", fontsize=14)
    plt.legend(["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("")
    plt.show()

def drawStockBar_trust_2(title, valueList, valueList2, namingList, title_extra = ''):

    y1 = np.array([(np.sum(valueList == 1)/ len(valueList))*100, (np.sum(valueList2 == 1)/ len(valueList2))*100])
    y2 = np.array([(np.sum(valueList == 2)/ len(valueList))*100, (np.sum(valueList2 == 2)/ len(valueList2))*100])
    y3 = np.array([(np.sum(valueList == 3)/ len(valueList))*100, (np.sum(valueList2 == 3)/ len(valueList2))*100])
    fig, ax = plt.subplots(figsize=(4, 6))
    colors = ["#973A11", "#FFAE6C", "#DDDAD5"]
    y_values = [y1,y2,y3]
    labels = ["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"]
    y_bottom = np.zeros(len(namingList))
    for i in range(3):
        y = y_values[i]
        bars = ax.bar(namingList, y, bottom=y_bottom, color=colors[i], label=labels[i])

        # Prozentwerte in die Stacks schreiben
        for bar, val, bottom in zip(bars, y, y_bottom):
            height = bar.get_height()
            if height > 0:  # Nur anzeigen, wenn der Balken eine Höhe hat
                percentage = f'{height:.1f}%'
                y_center = bottom + height / 2
                ax.text(bar.get_x() + bar.get_width() / 2, y_center, percentage,
                        ha='center', va='center', color='black', fontsize=10)

        y_bottom += y
    plt.xlabel("")
    plt.ylabel("Percentage", fontsize=14)
    plt.legend(["I trust the voting system", "I do not trust the voting system", "I am unsure / undecided"], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title("")
    plt.show()



def draw_boxplot_6(value_list, data_name, score, group_names, folder, field_2='', max=5.1, field_3=''):
        path=f'G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\BoxPlots\\{folder}'   
        
        #labeling_boxes = [f"Group {i+1}" for i in range(len(value_list))]
        plt.figure(figsize =(5, 6))
        plt.boxplot(value_list, labels = group_names, showmeans=True)
        #plt.ylabel(f'{score}', fontsize=14)
        if field_2 == '':
            plt.ylabel(f"{score}", fontsize=16)
        elif field_2 != '' and field_3 == '':
            plt.ylabel(f"{score} ({field_2} only)", fontsize=16)
        elif field_3 != '':
            plt.ylabel(f"{score} ({field_3} {field_2} only)", fontsize=16)
        plt.grid(True, linestyle='--', alpha=0.7)
        ax = plt.gca()
        ax.set_ylim([0.9,max])
        ax.tick_params(axis='x', labelsize=15)
        plt.savefig(f"{path}\\plot_{data_name}_{score}_{field_2}_{field_3}.png", dpi=300, bbox_inches='tight')
        plt.close()

def zeichne_balkendiagramm(werte, beschriftungen, title, labels, age =''):
    path='G:\\Meine Ablage\\Masterthese\\Data Visualisierung\\Reason_Code_percent'
    anzahl_balken = len(werte[0])
    x_positionen = np.arange(anzahl_balken)  # Erzeugt numerische Positionen für die Balken
    bar_width = 0.4  # Breite der Balken
    #plt.figure(figsize=(10, 6))  # Optional: Legt die Größe des Diagramms fest
    bar1 = plt.bar(x_positionen - bar_width, werte[0], color='#973A11', align='center', width=bar_width, label=labels[0])
    bar2 = plt.bar(x_positionen, werte[1], color="#FFAE6C", align='center', width=bar_width, label=labels[1])
    #bar3 = plt.bar(x_positionen + bar_width, werte[2], color="#DDDAD5", align='center', width=bar_width, label=labels[2])
    plt.legend(loc='upper right', fontsize=8)  # Legende hinzufügen
    # Beschriftung der x-Achse mit den gegebenen Beschriftungen
    plt.xticks(x_positionen, beschriftungen, rotation=90, ha='right')  # Rotation für bessere Lesbarkeit

    #plt.xlabel(x_achse)
    plt.ylabel(f"% of participants", fontsize=14)
    plt.title(f'{title} {age}', fontsize=14)
    plt.tight_layout()  # Sorgt dafür, dass alle Beschriftungen ins Diagramm passen
    ax = plt.gca()
    ax.set_ylim([0,40])
    plt.savefig(f"{path}\\Reason_code_{title}_percent.png", dpi=300, bbox_inches='tight')
    #plt.show()
    plt.close()
