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


def generate_wordcloud(text):
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")

    # # lower max_font_size
    # wordcloud = wordcloud.WordCloud(max_font_size=40).generate(text)
    # plt.figure()
    # plt.imshow(wordcloud)
    # plt.axis("off")
    plt.show()

    # The pil way (if you don't have matplotlib)
    #image = wordcloud.to_image()
    #image.show()


def test_generate_wordcloud():
    # descriptions_dump = 'datasets/%s_%s_titles.txt' % (portal_id, snapshot)
    descriptions_dump = 'datasets/data_gv_at_titles.txt'
    # Read the whole text.
    text = open(descriptions_dump).read()
    generate_wordcloud(text)


if __name__ == '__main__':
    test_generate_wordcloud()
