#Email:cyber.professional@outlook.com
#Jeremiah (Jay) Williams

import requests as a
from bs4 import BeautifulSoup as b
import pandas as c
import matplotlib.pyplot as e
from mpl_toolkits.mplot3d import Axes3D
import re as f
import numpy as g

def main():
    templ=[]
    temp2=[]
    temp3=[]
    set_max=0
    while len(templ)!=3:
        page0=input("Enter URL for analysy: ")
        templ.append(page0)
    print(templ)
    a0="http://webcache.googleusercontent.com/search?q=cache:"
    def a00(page0,dat):
        a1=['a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'bdi', 'bdo', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'command', 'datalist', 'dd', 'del', 'details', 'dfn', 'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'keygen', 'label', 'legend', 'li', 'main', 'map', 'mark', 'menu', 'meter', 'nav', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'section', 'select', 'small', 'source', 'span', 'strong', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'time', 'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr']
        a2=b(dat,'html.parser')
        a4=0
        a5={}
        for a6 in a1:
            a4=0
            for a7 in a2.find_all(a6):
                a4+=1
            if a4==0:
                pass
            else:
                a5[a6]=a4
        temp3.append(a5)
    def b00(page0):
        b1=a.get(page0)
        if b1.status_code!=200:
                b1=a.get(a0+page0)
                if b1.status_code!=200:
                    print("""We do apologize, but the page you requested for analysis is unavailable.
                    PageStats is used for a simple educational demonstration of analysis on publically
                    available data from the internet. The site or webpage owner may be actively blocking
                    our program from retreiving the requested data. And readind this message also means we
                    have yet to add it to our database. 
                    - Thank you for your understanding!
                    """)
                else:
                    a00(page0,b1.text)
        else:
            a00(page0,b1.text)
    def c00():
        max_0=[]
        for f0 in temp3:
            for f1,f2 in f0.items():
                max_0.append(f2)
        return (max(max_0))
    def d00():
        e.style.use('dark_background')
        fig=e.figure(figsize=(14,7))
        ax=fig.add_subplot(111, projection='3d') 
        depth=0
        colors=['r','b','g']
        for c0 in temp3:
            for c000,c001 in c0.items():
                c1=c0.keys()
                c2=c0.values()
                c3=g.arange(set_max)
                e0=[c]*len(c1)
                e0[0]='c'
                ax.bar(c1, c2)
                ax.set_xlabel('X', labelpad=10)
                ax.set_ylabel('Tag Totals')
                ax.set_title("Tag-Stats!")
                ax.set_yticks(temp2)
                ax.tick_params(axis='x', labelrotation=23)
                fig.autofmt_xdate()
                e.savefig(page0[8:11]+'.png')
    for page0 in templ:
        temp2.append(page0[8:])
        b00(page0)
        set_max=c00()
    print(temp2)
    print(temp3)
    print(set_max)
    d00()
main()