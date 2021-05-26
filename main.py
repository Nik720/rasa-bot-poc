import json


def findData(node="start"):
    with open('data.json') as f:
        data = json.load(f)
    newObj = data['start']
    childs = []
    text = ""
    WA_text = ""

    if not node == 'start':
        nodeObj = findNode(newObj, node)
        newObj = nodeObj.get('data')

    childData = newObj if node == 'start' else newObj['children']
    for k in childData:
        if k == 'text':
            text = childData[k]
        elif k == 'WA_text':
            WA_text = childData[k]
        elif k == 'children':
            for j in childData[k]:
                childs.append({'title': j['title'], 'payload': j['payload']})

    finalData = {
        'text': text,
        'WA_text': WA_text,
        'children': childs,
        'intent': node
    }
    return finalData


def findNode(d, node):
    import collections

    finalData = collections.OrderedDict()

    def recurse(t, n):
        if isinstance(t, list):
            for i in range(len(t)):
                recurse(t[i], n)
        elif isinstance(t, dict):
            for k, v in t.items():
                if k == 'id' and v == n:
                    finalData['data'] = t
                recurse(v, n)

    recurse(d, node)

    return finalData
