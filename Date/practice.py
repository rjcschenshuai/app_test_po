def get_date():
    import yaml
    with open('./search_date.yaml','r',encoding='utf-8')as f:
        date=yaml.safe_load(f)
    date=date.values()
    list=[]
    for x in date:
        p=tuple(x.values())
        list.append(p)
    return list
