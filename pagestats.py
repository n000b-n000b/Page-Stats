#Email:cyber.professional@outlook.com
#Jeremiah (Jay) Williams

import requests as a
from bs4 import BeautifulSoup as b
import pandas as c
import matplotlib.pyplot as e
from mpl_toolkits.mplot3d import Axes3D
import re as f
import numpy as g
import subprocess as h
import streamlit as i
import plotly.express as j
import plotly.graph_objects as k
import time

def main(a000,a001,a002):
    templ=[]
    temp2=[]
    temp3=[]
    coun00=0
    blacklist=['security','access','forbidden','denied','protection','detected','unusual']
    set_max=0
    i.set_page_config(layout='wide')
    i.markdown("<h1 style='text-align: center; '> Welcome to Page-Statz !</h1>", unsafe_allow_html=True)
    col00,col001=i.columns([4,5])
    with col00:
        i.caption("<h1 style='text-align: center'>Overview</h1><p style='font-size: 26px; text-align: center'>Page-Statz is a simple and user friendly educational webpage analysis &amp; visualization project. Summarizing the markup language of the sources provided in a 3D surface graph. Updates and features are in development. In the mean time enter three URLs and have a look at the data!</p>",unsafe_allow_html=True)
    with col001:
        form=i.form("Main", clear_on_submit=True)
        a000=form.text_input("Enter URL 1: ")
        a001=form.text_input("Enter URL 2: ")
        a002=form.text_input("Enter URL 3: ")
        b000=form.form_submit_button("Analyze")
    if b000:
        progress_text = "Analyzing . . ."
        pbar = i.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.1)
            pbar.progress(percent_complete + 1, text=progress_text)
        if (len(a000)==0 or len(a001)==0 or len(a002)==0):
            i.warning("Please enter a URL for each field above.")
            pass
        if ('https://' not in a000):
            a000='https://'+a000
        if ('https://' not in a001):
            a001='https://'+a001
        if ('https://' not in a002):
            a002='https://'+a002
        templ.extend((a000,a001,a002))
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
                    coun00+=1
                    pass
                else:
                    for b2 in blacklist:
                        if b2 in b1.text and b1.text.count(b2)==1:
                            coun00+=1
                            templ.remove(page0)
                            if coun00<=2:
                                i.warning("""Apologies""")
                            else:
                                i.write("Source "+page0+" is non-compliant. Displaying other sources in visualization.")
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
        fig=e.figure(figsize=(20,7))
        ax=fig.add_subplot(111, projection='3d') 
        for c0 in temp3:
            for c000,c001 in c0.items():
                c1=c0.keys()
                c2=c0.values()
                c3=g.arange(set_max)
                e0=[c]*len(c1)
                e0[0]='c'
                ax.bar(c1, c2, zs=c001, zdir='y')
        ax.set_xlabel('Tag', labelpad=25)
        ax.set_ylabel(temp2)
        ax.set_zlabel('Tag Totals')
        ax.set_title("Tag-Stats!")
        fig.autofmt_xdate()
        i.pyplot(fig)
        e.savefig(page0[8:11]+'.png')
    def d01():
        if len(temp3)==0:
            pass
        else:
            frame00=c.DataFrame.from_dict(temp3).drop_duplicates()
            frame00=frame00.fillna(0)
            try:
                frame00.index=[templ[0][8:],templ[1][8:],templ[2][8:]]
                with i.container():
                    i.data_editor(frame00, width=9000, height=175)
                    with i.container():
                        z=frame00
                        x,y= frame00.columns, frame00.index
                        fig00=k.Figure(data=k.Surface(z=z,x=x,y=y))
                        fig00.update_layout(title='Page-Stats!', title_x=0.5, autosize=False,
                                width=1080, height=900,
                                margin=dict(l=65, r=50, b=65, t=90,))
                        i.plotly_chart(fig00)
            except:
                try:
                    frame00.index=[templ[0][8:],templ[1][8:]]
                    with i.container():
                        i.data_editor(frame00, width=9000, height=175)
                        with i.container():
                            z=frame00
                            x,y= frame00.columns, frame00.index
                            fig00=k.Figure(data=k.Surface(z=z,x=x,y=y))
                            fig00.update_layout(title='Page-Stats!', title_x=0.5, autosize=False,
                                    width=1080, height=900,
                                    margin=dict(l=65, r=50, b=65, t=90,))
                            i.plotly_chart(fig00)
                except:
                    pass

            with i.container():
                i.subheader("Front-End")
                i.caption("Alayah H. - "+'\nhttps://www.linkedin.com/in/alayah-howard/')
                i.subheader("Backend & Visuals")
                i.caption("Jay-C137 - "+'\nhttps://www.linkedin.com/in/jay-williams-c137/')
    try:
        if len(templ)==2 or len(templ)==3:
            for page0 in templ:
                temp2.append(page0)
                b00(page0)
                set_max=c00()
            #d00()
            d01()
        else:
            pass
    except:
        i.warning("""Apologies, but in order for Page-Stats! remain within ethical boundaries. 
                  We are unable to analyze your previous entry, all sources provided are non-compliant.
                  PageStats is used for a simple educational demonstration of analysis on native markup language used to create the websites provided.
                  This means security measures are in place blocking our program from retrieving the data. 
                  Please try entering alternate URLs.
                  - Thank you for your understanding!""")
main(a000='',a001='',a002='')
