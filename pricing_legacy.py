# โค้ดเดิมที่เขียนแบบรีบๆ สำหรับใช้ทำ Characterization Test (ห้ามแก้ไฟล์นี้)
H = []
P = {}

def calc(items, m=None, c=None, dt="2026-10-03"):
    t = 0
    for x in items:
        if x["q"] > 0:
            p = x["p"] * x["q"]
            if x["q"] >= 50:
                p = p * 0.90
            elif x["q"] >= 10:
                p = p * 0.95
            t += p
    if m != None:
        t = t * 0.95
    if c != None:
        if c == "SAVE50":
            t = t - 50
        elif c == "VIP10":
            t = t * 0.90
        elif c == "NEWYEAR":
            if dt == "2026-01-01":
                t = t - 100
    t = round(t, 2)
    if m != None:
        pts = int(t // 10) if t > 0 else 0
        P[m] = P.get(m, 0) + pts
    H.append({"m": m, "t": t, "len": len(H) + 1})
    return t
