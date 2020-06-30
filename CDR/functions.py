def countLocationsInNewDay(data,targetDays):
    prev = set(); cur = set()
    for index,row in data.iterrows():
        if not row['date'] in targetDays:
            prev.add(','.join([str(row['lon']),str(row['lat'])]))
        else:
            cur.add(','.join([str(row['lon']),str(row['lat'])]))
    res = 0
    for one in cur:
        if not one in prev: res += 1
    return(res)


