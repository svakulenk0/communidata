#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jan 2, 2017

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Wordcloud generator adopted from https://github.com/amueller/word_cloud/blob/master/examples/simple.py

'''

from os import path
from wordcloud import WordCloud

# d = path.dirname(__file__)

def generate_wordcloud(text):
    # load custom stopword list
    stopwords = set([x.strip() for x in open('stopwords').read().split('\n')])
    print stopwords
    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=2000, width=800, height=600, margin=0).generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")

    # display the image
    # plt.show()

    # save image on disk (+ get rid of the margin trick)
    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
                        hspace = 0, wspace = 0)
    plt.margins(0,0)
    import matplotlib.ticker as ticker
    plt.gca().xaxis.set_major_locator(ticker.NullLocator())
    plt.gca().yaxis.set_major_locator(ticker.NullLocator())
    plt.savefig('results.png', bbox_inches='tight', pad_inches=0.0)

    # The pil way (if you don't have matplotlib)
    #image = wordcloud.to_image()
    #image.show()


def test_generate_wordcloud():
    # descriptions_dump = 'datasets/%s_%s_titles.txt' % (portal_id, snapshot)
    # descriptions_dump = 'datasets/data_gv_at_1701_titles.txt'
    descriptions_dump = 'datasets/www_opendataportal_at_1701_titles.txt'
    # Read the whole text.
    text = open(descriptions_dump).read().decode('utf-8')
    # import unicodedata
    # text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
    # print len(text)
    generate_wordcloud(text)


if __name__ == '__main__':
    test_generate_wordcloud()
