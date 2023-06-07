"""
Rules to give a bonus
- each employee begins with a bonus factor of 1
- for each employee, if they perform better than the person sitting next to them, the bonus is given +1 (and +2 if better than either side)

Example:

Input [1, 2, 3, 2, 3, 5, 1]
Output [1, 2, 3, 1, 2, 3, 1]
"""

def getBonuses(performance):
    count = len(performance)
    bonus = [1] * count

    for i in range(1, count):
        if performance[i - 1] < performance[i]:
            bonus[i] = bonus[i - 1] + 1

    for i in range(count - 2, -1, -1):
        if performance[i + 1] < performance[i]:
            bonus[i] = max(bonus[i], bonus[i + 1] + 1)

    return bonus


print(getBonuses([1, 2, 3, 2, 3, 5, 1]))

