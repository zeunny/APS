import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[.]+', '.', new_id)
    if len(new_id) > 0 and new_id[0] == '.': new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.': new_id = new_id[:-1]
    if len(new_id) == 0: new_id = 'a'
    if len(new_id) > 15: new_id = new_id[:15]
    if len(new_id) > 0 and new_id[-1] == '.': new_id = new_id[:-1]
    while len(new_id) < 3:
        new_id += new_id[-1]
            
    return new_id
