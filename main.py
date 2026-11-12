import zlib, struct, math, os
W=H=512
px=[[ (255,236,242) for _ in range(W)] for _ in range(H)]
def circ(cx,cy,r,c):
    for y in range(max(0,cy-r),min(H,cy+r+1)):
        for x in range(max(0,cx-r),min(W,cx+r+1)):
            if (x-cx)**2+(y-cy)**2<=r*r: px[y][x]=c
def ell(cx,cy,a,b,c):
    for y in range(max(0,cy-b),min(H,cy+b+1)):
        for x in range(max(0,cx-a),min(W,cx+a+1)):
            if ((x-cx)/a)**2+((y-cy)/b)**2<=1: px[y][x]=c
def tri(p,c):
    xs=[q[0] for q in p];ys=[q[1] for q in p]
    for y in range(min(ys),max(ys)+1):
        for x in range(min(xs),max(xs)+1):
            a,b,d=p
            def s(u,v,w):return (u[0]-w[0])*(v[1]-w[1])-(v[0]-w[0])*(u[1]-w[1])
            q=(x,y);d1=s(q,a,b);d2=s(q,b,d);d3=s(q,d,a)
            if not((d1<0 or d2<0 or d3<0) and (d1>0 or d2>0 or d3>0)): px[y][x]=c
for i,(x,y) in enumerate([(60,60),(450,80),(100,440),(420,430),(256,40)]): circ(x,y,14,(255,200,220))
fur=(255,205,150);dark=(70,40,40)
tri([(120,200),(150,60),(240,140)],fur);tri([(392,200),(362,60),(272,140)],fur)
tri([(145,170),(158,100),(205,145)],(255,170,185));tri([(367,170),(354,100),(307,145)],(255,170,185))
ell(256,300,170,140,fur)
ell(256,340,80,60,(255,240,225))
for sx in(-1,1):
    cx=256+sx*70
    circ(cx,290,32,dark);circ(cx-6*sx*-1 if False else cx+8,278,11,(255,255,255));circ(cx-10,305,5,(255,255,255))
    ell(256+sx*115,345,32,20,(255,160,175))
tri([(240,330),(272,330),(256,348)],(240,110,130))
for sx in(-1,1):
    for t in range(0,60):
        a=t/59*math.pi
        x=int(256+sx*18+sx*math.sin(a)*18*0+ sx*t*0.5);y=int(348+ math.sin(a)*10) if False else int(350+8*math.sin(t/59*math.pi))
        for d in(-1,0,1):
            circ(int(256+sx*(10+t*0.45)),int(352+ (t*0.12)),2,dark) if t%2==0 else None
raw=b''.join(b'\0'+bytes(v for p in r for v in p) for r in px)
def ch(t,d):
    c=struct.pack('>I',len(d))+t+d
    return c+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
png=b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('>IIBBBBB',W,H,8,2,0,0,0))+ch(b'IDAT',zlib.compress(raw,9))+ch(b'IEND',b'')
pass
out='/output/entry.png' if os.path.isdir('/output') else 'entry.png'
open(out,'wb').write(png)
