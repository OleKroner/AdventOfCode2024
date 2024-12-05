rule_dictionary: dict[int, list[int]] = {}

rules = []
updates = []

def add_rule(key: int, value: int):
    if rule_dictionary.get(key):
        rule_dictionary[key].append(value)
    else:
        rule_dictionary[key] = [value]

def order_update(update: list[int]):
    update_is_incorrect = True
    while update_is_incorrect:
        temp_update = update.copy()
        seen_pages = []

        is_incorrect = True

        for page in update:
            if page in rule_dictionary.keys() and not set(rule_dictionary[page]).isdisjoint(seen_pages):
                incorrect_rule = set(rule_dictionary[page]).intersection(seen_pages)
                temp_update.remove(page)
                temp_update.insert(temp_update.index(incorrect_rule.pop()), page)
                is_incorrect = False
            seen_pages.append(page)
        
        update = temp_update
        if is_incorrect:
            update_is_incorrect = False
    
    return update

with open("./input.txt") as file:
    sections = file.read().split("\n\n")

    for rule in sections[0].split():
        items = rule.split("|")
        rules.append((int(items[0]), int(items[1])))
        add_rule(int(items[0]), int(items[1]))
    
    for update in sections[1].split():
        items = update.split(",")
        parsed_updated = []
        for item in items:
            parsed_updated.append(int(item))
        
        updates.append(parsed_updated)

middle_sum = 0
fixed_middle_sum = 0

for update in updates:
    seen_pages = []
    is_correct = True

    for page in update:
        if page in rule_dictionary.keys() and not set(rule_dictionary[page]).isdisjoint(seen_pages):
            is_correct = False
        seen_pages.append(page)
    
    if is_correct:
        #print("Correct")
        middle_sum += update[(len(update) - 1) // 2]
    else:
        fixed_update = order_update(update)
        fixed_middle_sum += fixed_update[(len(fixed_update) - 1) // 2]

print(middle_sum)
print(fixed_middle_sum)